"""Food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Lunch import views
from register import views as register_views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^adminlogin/', views.admin_login, name='admin_login'),
    url(r'^lunch/', views.home_page, name='homepage'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^register/', register_views.index, name='register'),
    url(r'^registersuccess/', register_views.register_success, name='register_success'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^adminlogout/', views.admin_logout, name='admin_logout'),
    url(r'^checkout/', views.checkout, name='checkout'),
    url(r'^checkoutsuccess/', views.checkout_success, name='checkout_success'),
    url(r'^checkoutfail/', views.checkout_fail, name='checkout_fail'),
    url(r'^personal/', views.personal_info, name='personal_info'),
    url(r'^administrator/', views.administrator_info, name='administrator_info'),
    url(r'^summary/', views.summary, name='summary'),
    url(r'^orderstatechange/', views.order_state_change, name='order_state_change'),
    url(r'^notifyuser/', views.notify_user, name='notify_user'),
    url(r'^adminadd/', views.admin_add, name='admin_add'),
    url(r'^adminaddnext/', views.admin_add_next, name='admin_add_next'),
    url(r'^scorechange/', views.personal_change_score, name="personal_change_score"),
    url(r'^recommend_newdishes/', views.admin_recommend_newdishes, name='admin_recommend_newdishes'),
    url(r'^recommend_popular/', views.admin_recommend_popular, name='admin_recommend_popular'),
    url(r'^recommend_specialoffer/', views.admin_recommend_specialoffer, name='admin_recommend_specialoffer'),
]
