# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-12-12 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcartlistmod',
            name='bid',
            field=models.CharField(default='', max_length=255, verbose_name='\u5e97\u94faid'),
        ),
    ]
