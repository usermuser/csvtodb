#coding: utf-8
from django.contrib import admin
from .models import Rukzak

class RukzakAdmin(admin.ModelAdmin):
	list_display = ['link', 'naim', 'artikul','price', 'img_link', 'other']
	#list_display = ['naim', 'price']
	#list_filter = ['price']
	#list_filter = ['naim', 'price']
admin.site.register(Rukzak, RukzakAdmin)
'''
#coding: utf-8
from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'stock',
					'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
'''

