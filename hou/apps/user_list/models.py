# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserListMod ( models.Model ):
    uid = models.CharField(max_length=255, verbose_name='用户id')
    user_time= models.CharField(max_length=255, verbose_name='用户注册时间')
    user_name = models.CharField(max_length=255, verbose_name='用户名称')
    user_pwd = models.CharField(max_length=255, verbose_name='用户密码',default="")
    user_address = models.CharField(max_length=255, verbose_name='用户地址')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name

class UserWarnMod ( models.Model ):
    uid = models.CharField(max_length=255, verbose_name='用户id')
    user_content = models.CharField(max_length=255, verbose_name='用户预警')

    class Meta:
        verbose_name = '用户预警'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uid