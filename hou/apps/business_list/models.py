# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BussinessListMod ( models.Model ):
    bid = models.CharField(max_length=255, verbose_name='店铺id')
    sid = models.CharField(max_length=255, verbose_name='商家id', default="")
    bus_name= models.CharField(max_length=255, verbose_name='店铺名称')
    bus_address = models.CharField(max_length=255, verbose_name='店铺地址')
    bus_phone = models.CharField(max_length=255, verbose_name='店铺电话')
    bus_introduction = models.CharField(max_length=255, verbose_name='店铺介绍')
    bus_slogan = models.CharField(max_length=255, verbose_name='店铺标语')
    bus_class = models.CharField(max_length=255, verbose_name='店铺分类')
    bus_characteristic = models.CharField(max_length=255, verbose_name='店铺特征')
    bus_delivery = models.CharField(max_length=255, verbose_name='店铺配送')
    bus_start_delivery = models.CharField(max_length=255, verbose_name='店铺配送时间')
    bus_start_time = models.CharField(max_length=255, verbose_name='开店时间')
    bus_end_time = models.CharField(max_length=255, verbose_name='闭店时间')
    bus_avator = models.CharField(max_length=255, verbose_name='店铺头像')
    bus_permit = models.CharField(max_length=255, verbose_name='店铺许可证')
    bus_cater = models.CharField(max_length=255, verbose_name='店铺营业执照')
    bus_discount = models.CharField(max_length=255, verbose_name='店铺活动')

    class Meta:
        verbose_name = '店铺信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.bus_name

class BusinessImageMod ( models.Model ):
    bid = models.CharField(max_length=255, verbose_name='店铺id',default="")
    file = models.ImageField(upload_to='media/bussiness', verbose_name='店铺图片')

    class Meta:
        verbose_name = '店铺图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.bid
