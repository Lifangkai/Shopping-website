# -*- coding: utf-8 -*-
from rest_framework import serializers

class UsersSerializer(serializers.Serializer):
    # 要定义需要序列化的字段，注意：这里定义的字段的值必须和models.py中的字段保持一致
    uid = serializers.CharField()
    user_time = serializers.CharField()
    user_name = serializers.CharField()
    user_pwd = serializers.CharField()
    user_address = serializers.CharField()

class UserWarnSerializer(serializers.Serializer):
    uid = serializers.CharField()
    user_content = serializers.CharField()