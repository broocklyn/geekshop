from django.urls import path, re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.index, name='index'),
    re_path(r'^products/$', mainapp.products, name='products'),
    # path('category/<int:pk>/', mainapp.category, name='category'),
    re_path(r'^category/(?P<pk>\d+)$', mainapp.category, name='category'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.category, name='category_paginator'),
    re_path(r'^product/(?P<pk>\d+)$', mainapp.product, name='product'),
    re_path(r'^contact/$', mainapp.contact, name='contact')
]
