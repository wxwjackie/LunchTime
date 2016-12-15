'''
Created on 

@author: Jerry

Order Utils, some module to generate the order 
'''
import time, datetime
from models import CousineBase, RestaurantBase, NewOrderRecord, SERVICE_TYPE, ORDER_STATE
from register.models import UserRecord
import re
from time import strftime, gmtime

def idenfity_product_id(product_list):
    '''
    product_list
    '''
    new_list = [id.split('product_')[1] for id in product_list]
    return new_list

def generate_order_id():
    '''
    generate an unique id for each order, one order might contains several records
    '''
    return int(time.time())


def change_order_score(order_id, cousine_name, score):
    '''
    change the history order score
    '''
    if not score:
        return False
    order_list = NewOrderRecord.objects.filter(order_serial_no=order_id)
    if not order_list:
        print "Failed to get order data from NewOrderRecord"
        return False
    for order in order_list:
        if isinstance(cousine_name, str) and order.cousine.cousine_name == cousine_name:
            order.score = score
            order.save()
        else:
            order.score = score
            order.save()
    order_list = NewOrderRecord.objects.filter(order_serial_no=order_id)
    for order in order_list:
        print order.cousine.cousine_name, order.score
    return True
def change_order_state(order_id, new_state):
    '''
    change the order state, from
    '''
    if (not order_id) or (not new_state):
        return False

    order_list = NewOrderRecord.objects.filter(order_serial_no=order_id)
    if not order_list:
        print "Failed to get order data from NewOrderRecord"
        return False
    order = order_list[0]
    print "BEFORE: order_id=[%s]; order_state=[%s]; new_state=[%s]" % (order.order_serial_no, order.order_state, new_state)
    
    if order.order_state != new_state:
        order.order_state = new_state
        order.save()
    
    print "AFTER: order_id=[%s]; order_state=[%s]" % (order.order_serial_no, order.order_state)
    return True


def generate_order(user_name, product_list, quantity_list):
    '''
    generate the order list based on the product and quantity
    '''

    if not product_list or not quantity_list:
        return
    
    date = strftime("%Y-%m-%d", gmtime())
    order_id = generate_order_id()
    user_ = UserRecord.objects.filter(user_name__exact=user_name)
    i = 0
    for product_id in product_list:
        cousine = CousineBase.objects.get(id=product_id)
        order = NewOrderRecord(date=date, \
                            order_serial_no=str(order_id), \
                           expected_time="Lunch", \
                           order_by_one= list(user_)[0],\
                           cousine=cousine,\
                           quantity=quantity_list[i], \
                           order_state="Submitted")
        
        order.save()
        i = i + 1
    
    return True


def get_last_n_order(number=1, user_name=None):
    '''
    get the order list before certain time, return n
    return:
    
    { 
    id:[orderobj, orderobj,...],
    ...
    }
    '''

    id_list_queryset = NewOrderRecord.objects.values('order_serial_no').distinct().order_by('-order_serial_no')
    
    #filter the user
    if user_name:
        user_obj = UserRecord.objects.filter(user_name__exact=user_name)
        id_list_queryset = id_list_queryset.filter(order_by_one__exact=user_obj)
        
    id_list = id_list_queryset[0:number]
    
    ret_list = {}
    
    for id in id_list:
        id_list = []
        order_list = NewOrderRecord.objects.filter(order_serial_no__exact=id['order_serial_no'])

        for order in order_list:
            id_list.append(order)
        ret_list[id['order_serial_no']] = id_list
    return ret_list


def get_today_order():
    '''
    Get today's order
    return:
    {
    id_1: [orderObj, orderObj,...],
    id_2: [orderObj, orderObj,...],
    ...}
    '''
    today_time_tuple = datetime.date.today().timetuple()
    today_timestamp = time.mktime(today_time_tuple)
    id_list = NewOrderRecord.objects.filter(order_serial_no__gte=today_timestamp).distinct()

    ret_list = {}
    
    for id_item in id_list:
        print type(id_item)
        id_list = []
        order_list = NewOrderRecord.objects.filter(order_serial_no__exact=id_item.order_serial_no)
    
        for order in order_list:
            id_list.append(order)
        ret_list[id_item.order_serial_no] = id_list
        
    return ret_list


def get_orders_by_user(user_name, start=None, end=None):
    '''
    get the orders belong to certain user between time stamp start and end
    :param user_name: user's name
    :param start: time stamp start, default none, means all
    :param end: time stamp end
    :return: list of user orders
    '''
    ret_list = []
    user_obj = UserRecord.objects.filter(user_name__exact=user_name)
    if not user_obj:
        return ret_list

    if start is None or end is None:

        ret_list = NewOrderRecord.objects.filter(order_by_one__exact=user_obj)
    else:
        ret_list = NewOrderRecord.objects.filter(order_by_one__exact=user_obj,
                                                 order_serial_no__gte=start,
                                                 order_serial_no__lte=end)

    return ret_list


def get_cousine_by_name(cousine_name):
    '''
    Get the full record of the cousine by name
    :param cousine_name: cousine name, list or not
    :return: object
    '''
    ret_list = []
    if isinstance(cousine_name, list):
        for cousine in cousine_name:
            ret_list.append(list(CousineBase.objects.filter(cousine_name__exact=cousine))[0])
    else:
        ret_list.append(list(CousineBase.objects.filter(cousine_name__exact=cousine_name))[0])

    return ret_list


def get_cousine_list():
    '''
    Get all cousine list
    :return:  a list
    '''
    return list(CousineBase.objects.all())


def get_consine_frequency(user_name, include_all=True, reverse=True):
    '''
    Returen the consine list orderd by frequency
    Used to recommend consine
    @param include_all: if False, cousine that hasn't been orderd will not be returned
    '''
    order_list = get_orders_by_user(user_name)
    if not order_list:
        return []

    frequency_map = {}
    for order in order_list:
        if frequency_map.has_key(order.cousine.cousine_name):
            frequency_map[order.cousine.cousine_name] += 1
        else:
            frequency_map[order.cousine.cousine_name] = 1

    # include_all make whether return cousine hasn't been orderd
    if include_all:
        cousine_list = list(CousineBase.objects.all())
        for cousine in cousine_list:
            if frequency_map.has_key(cousine.cousine_name):
                continue
            frequency_map[cousine.cousine_name] = 0


    sorted_frequency_map = sorted(frequency_map.items(), key=lambda d:d[1], reverse=reverse)
    return  sorted_frequency_map


def get_resturant_frequency(user_name, reverse=True):
    '''
    Retruen the resturant Frequency list by user.
    Used to recommend resturant
    '''
    order_list = get_orders_by_user(user_name)
    if not order_list:
        return []
    frequency_map = {}
    for order in order_list:
        restaurant = order.cousine.restaurant_name
        frequency_map.setdefault(restaurant.name, 0)
        frequency_map[restaurant.name] += 1
    print frequency_map

    sorted_restarant_map = sorted(frequency_map.items(), key=lambda d:d[1], reverse=reverse)
    print sorted_restarant_map
    return sorted_restarant_map


def get_CFR_data(include_all=False):
    '''
    return all the users' order data
    '''
    users = UserRecord.objects.all()
    data = {}
    for user in users:
        data.setdefault(user.user_name, {})
        user_data = get_consine_frequency(user.user_name, include_all)
        if not user_data:
            continue
        total = sum([value[1] for value in user_data])
        print user.user_name, total, user_data
        for cousine, times in user_data:
            data[user.user_name][cousine] = times / (total + 0.0)

    return data


if __name__ == '__main__':
    print get_cousine_list()