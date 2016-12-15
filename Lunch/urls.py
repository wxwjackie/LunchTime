from django.conf.urls import url
from . import views

app_name = 'Lunch'
urlpatterns = [
    url(r'^$', views.index),
]