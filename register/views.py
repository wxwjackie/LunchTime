from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .RegisterForm import RegisterForm
from .models import UserRecord
from django.template import RequestContext
# Create your views here.

def index(request):
    '''
    to show the register forms
    '''
    
    if request.method == 'POST':
        '''
        If the method is POST
        '''
        #bind the form
        form = RegisterForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                return HttpResponse('The passwords are inconsistent!')

            input_user_name = form.cleaned_data['user_name']
            input_password = form.cleaned_data['password']
            input_email = form.cleaned_data['email']
            print input_user_name
            print input_password
            print input_email

            is_exist = UserRecord.objects.filter(user_name__exact=input_user_name)
            if is_exist:
                '''
                The user name is existing
                '''
                return HttpResponse("User Name existed. Please change to another.")

            UserRecord.objects.create(user_name=input_user_name,
                                      passwd=input_password,
                                      email=input_email)
            return HttpResponseRedirect('/registersuccess/')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})
    return render_to_response('regist.html',{'form': form}, context=RequestContext(request))

def register_success(request):
    return render(request, 'register_success.html')