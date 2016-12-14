from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserRecord(models.Model):
    '''
    A class that records the user and the registered password
    '''
    user_name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="None")

    def __str__(self):
        return self.user_name

class AdminUserRecord(models.Model):
    '''
    Record the admin user info
    '''
    admin_username = models.CharField(max_length=50)
    admin_passwd = models.CharField(max_length=50)
    admin_email = models.CharField(max_length=50)

    def __str__(self):
        return self.admin_username
