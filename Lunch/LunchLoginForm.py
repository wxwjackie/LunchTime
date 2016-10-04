
from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label="User Name")
    #message = forms.CharField(widget=forms.Textarea)
    passwd = forms.CharField(widget=forms.PasswordInput, label="Password")
