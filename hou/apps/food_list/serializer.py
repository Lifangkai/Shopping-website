# -*- coding: utf-8 -*-
from rest_framework import serializers

class FoodListSerializer (serializers.Serializer):
    fid = serializers.CharField()
    bid = serializers.CharField()
    food_name= serializers.CharField()
    food_activity = serializers.CharField()
    food_introduction = serializers.CharField()
    food_class = serializers.CharField()
    food_class_detail = serializers.CharField()
    food_characteristic = serializers.CharField()
    food_other = serializers.CharField()
    food_avator = serializers.CharField()