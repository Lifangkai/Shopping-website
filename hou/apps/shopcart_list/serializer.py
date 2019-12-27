# -*- coding: utf-8 -*-
from rest_framework import serializers

class ShopCartSerializer (serializers.Serializer):
    uid = serializers.CharField()
    fid = serializers.CharField()
    bid = serializers.CharField()
    food_avator = serializers.CharField()
    food_name= serializers.CharField()
    food_introduction = serializers.CharField()
    food_price = serializers.DecimalField(max_digits=10, decimal_places=1)
    food_number = serializers.IntegerField()

# class AliPayOrderSerializer (serializers.Serializer):
#     out_trade_no = serializers.CharField()
#     total_amount = serializers.CharField()
#     subject = serializers.CharField()
#     buyer_id = serializers.CharField()
#     modelBody = serializers.CharField()