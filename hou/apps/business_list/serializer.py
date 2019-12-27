# -*- coding: utf-8 -*-
from rest_framework import serializers

class BusinessSerializer(serializers.Serializer):
    # 要定义需要序列化的字段，注意：这里定义的字段的值必须和serializers.py中的字段保持一致
    bid = serializers.CharField()
    sid = serializers.CharField()
    bus_name = serializers.CharField()
    bus_address = serializers.CharField()
    bus_phone = serializers.CharField()
    bus_introduction = serializers.CharField()
    bus_class = serializers.CharField()
    bus_characteristic = serializers.CharField()
    bus_delivery = serializers.CharField()
    bus_start_delivery = serializers.CharField()
    bus_start_time = serializers.CharField()
    bus_end_time = serializers.CharField()
    bus_avator = serializers.CharField()
    bus_permit = serializers.CharField()
    bus_cater = serializers.CharField()
    bus_discount = serializers.CharField()