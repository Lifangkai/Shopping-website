# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ShopCartListMod ( models.Model ):
    uid = models.CharField(max_length=255, verbose_name='用户id')
    fid = models.CharField(max_length=255, verbose_name='商品id')
    bid = models.CharField(max_length=255, verbose_name='店铺id',default="")
    food_avator = models.CharField(max_length=255, verbose_name='商品头像')
    food_name = models.CharField(max_length=255, verbose_name='商品名称')
    food_introduction = models.CharField(max_length=255, verbose_name='商品介绍')
    food_price = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='商品价格')
    food_number = models.IntegerField(max_length=255, verbose_name='商品数量')

    class Meta:
        verbose_name = '购物车信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.food_name

# class AliPayOrderListMod ( models.Model ):
#     out_trade_no = models.CharField(max_length=255, verbose_name='订单id')
#     total_amount = models.CharField(max_length=255, verbose_name='订单金额')
#     subject = models.CharField(max_length=255, verbose_name='订单名称')
#     buyer_id = models.CharField(max_length=255, verbose_name='买家id')
#     modelBody = models.CharField(max_length=10000, verbose_name='商品列表')
#
#     class Meta:
#         verbose_name = "支付宝订单"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.subject