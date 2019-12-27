# -*- coding: utf-8 -*-
from rest_framework import serializers

class OrderListSerializer (serializers.Serializer):
    oid = serializers.CharField()
    bid = serializers.CharField()
    uid = serializers.CharField()
    order_name = serializers.CharField()
    order_allprice = serializers.CharField()
    order_status = serializers.CharField()