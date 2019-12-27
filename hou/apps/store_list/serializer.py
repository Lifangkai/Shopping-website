# -*- coding: utf-8 -*-
from rest_framework import serializers

class StoreSerializer(serializers.Serializer):
    # 要定义需要序列化的字段，注意：这里定义的字段的值必须和models.py中的字段保持一致
    sid = serializers.CharField()
    bid = serializers.CharField()
    store_time = serializers.CharField()
    store_name = serializers.CharField()
    store_pwd = serializers.CharField()
    store_address = serializers.CharField()

class StoreWarnSerializer (serializers.Serializer):
    sid = serializers.CharField(max_length=255)
    store_content = serializers.CharField(max_length=255)