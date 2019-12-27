# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 订单列表
class AdminListMod ( models.Model ):
    aid = models.CharField(max_length=255, verbose_name='管理员id')
    admin_name = models.CharField(max_length=255, verbose_name='管理员名称')
    admin_pwd = models.CharField(max_length=255, verbose_name='管理员密码',default="")
    admin_registertime = models.CharField(max_length=255, verbose_name='管理员注册时间')
    admin_address = models.CharField(max_length=255, verbose_name='管理员地址')
    admin_authority = models.IntegerField(max_length=255, verbose_name='管理员权限')
    admin_avator = models.CharField(max_length=255, verbose_name='管理员头像')

    class Meta:
        verbose_name = '管理员信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.admin_name

class AdminImageMod ( models.Model ):
    aid = models.CharField(max_length=255, verbose_name='管理员id',default="")
    file = models.FileField(upload_to='media/admin', verbose_name='管理员头像')

    class Meta:
        verbose_name = '管理员图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.aid