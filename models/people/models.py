from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	male = models.BooleanField(default=True)
    
	def __unicode__(self):
		return self.name
		
# Create your models here.
