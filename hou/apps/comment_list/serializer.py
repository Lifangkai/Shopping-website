# -*- coding: utf-8 -*-
from rest_framework import serializers

class BussCommitSerializer(serializers.Serializer):
    # 要定义需要序列化的字段，注意：这里定义的字段的值必须和serializers.py中的字段保持一致
    bid = serializers.CharField()
    bus_score = serializers.DecimalField(max_digits =2,decimal_places=1)
    bus_sell = serializers.IntegerField()

class FoodCommentSerializer(serializers.Serializer):
    # 要定义需要序列化的字段，注意：这里定义的字段的值必须和serializers.py中的字段保持一致
    fid = serializers.CharField()
    food_score = serializers.DecimalField(max_digits =2,decimal_places=1)
    food_sell = serializers.IntegerField()