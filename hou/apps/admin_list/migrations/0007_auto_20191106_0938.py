# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-06 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_list', '0006_auto_20191105_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminimagemod',
            name='admin_name',
        ),
        migrations.AlterField(
            model_name='adminlistmod',
            name='admin_avator',
            field=models.CharField(max_length=255),
        ),
    ]
