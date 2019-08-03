from django.urls import path, re_path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    re_path(r'^login/$', authapp.index, name='index'),

]