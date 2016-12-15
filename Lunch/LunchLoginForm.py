
from django import forms
from models import CousineBase

class LoginForm(forms.Form):
    user_name = forms.CharField(label="User Name")
    #message = forms.CharField(widget=forms.Textarea)
    passwd = forms.CharField(widget=forms.PasswordInput, label="Password")


class CousineRegForm(forms.ModelForm):
    class Meta:
        model = CousineBase
        fields = ('cousine_name','restaurant_name','cousine_price', 'service_time', 'picture')

"""
class CousineRegForm(forms.Form):
    '''
    register the cousine
    '''
    cousine_name = forms.CharField(label="Cousine name")
    cousine_restaurant = forms.CharField(label="Restaurant name")
    cousine_price = forms.CharField(label="Price")
    service_time = forms.CharField(label="Service time")
    cousine_image = forms.ImageField(required=False)

"""


