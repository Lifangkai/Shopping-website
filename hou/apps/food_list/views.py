# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView

from code_file import ERRORCODE
from code_file import ERRORMSG
from .models import FoodImageMod
from .models import FoodListMod
from .serializer import FoodListSerializer


# Create your views here.

class FoodQueryView(APIView):
    """
    搜索店铺对应商品信息
    """
    def get(self, request):
        try:
            bid = request.query_params.get("bid")
            if bid is not None:
                FoodData = FoodListMod.objects.filter(bid=bid)
                ret = FoodListSerializer(FoodData,many=True)
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "data": ret.data
                }
            elif bid is None:
                FoodData = FoodListMod.objects.all()
                ret = FoodListSerializer(FoodData, many=True)
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "data": ret.data
                }
        except:
                res = {
                    "code": ERRORCODE.ERROR_WEBSERVER,
                    "msg": ERRORMSG.ERROR_WEBSERVER
                }
        return Response(res)

class FoodQueryListView(APIView):
    """
    搜索商品信息
    """
    def get(self, request):
        try:
            food_name = request.query_params.get("food_name")
            food_class = request.query_params.get("food_class")
            if food_name is not None and food_class is None:
                FoodData = FoodListMod.objects.filter(food_name=food_name)
                ret = FoodListSerializer(FoodData, many=True)
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "data": ret.data
                }
            elif food_name is None and food_class is not None:
                FoodData = FoodListMod.objects.filter(food_class=food_class)
                ret = FoodListSerializer(FoodData, many=True)
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "data": ret.data
                }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class FoodAddListView(APIView):
    """
    添加商品信息
    """
    def post(self, request):
        try:
            data = request.data
            FoodListMod.objects.create(**data)
            res = {
                "code": ERRORCODE.SUCCESS,
                "msg": ERRORMSG.SUCCESS
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class FoodEditView(APIView):
    """
    编辑商品信息
    """
    def post(self, request):
        try:
            fid = request.data.get("fid","")
            bid = request.data.get("bid","")
            data = request.data
            foodinfo = FoodListMod.objects.get(fid=fid,bid=bid)
            foodinfo.food_name = data.get("food_name","")
            foodinfo.food_introduction = data.get("food_introduction","")
            foodinfo.food_class = data.get("food_class","")
            foodinfo.food_avator = data.get("food_avator","")
            foodinfo.food_other = data.get("food_other","")
            foodinfo.save()
            res = {
                "code": ERRORCODE.SUCCESS,
                "msg": ERRORMSG.SUCCESS
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class FoodDelView(APIView):
    """
    删除商品信息
    """
    def post(self, request):
        try:
            fid = request.data.get("fid","")
            bid = request.data.get("bid","")
            FoodListMod.objects.filter(bid=bid,fid=fid).delete()
            FoodImageMod.objects.filter(fid=fid).delete()
            res = {
                "code": ERRORCODE.SUCCESS,
                "msg": ERRORMSG.SUCCESS
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class FoodImageView(APIView):
    """
    商品图片上传
    """
    def post(self, request):
        try:
            fid = request.data.get("fid","")
            file = request.FILES.get("file","")
            FoodImageMod.objects.create(fid=fid,file=file)
            res = {
                "code": ERRORCODE.SUCCESS,
                "data": file.name
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)