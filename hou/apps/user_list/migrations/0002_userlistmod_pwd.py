# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-04 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlistmod',
            name='pwd',
            field=models.CharField(default='', max_length=255),
        ),
    ]
