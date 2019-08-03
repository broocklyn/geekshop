from django.urls import path, re_path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    re_path(r'^$', authapp.index, name='index'),
    re_path(r'^products/$', authapp.products, name='products'),
    re_path(r'^contact/$', authapp.contact, name='contact')
]