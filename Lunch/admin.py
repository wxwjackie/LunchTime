from django.contrib import admin
from .models import CousineBase, RestaurantBase, StaffBase, GroupBase, OrderBase
# Register your models here.

def register_all():
    """
    Register all the models
    """
    admin.site.register(CousineBase)
    admin.site.register(RestaurantBase)
    admin.site.register(StaffBase)
    admin.site.register(GroupBase)
    admin.site.register(OrderBase)

register_all()