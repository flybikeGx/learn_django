# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u65e5\u671f')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
