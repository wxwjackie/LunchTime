from django.db import models
from register.models import UserRecord

# Create your models here.
class RestaurantBase(models.Model):
    '''
    Restaurant
    '''
    name = models.CharField(max_length=50);
    address = models.CharField(max_length=1024)
    #the telephone
    phone = models.CharField(max_length=50);
    
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
    restaurant_name = models.CharField(max_length=50)
    #price
    cousine_price = models.CharField(max_length=25)
    #service time
    service_time = models.CharField(max_length=25)
    
    def __str__(self):
        return self.restaurant_name
    
    
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

class OrderRecord(models.Model):
    """
    THe order of a transaction
    """
    # the placing time of the order
    order_time = models.TimeField(auto_now_add=True)
    order_serial_no = models.CharField(max_length=25)
    #the expected time the food expected
    expected_time = models.CharField(max_length=25, choices=SERVICE_TYPE)
    order_by_one = models.ForeignKey(UserRecord)
    cousine = models.ForeignKey(CousineBase)
    order_state = models.CharField(max_length=25, choices=ORDER_STATE)

    def __str__(self):
        return self.order_serial_no
    
    
    
