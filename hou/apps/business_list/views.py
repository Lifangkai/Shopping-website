# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.views import APIView

from code_file import ERRORCODE
from code_file import ERRORMSG
from .models import BussinessListMod
from .models import BusinessImageMod
from food_list.models import FoodListMod
from .serializer import BusinessSerializer
from rest_framework_extensions.cache.decorators import (
    cache_response
)
from util_con import db


# Create your views here.
class BussinessQueryView(APIView):
    """
    查询商家店铺信息
    """
    def get(self, request):
        try:
            sid = request.session.get("store_id", "")
            BusData = BussinessListMod.objects.filter(sid=sid)
            ret = BusinessSerializer(BusData,many=True)
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

class BussQueryOneView(APIView):
    """
    查询单个店铺信息
    """
    def post(self, request):
        try:
            bid = request.data.get("bid","")
            BussData = BussinessListMod.objects.filter(bid=bid)
            ret = BusinessSerializer(BussData,many=True)
            res = {
                "code": ERRORCODE.SUCCESS,
                "data":ret.data
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class BussinessEditView(APIView):
    """
    修改店铺信息
    """
    def post(self, request):
        try:
            sid = request.session.get("store_id", "")
            bid = request.data.get("bid","")
            data = request.data
            businessCount = BussinessListMod.objects.filter(sid=sid,bid=bid).count()
            # 判断商家是否存在店铺
            if businessCount != 0:
                obj = BussinessListMod.objects.get(sid=sid)
                obj.bus_name = data.get("bus_name", "")
                obj.bus_address = data.get("bus_address", "")
                obj.bus_introduction = data.get("bus_introduction", "")
                obj.bus_phone = data.get("bus_phone", "")
                obj.bus_class = data.get("bus_class", "")
                obj.bus_avator = data.get("bus_avator", "")
                obj.save()
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "msg": ERRORMSG.SUCCESS
                }
            else:
                res = {
                    "code": ERRORCODE.ERROR_MODIFY,
                    "msg": ERRORMSG.ERROR_MODIFY
                }
        except:
                res = {
                    "code": ERRORCODE.ERROR_WEBSERVER,
                    "msg": ERRORMSG.ERROR_WEBSERVER
                }
        return Response(res)

class BussinessDelView(APIView):
    """
    删除店铺信息
    """
    def post(self, request):
        try:
            bid = request.data.get("bid", "")
            # 删除店铺
            BussinessListMod.objects.filter(bid=bid).delete()
            BusinessImageMod.objects.filter(bid=bid).delete()
            # 判断店铺是否含有商品
            foodinfocount = FoodListMod.objects.filter(bid=bid).count()
            if foodinfocount != 0:
                # 删除店铺商品
                cursor = db.cursor()
                cursor.execute("SELECT * FROM food_list_foodlistmod WHERE bid='{}'".format(bid))
                foodinfo = cursor.fetchall()
                for i in foodinfo:
                    # print "DELETE FROM food_list_foodimagemod WHERE fid='{}'".format(i.get("fid",""))
                    cursor.execute("DELETE FROM food_list_foodimagemod WHERE fid='{}'".format(i.get("fid","")))
                    cursor.execute("DELETE FROM food_list_foodlistmod WHERE fid='{}'".format(i.get("fid","")))
                    # db.commit()
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

class BussinessAddView(APIView):
    """
    创建店铺
    """
    def post(self, request):
        try:
            sid = request.session.get("store_id", "")
            data = request.data
            businessCount = BussinessListMod.objects.filter(sid=sid).count()
            if businessCount == 0:
                BussinessListMod.objects.create(**data)
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "msg": ERRORMSG.SUCCESS
                }
            else:
                res = {
                    "code": ERRORCODE.ERROR_ADD,
                    "msg": ERRORMSG.ERROR_ADD
                }
        except:
                res = {
                    "code": ERRORCODE.ERROR_WEBSERVER,
                    "msg": ERRORMSG.ERROR_WEBSERVER
                }
        return Response(res)

class BussinessImageView(APIView):
    """
    上传店铺图片
    """
    def post(self, request):
        try:
            bid = request.data.get("bid", "")
            file = request.FILES.get("file","")
            BusinessImageMod.objects.create(bid=bid,file=file)
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

class BussinessPermitView(APIView):
    """
    上传营业执照
    """
    def post(self, request):
        try:
            bid = request.data.get("bid", "")
            file = request.FILES.get("file","")
            BusinessImageMod.objects.create(bid=bid,file=file)
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

class BussinessCaterView(APIView):
    """
    上传服务许可证
    """
    def post(self, request):
        try:
            bid = request.data.get("bid", "")
            file = request.FILES.get("file","")
            BusinessImageMod.objects.create(bid=bid,file=file)
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