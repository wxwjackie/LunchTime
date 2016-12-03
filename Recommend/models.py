from __future__ import unicode_literals

from django.db import models
from Lunch.models import CousineBase

# Create your models here.

class ItemFeatureBase(models.Model):
    '''
    Base class for Item-related feature, it's common feature for all the cousine
    '''
    #feature name, i.e. materials, flavor, 
    cousine_id = models.ForeignKey(CousineBase)

    #feature
    materials_name = models.CharField(max_length=50)
    
    # cooked, fried, steamed, cooled
    cook_method = models.CharField(max_length=50)
    
    # spicy, sweet, salty, wild, 
    flavor = models.CharField(max_length=50)
    
    # estimated Calories
    calories = models.CharField(max_length=50)


GENDER_TYPE = (
               ('M', "MALE"),
               ('F', "FEMALE")
               )

AGE_RANGE = (
             ('A', "20-25"),
             ('B', "26-30"),
             ('C', "31-35"),
             ('D', "36-40"),
             ('E', "41-50"),
             ('F', "50+")
             )

class UserFeatureBase(models.Model):
    '''
    Base class for User-profile feature, it's common feature for all the users' profile
    '''
    user_gender = models.CharField(max_length=50, choices=GENDER_TYPE)
    user_age    = models.CharField(max_length=20, choices=AGE_RANGE)
    

    