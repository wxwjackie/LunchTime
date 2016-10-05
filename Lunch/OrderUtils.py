'''
Created on 

@author: Jerry

Order Utils, some module to generate the order 
'''
import time
from .models import CousineBase, RestaurantBase, NewOrderRecord, SERVICE_TYPE, ORDER_STATE
from register.models import UserRecord
import re

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


def change_order_state(order_id, old_state, new_state):
    '''
    change the order state, from
    '''
    

def generate_order(user_name, product_list, quantity_list):
    '''
    generate the order list based on the product and quantity
    '''

    if not product_list or not quantity_list:
        return
    
    order_id = generate_order_id()
    user_ = UserRecord.objects.filter(user_name__exact=user_name)
    i = 0
    for product_id in product_list:
        cousine = CousineBase.objects.get(id=product_id)
        order = NewOrderRecord(order_serial_no=str(order_id), \
                           expected_time="Lunch", \
                           order_by_one= list(user_)[0],\
                           cousine=cousine,\
                           quantity=quantity_list[i], \
                           order_state="Submitted")
        
        order.save()
        i = i + 1
    
    return True
    
def get_last_n_order(number=1):
    '''
    get the order list before certain time, return n
    return:
    
    { 
    id:[orderobj, orderobj,...],
    ...
    }
    '''
    id_list = NewOrderRecord.objects.values('order_serial_no').distinct()[0:number]
 
    ret_list = {}
    
    for id in id_list:
        id_list = []
        order_list = NewOrderRecord.objects.filter(order_serial_no__exact=id['order_serial_no'])

        for order in order_list:
            id_list.append(order)
        ret_list[id['order_serial_no']] = id_list
    return ret_list
    