# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-12-11 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCartListMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255, verbose_name='\u7528\u6237id')),
                ('fid', models.CharField(max_length=255, verbose_name='\u5546\u54c1id')),
                ('food_avator', models.CharField(max_length=255, verbose_name='\u5546\u54c1\u5934\u50cf')),
                ('food_name', models.CharField(max_length=255, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('food_introduction', models.CharField(max_length=255, verbose_name='\u5546\u54c1\u4ecb\u7ecd')),
                ('food_price', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='\u5546\u54c1\u4ef7\u683c')),
                ('food_number', models.IntegerField(max_length=255, verbose_name='\u5546\u54c1\u6570\u91cf')),
            ],
            options={
                'verbose_name': '\u8d2d\u7269\u8f66\u4fe1\u606f',
                'verbose_name_plural': '\u8d2d\u7269\u8f66\u4fe1\u606f',
            },
        ),
    ]
