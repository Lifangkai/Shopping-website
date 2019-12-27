# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StoreListMod ( models.Model ):
    sid = models.CharField(max_length=255, verbose_name='商家id')
    bid = models.CharField(max_length=255, verbose_name='店铺id')
    store_time= models.CharField(max_length=255, verbose_name='商家注册时间')
    store_name = models.CharField(max_length=255, verbose_name='商品名称')
    store_pwd = models.CharField(max_length=255, verbose_name='商品密码',default="")
    store_address = models.CharField(max_length=255, verbose_name='商品地址')

    class Meta:
        verbose_name = '商家信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.store_name

class StoreWarnMod ( models.Model ):
    sid = models.CharField(max_length=255, verbose_name='商家id')
    store_content = models.CharField(max_length=255, verbose_name='商家预警')

    class Meta:
        verbose_name = '商家预警'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sid