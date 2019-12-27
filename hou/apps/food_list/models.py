# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 食品列表
class FoodListMod ( models.Model ):
    fid = models.CharField(max_length=255, verbose_name='商品id')
    bid = models.CharField(max_length=255, verbose_name='店铺id')
    food_name = models.CharField(max_length=255, verbose_name='商品名称')
    food_activity = models.CharField(max_length=255, verbose_name='商品活动')
    food_introduction = models.CharField(max_length=255, verbose_name='商品介绍')
    food_class = models.CharField(max_length=255, verbose_name='商品分类')
    food_class_detail = models.CharField(max_length=255, verbose_name='商品分类详情')
    food_characteristic = models.CharField(max_length=255, verbose_name='商品特征',default="")
    food_other = models.CharField(max_length=255, verbose_name='商品规格')
    food_avator = models.CharField(max_length=255, verbose_name='商品头像')

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.food_name

class FoodImageMod ( models.Model ):
    fid = models.CharField(max_length=255, verbose_name='商品id',default="")
    file = models.FileField(upload_to='media/food', verbose_name='商品图片')

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.fid