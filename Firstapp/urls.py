# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from Firstapp import views

app_name='Firstapp'

urlpatterns=[
    # url(r'^$',views.login,name='login'),
    url(r'^$',views.test, name='test')
]