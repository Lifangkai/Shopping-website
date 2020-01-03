# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView

from code_file import ERRORCODE
from code_file import ERRORMSG
from .models import BussCommentListMod
from .models import FoodCommentListMod
from .serializer import BussCommitSerializer
from .serializer import FoodCommentSerializer
from util_con import db
from comm_func import deleteDuplicate
from rest_framework_extensions.cache.decorators import (
    cache_response
)

# Create your views here.
class BussCommQueryView(APIView):
    """
    查询商家评分，销量等信息
    """
    def post(self, request):
        try:
            bid = request.data.get("bid","")
            BussData = BussCommentListMod.objects.filter(bid=bid)
            ret = BussCommitSerializer(BussData, many=True)
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

class BussCommAddView(APIView):
    """
    添加商家评分，销量等信息
    """
    def post(self, request):
        try:
            bid = request.data.get("bid","")
            bus_score = 0.0
            bus_sell = 0
            dic = {
                "bid":bid,
                "bus_score":bus_score,
                "bus_sell":bus_sell,
            }
            BussCommentListMod.objects.create(**dic)
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

class FoodCommQueryView(APIView):
    """
    查询食品评分，销量等信息
    """
    def post(self, request):
        try:
            fid = request.data.get("fid","")
            FoodData = FoodCommentListMod.objects.filter(fid=fid)
            ret = FoodCommentSerializer(FoodData, many=True)
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

class FoodCommAddView(APIView):
    """
    添加食品评分，销量等信息
    """
    def post(self, request):
        try:
            fid = request.data.get("fid","")
            food_score = 0.0
            food_sell = 0
            dic = {
                "fid":fid,
                "food_score":food_score,
                "food_sell":food_sell,
            }
            FoodCommentListMod.objects.create(**dic)
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

class FoodLikeView(APIView):
    """
    根据买过的店铺推荐
    """
    def get(self, request):
        try:
            uid = request.session.get("user_id","")
            cursor = db.cursor()
            cursor.execute("SELECT bid FROM order_list_orderlistmod WHERE uid='{}'".format(uid))
            orderinfo = cursor.fetchall()
            orderinfo = list(orderinfo)
            orderinfo = deleteDuplicate(orderinfo)
            datalist = []
            for i in orderinfo:
                cursor.execute("SELECT * FROM food_list_foodlistmod WHERE bid='{}'".format(i.get("bid","")))
                data = cursor.fetchone()
                datalist.append(data)
            res = {
                "code": ERRORCODE.SUCCESS,
                "data": datalist
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)