'''
Created on

@author: Jerry

Admin Utils, process the admin related operations
'''
import time, datetime
from LunchLoginForm import CousineRegForm
from models import CousineBase, RestaurantBase, NewOrderRecord, SERVICE_TYPE, ORDER_STATE, CookingTypeBase


def create_new_cousine(cousine_name, cousine_restaurant, service_time,  cousine_price, cousine_image):
    '''
    create the new cousine and add to the record
    :return:
    '''
    # print RestaurantBase.objects.all()
    exist_restaurant = RestaurantBase.objects.filter(name__exact=cousine_restaurant)
    if not exist_restaurant:
        print "restaurant not exists"
        raise Exception

    exist_cousine = CousineBase.objects.filter(cousine_name__exact=cousine_name,
                                               restaurant_name__exact=cousine_restaurant)
    if exist_cousine:
        print "Cuisine existing"
        if cousine_price:
            exist_cousine.cousine_price = cousine_price
        if service_time:
            exist_cousine.service_time = service_time
        if cousine_image:
            exist_cousine.picture = cousine_image
        print "Cuisine updated"

    else:
        cousine = CousineBase(cousine_name=cousine_name,
                              restaurant_name=cousine_restaurant,
                              cousine_price=cousine_price,
                              service_time = service_time,
                              picture = cousine_image)
        cousine.save()
        print "New cuisine record added"
        print cousine.picture


def create_new_restaurant(name, address, phone, rest_type):
    """
    Create new restaurant record
    """
    existing_record = RestaurantBase.objects.filter(name__exact=name)

    if existing_record:
        print "Restaurant record already existing"
        if address:
            existing_record.address = address
        if phone:
            existing_record.phone = phone
        if rest_type:
            existing_record.type = CookingTypeBase(type_name=rest_type)
        print "Updated restaurant DB"

    else:
        cooking_type = CookingTypeBase(type_name=rest_type)
        
        restaurant = RestaurantBase(name=name,
                                    address=address,
                                    phone=phone,
                                    type=cooking_type)
        restaurant.save()
        print "New restaurant record added to DB"