#coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rukz_product_list, name='rukz_product_list'),
    url(r'^(?P<id>\d+)/$', views.rukz_product_detail, name='rukz_product_detail'),
]

#from documentation url(r'^$', views.index, name='index'),
''' 
#coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]
'''