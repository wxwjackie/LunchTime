
from django import forms
from models import CousineBase, RestaurantBase
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
    user_name = forms.CharField(label="User Name")
    #message = forms.CharField(widget=forms.Textarea)
    passwd = forms.CharField(widget=forms.PasswordInput, label="Password")


class CousineRegForm(forms.ModelForm):
    class Meta:
        model = CousineBase
        fields = ['cousine_name','restaurant_name','cousine_price', 'service_time', 'picture']
        labels = {'cousine_name': _('Cuisine Name'),
                  'restaurant_name': _('Restaurant Name'),
                  'cousine_price': _('Cuisine Price'),
                  'service_time': _('Service Time'),
                  'picture': _('Picture'),
        }


class RestaurantRegForm(forms.ModelForm):
    class Meta:
        model = RestaurantBase
        fields = ('name','address','phone', 'type')
        labels = {'name': _('Restaurant Name'),
                  'address': _('Restaurant Address'),
                  'phone': _('Restaurant Phone'),
                  'type': _('Restaurant Type'),
        }

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