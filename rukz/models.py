#coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

class Rukzak(models.Model):
	# fields: Ссылка	Наименование (Артикул - в топку)	Цена, руб.	Изображение	Прочее
	link = models.CharField(max_length=200)
	naim = models.CharField(max_length=200, db_index=True)
	artikul = models.CharField(max_length=200, db_index=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	img_link = models.CharField(max_length=200)
	other = models.CharField(max_length=200, blank=True)

	class Meta:
		#ordering = ('price',)
		ordering = ('price',)
		#index_together = (('id', 'slug'),)
		
	def __unicode__(self):
		return self.naim

	def get_absolute_url(self):
		return reverse('rukz:product_detail',
						args=[self.id])

'''class Category(models.Model):
	name = models.CharField(max_length=200,
							db_index=True)
	slug = models.SlugField(max_length=200,
							db_index=True,
							unique=True)
	
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category',
						args=[self.slug])
'''

'''
class Product(models.Model):
	category = models.ForeignKey(Category,
								related_name='products')
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d',
							blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)
		
	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail',
						args=[self.id, self.slug])
'''