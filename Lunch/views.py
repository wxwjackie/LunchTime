from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .LunchLoginForm import LoginForm
from register.models import UserRecord
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from .models import CousineBase, RestaurantBase
from django.forms import formset_factory
from .DishForm import DishForm

@csrf_protect
def login(request):
    if request.method == "POST":
        #binding form with data
        form = LoginForm(request.POST)
        
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            passwd = form.cleaned_data['passwd']
            print user_name, passwd
            
            #query the user name and passwd
            if UserRecord.objects.filter(user_name__exact=user_name,  
                                         passwd__exact=passwd):
                #now the login succeed
                #return HttpResponse("Login Successfully!")
                request.session['username'] = user_name
                return HttpResponseRedirect('/Lunch/')
                #return render(request, 'index.html', {'user_login': True, 'user_name':user_name})
            else:
                #still in this page
                #return render(request, 'index.html', {'form':form, 'password_is_wrong': True})
                return render_to_response('login.html', {'form':form, 'password_is_wrong': True}, \
                                          RequestContext(request))
    else:
        #this is get
        form = LoginForm()
        print "GET"
        return render(request, 'login.html',{'form':form})

def logout(request):
    """
    logout
    """
    del request.session['username']
    return HttpResponseRedirect('/Lunch/')


def home_page(request):
    '''
    load the home page
    '''
    manu_list = CousineBase.objects.all()
    
    user_name = request.session.get('username')
    '''
    order_form_set = formset_factory(DishForm)
    
    formset = order_form_set()
    
    if request.method == "POST":
        formset = order_form_set(request.POST)
        print "receive post"
        print formset
    #here, we need to get all the cousine data and pass them into the view
    '''
    if user_name:
        return render(request, 'index.html', {'user_login': True, 'user_name': user_name, 'manu_list':manu_list})
    else:
        return render(request, 'index.html', {'manu_list':manu_list})
        

def checkout(request):
    '''
    now checkout
    '''
    if request.method == "GET":
        print request.GET
    user_name = request.session.get('username')
    
    if user_name:
        return HttpResponse("Checkout!")
    else:
        return HttpResponseRedirect('/login/')