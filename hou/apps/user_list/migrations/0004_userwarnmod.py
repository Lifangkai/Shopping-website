# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-08 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0003_auto_20191107_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWarnMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255)),
                ('user_content', models.CharField(max_length=255)),
            ],
        ),
    ]
