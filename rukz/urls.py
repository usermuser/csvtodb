#coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_product_list, name='all_product_list'), #all bags
    url(r'^chel/$', views.chel_product_list, name='chel_product_list'), #bags in Chelyabinsk
    url(r'^ekat$', views.ekat_product_list, name='ekat_product_list'), #bags in Ekat
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