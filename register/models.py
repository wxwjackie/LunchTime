from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserRecord(models.Model):
    '''
    A class that records the user and the registered password
    '''
    user_name = models.CharField(max_length=50)
    passwd = models.TextField()
    
    