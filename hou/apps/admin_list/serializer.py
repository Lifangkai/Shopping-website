# -*- coding: utf-8 -*-
from rest_framework import serializers

class AdminListSerializer (serializers.Serializer):
    aid = serializers.CharField()
    admin_name = serializers.CharField()
    admin_pwd = serializers.CharField()
    admin_registertime = serializers.CharField()
    admin_address = serializers.CharField()
    admin_authority = serializers.IntegerField()
    admin_avator = serializers.CharField()