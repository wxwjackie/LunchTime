'''
Created on 

@author: Jerry
'''
from django import forms

class DishForm(forms.Form):
    dish_name = forms.CharField(label="Dish Name")
    dish_restaurant = forms.CharField(label="Restaurant")
    dish_quantity = forms.IntegerField(label="Quantity")
    dish_description = forms.CharField(label="Description")
    #message = forms.CharField(widget=forms.Textarea)
    #passwd = forms.CharField(widget=forms.PasswordInput, label="Password")

