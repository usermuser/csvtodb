from django.db import models

class Data_csv(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  
  def __unicode__(self):
    return self.name
