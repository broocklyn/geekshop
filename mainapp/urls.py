from django.contrib import admin
from django.urls import path, re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.index, name='index'),
    re_path(r'^products/$', mainapp.products, name='products'),
    re_path(r'^contact/$', mainapp.contact, name='contact'),
]