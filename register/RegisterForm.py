from django import forms

class RegisterForm(forms.Form):
    '''
    A form to create the user
    '''
    user_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput,)
    confirm_password = forms.CharField(widget=forms.PasswordInput,)