from django import forms

class RegisterForm(forms.Form):
    '''
    A form to create the user
    '''
    user_name = forms.CharField(max_length=50)
    passwd = forms.CharField(widget=forms.PasswordInput,)
    confirm_passwd = forms.CharField(widget=forms.PasswordInput,)