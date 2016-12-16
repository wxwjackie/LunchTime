# coding=utf-8
#!/usr/bin/python

from django.db import models
from register.models import UserRecord


help_txt = """
1 . other   ;
2 . chuan cai;
3 . lu cai   ;
4 . yue cai  ;
5 . su cai   ;
6 . min cai  ;
7 . zhe cai  ;
8 . xiang cai;
9 . hui cai  ;
10. qing zhen;
11. bei jing cai;
"""
# Create your models here.
class CookingTypeBase(models.Model):
    '''
            chuan, lu, yue, su, min,zhe, xiang, hui
    '''
    type_name = models.CharField(max_length=20, default="chuan")
    type_num = models.IntegerField(null=False, default=2, primary_key=True, help_text=help_txt)
    def __str__(self):
        return self.type_name

class RestaurantBase(models.Model):
    '''
    Restaurant
    '''
    name = models.CharField(max_length=50);
    address = models.CharField(max_length=1024)
    #the telephone
    phone = models.CharField(max_length=50);

    type = models.ForeignKey(CookingTypeBase, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s' % (self.name)


SERVICE_TYPE = (
                ('B', "Breakfase"),
                ('L', "Lunch"),
                ('D', "Dinner"),
                ('A', "All day")
                )

class CousineBase(models.Model):
    '''
    A base class for Cousine
    '''
    SERVICE_TYPE = (
                (u'B', u"Breakfast"),
                (u'L', u"Lunch"),
                (u'D', u"Dinner"),
                (u'A', u"All day")
                )
    #class Meta:
    #    abstract = True
    #The restraurant name
    #cousine name
    cousine_name = models.CharField(max_length=50)
    #restaurant name
#     restaurant_name = models.CharField(max_length=50)
    restaurant_name = models.ForeignKey(RestaurantBase, verbose_name="restaurant_name", default=0)
    #price
    cousine_price = models.CharField(max_length=25)
    #service time
    service_time = models.CharField(max_length=25, choices=SERVICE_TYPE)
    # picture path
    picture = models.ImageField(upload_to='restaurant/%Y/%m/%d', blank=True, null=True)
    
    def __str__(self):
        return self.cousine_name
    
    
#Now the following is the employee information
class StaffBase(models.Model):
    '''
    Staff of Infinera
    '''
   
    name = models.CharField(max_length=50)
    work_phone = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    staff_id = models.CharField(max_length=50)
    email_addr = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class GroupBase(models.Model):
    """
    Group of Staff
    """
    name = models.CharField(max_length=50)
    #members of this group
    members = models.ManyToManyField(StaffBase, related_name="group_members_list")
    email_addr = models.CharField(max_length=50)
    #manager of this group
    manager = models.ForeignKey(StaffBase, related_name="group_manager")
    
    def __str__(self):
        return self.name
    
#Order states are defined as followed
ORDER_STATE = (
               ('SUB', 'Submitted'),
               ('CAC', 'Canceled'),
               ('CF', 'Confirmed'),
               ('FR', 'Food Ready'),
               ('FS', 'Finished'),
               )

class OrderBase(models.Model):
    """
    THe order of a transaction
    """
    # the placing time of the order
    order_time = models.TimeField(auto_now_add=True)
    #the expected time the food expected
    expected_time = models.CharField(max_length=25, choices=SERVICE_TYPE)
    order_by_one = models.ForeignKey(UserRecord)
    cousine = models.ForeignKey(CousineBase)
    order_state = models.CharField(max_length=25, choices=ORDER_STATE)

    def __str__(self):
        return self.order_serial_no


class NewOrderRecord(models.Model):
    """
    THe order of a transaction
    """
    from time import strftime, gmtime
    date1 = strftime("%Y-%m-%d",gmtime())
    # the placing time of the order
    date = models.CharField(default=date1, max_length=20)
    order_time = models.TimeField(auto_now_add=True)
    order_serial_no = models.CharField(max_length=25)
    #the expected time the food expected
    expected_time = models.CharField(max_length=25, choices=SERVICE_TYPE)
    order_by_one = models.ForeignKey(UserRecord)
    cousine = models.ForeignKey(CousineBase)
    quantity = models.IntegerField()
    order_state = models.CharField(max_length=25, choices=ORDER_STATE)
    score = models.IntegerField(default=0, help_text="Please give a score in [1,10]")

    def __str__(self):
        return self.order_serial_no
    
    
