# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 订单列表
class OrderListMod ( models.Model ):
    oid = models.CharField(max_length=255, verbose_name='订单id')
    uid = models.CharField(max_length=255, verbose_name='用户id',default="")
    bid = models.CharField(max_length=255, verbose_name='店铺id')
    order_name = models.CharField(max_length=255, verbose_name='订单名称')
    order_allprice = models.CharField(max_length=255, verbose_name='订单总价')
    order_status = models.CharField(max_length=255, verbose_name='订单状态')

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_name
