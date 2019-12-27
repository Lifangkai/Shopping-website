# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 商家评分销量列表
class BussCommentListMod ( models.Model ):
    bid = models.CharField(max_length=255, verbose_name='店铺id')
    bus_score = models.DecimalField(max_digits =2,decimal_places=1, verbose_name='店铺评分')
    bus_sell = models.IntegerField(max_length=255, verbose_name='店铺销量')


    class Meta:
        verbose_name = '店铺其他信息'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.bid

# 食品评分销量列表
class FoodCommentListMod ( models.Model ):
    fid = models.CharField(max_length=255, verbose_name='商品id')
    food_score = models.DecimalField(max_digits=2,decimal_places=1,verbose_name='商品评分')
    food_sell = models.IntegerField(max_length=255, verbose_name='商品销量')

    class Meta:
        verbose_name = '食品其他信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.bid