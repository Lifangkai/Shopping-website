# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-04 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bussinesslistmod',
            name='uid',
            field=models.CharField(default='', max_length=255),
        ),
    ]
