#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
    title = models.CharField('标题', max_length=256)
    content =models.TextField('内容')
    date = models.DateTimeField('日期', editable=True, auto_now_add=True)

    def __unicode__(self):
        return self.title
    
		