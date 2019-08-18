from django.urls import path, re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.index, name='index'),
    re_path(r'^shopuser/create/$', adminapp.shopuser_create, name='shopuser_create'),
    re_path(r'^shopuser/update/(?P<pk>\d+)/$', adminapp.shopuser_update, name='shopuser_update'),
    re_path(r'^shopuser/delete/(?P<pk>\d+)/$', adminapp.shopuser_delete, name='shopuser_delete'),
    re_path(r'^productcategory/list/$', adminapp.productcategory_list, name='productcategory_list'),
    re_path(r'^productcategory/create/$', adminapp.productcategory_create, name='productcategory_create'),
    re_path(r'^productcategory/update/(?P<pk>\d+)/$', adminapp.productcategory_update, name='productcategory_update'),
    re_path(r'^productcategory/delete/(?P<pk>\d+)/$', adminapp.productcategory_delete, name='productcategory_delete'),
    re_path(r'^productcategory/products/(?P<pk>\d+)/$', adminapp.productcategory_products,
            name='productcategory_products'),

    re_path(r'^product/create/(?P<pk>\d+)/$', adminapp.product_create, name='product_create'),
    re_path(r'^product/update/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
    re_path(r'^product/delete/(?P<pk>\d+)/$', adminapp.product_delete, name='product_delete'),
]
