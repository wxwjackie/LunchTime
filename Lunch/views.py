from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .LunchLoginForm import LoginForm, CousineRegForm
from register.models import UserRecord, AdminUserRecord
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from .models import CousineBase, RestaurantBase, NewOrderRecord
from Recommend.MostFreqRecommender import MostFreqRecommender
import OrderUtils
import EmailUtils
import Recommend.RecommendUtils as RecommendUtils
import json
from AdminUtils import create_new_cousine


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
                return HttpResponseRedirect('/lunch/')
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
    return HttpResponseRedirect('/lunch/')


def home_page(request):
    '''
    load the home page
    '''
    manu_list = []
    #CousineBase.objects.all()

    user_name = request.session.get('username')

    if user_name:
        personal_list = MostFreqRecommender(user_name=user_name).recommend()
        manu_list = []
        if not personal_list:
            manu_list = CousineBase.objects.all()
        else:
            manu_list = OrderUtils.get_cousine_by_name(personal_list)

        return render(request, 'index.html', {'user_login': True, 'user_name': user_name, 'manu_list':manu_list})
        #return render(request, 'index.html', {'user_login': True, 'user_name': user_name, 'formset':formset})
    else:
        manu_list = CousineBase.objects.all()
        return render(request, 'index.html', {'manu_list': manu_list})
        #return render(request, "index.html", {'formset': formset})


def checkout(request):
    '''
    now checkout
    '''
    user_name = request.session.get('username')
    
    if user_name:
        if request.method == "GET":
            print request.GET
        else:
            product_list =  request.POST.getlist('product_list[]')
            product_quantity = request.POST.getlist('quantity_list[]')
            
            product_list = OrderUtils.idenfity_product_id(product_list)
            response_data={}
            if OrderUtils.generate_order(user_name, product_list, product_quantity):
                response_data['result'] = True
            else:
                response_data['result'] = False

            return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponseRedirect('/login/')


def checkout_success(request):
    '''
    '''
    user_name = request.session.get('username')
    if user_name:
        return render(request, 'checkoutsuccess.html', {'user_login': True, 'user_name': user_name})
    else:
        return HttpResponseRedirect('/login/')


def checkout_fail(request):
    '''
    '''
    user_name = request.session.get('username')
    product_zero = False;
    if request.GET.has_key('product_num'):
        product_zero = True;
      
    if user_name:
        return render(request, 'checkoutfail.html', {'user_login': True, 'user_name': user_name, 'product_zero': product_zero})
    else:
        return HttpResponseRedirect('/login/')

    
def personal_info(request):
    '''
    display the personal information
    '''
    user_name = request.session.get('username')
    #order_raw_list = NewOrderRecord.objects.values('order_serial_no').distinct().order_by('-order_serial_no')
    order_dict =  OrderUtils.get_last_n_order(1, user_name)
    history_order_dict = OrderUtils.get_last_n_order(5, user_name)

    #order_list = []
    '''
    for order in order_raw_list:
        order_list.append(order)
    '''
    
    if user_name:
        return render(request, 'personal.html', {'user_login': True,
                                                 'user_name': user_name,
                                                 'order_dict': order_dict,
                                                 'history_order': history_order_dict})
    else:
        return HttpResponseRedirect('/login/')
        #return render(request, 'personal.html', {'user_login': True, 'user_name': user_name, 'order_list': order_list})


def summary(request):
    '''
    Summary
    '''
    
    user_name = request.session.get('username')
    
    #order_raw_list = NewOrderRecord.objects.values('order_serial_no').distinct().order_by('-order_serial_no')
    if user_name:
        order_dict =  OrderUtils.get_today_order()
        history_order_dict = OrderUtils.get_last_n_order(5)
        param_dict = {'user_login': True,
                     'user_name': user_name,
                     'order_dict': order_dict,
                     'history_order': history_order_dict}
        
        EmailUtils.notify_admin("zhaoyin_thu@126.com", param_dict)
        return render(request, 'summary.html', param_dict)
        
    else:
        return HttpResponseRedirect('/login/')


@csrf_protect
def admin_login(request):
    '''
    Login entry for administrator
    '''
    if request.method == "POST":
        # binding form with data
        form = LoginForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            passwd = form.cleaned_data['passwd']
            print user_name, passwd

            # query the user name and passwd
            if AdminUserRecord.objects.filter(admin_username__exact=user_name, admin_passwd__exact=passwd):
                print "Login OK"
                request.session['admin_username'] = user_name
                return HttpResponseRedirect('/administrator/')
            else:
                # still in this page
                print "Login failed"
                return render(request, 'adminlogin.html', {'form':form, 'password_is_wrong': True})
                # return render_to_response('adminlogin.html', {'form':form, 'password_is_wrong': True}, RequestContext(request))
    else:
        form = LoginForm()
        print "GET"
        return render(request, 'adminlogin.html', {'form':form})


def admin_logout(request):
    """
    logout
    """
    print "admin logout"
    del request.session['admin_username']
    return HttpResponseRedirect('/lunch/')


def administrator_info(request):
    '''
    Administrator page with more rights
    '''
    user_name = request.session.get('admin_username')
    order_dict =  OrderUtils.get_today_order()

    if user_name:
        return render(request,
                      'administrator.html',
                      {'user_login': True,
                       'user_name': user_name,
                       'order_dict': order_dict})
    else:
        return HttpResponseRedirect('/adminlogin/')


def order_state_change(request):
    """
    Change the order state according to the request
    """
    new_state = None
    order_id = None

    if request.method == "POST":
        if 'order_state' in request.POST:
            new_state = request.POST['order_state']
        if 'order_id' in request.POST:
            order_id = request.POST['order_id']

        print "Changing the order state to [%s] for order [%s]" % (new_state, order_id)

        if order_id and new_state:
            OrderUtils.change_order_state(order_id, new_state)

    return HttpResponseRedirect('/administrator/')


def notify_user(request):
    """
    Notify the user
    """
    order_id = None
    email = None

    if request.method == "POST":
        if 'order_id' in request.POST:
            order_id = request.POST['order_id']
        if 'email' in request.POST:
            email = request.POST['email']

        if not order_id or not email:
            return

        order = NewOrderRecord.objects.get(order_serial_no=order_id)
        state = order.order_state
        user = order.order_by_one
        print "Notifying the user [%s]; order state is [%s]" % (email, state)

        EmailUtils.notify_order_state_to_user(email, user, state)

    return HttpResponseRedirect('/administrator/')


def admin_add(request):
    """
    Add cousine by admin
    """

    if request.method == "POST":
        print request.FILES
        if 'cousine_image' in request.FILES:
            image = request.FILES["cousine_image"]
        else:
            image = None

        form = CousineRegForm(request.POST)
        if form.is_valid():
            cousine_name = form.cleaned_data['cousine_name']
            cousine_restaurant = form.cleaned_data['cousine_restaurant']
            cousine_price = form.cleaned_data['cousine_price']
            service_time = form.cleaned_data['service_time']
            create_new_cousine(cousine_name=cousine_name,
                               cousine_restaurant=cousine_restaurant,
                               cousine_price=cousine_price,
                               cousine_image=image,
                               service_time=service_time)

        else:
            raise Exception


        # create the obj
        return HttpResponseRedirect('/registersuccess/')


    else:
        form = CousineRegForm()
        print "GET"
        return render(request, 'adminadd.html', {'form':form})



def admin_change(request):
    """
    Modify cousine by admin
    """

