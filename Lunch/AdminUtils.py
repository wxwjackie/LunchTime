'''
Created on

@author: Jerry

Admin Utils, process the admin related operations
'''
import time, datetime
from LunchLoginForm import CousineRegForm
from models import CousineBase, RestaurantBase, NewOrderRecord, SERVICE_TYPE, ORDER_STATE


def create_new_cousine(cousine_name, cousine_restaurant, service_time,  cousine_price, cousine_image,):
    '''
    create the new cousine and add to the record
    :return:
    '''
    exist_cousine = CousineBase.objects.filter(cousine_name__exact=cousine_name)
    print RestaurantBase.objects.all()
    exist_restaurant = RestaurantBase.objects.filter(name__exact='KFC')[0]
    if not exist_restaurant:
        print "restaurant not exists"

    if exist_cousine:
        print "the cousine already exists"

    else:
        cousine = CousineBase(cousine_name=cousine_name,
                              restaurant_name=exist_restaurant,
                              cousine_price=cousine_price,
                              service_time = service_time,
                              picture = cousine_image)
        cousine.save()
        print cousine.picture


