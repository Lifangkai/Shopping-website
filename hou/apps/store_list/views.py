# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.cache.decorators import (
    cache_response
)
from code_file import ERRORCODE
from code_file import ERRORMSG
from .models import StoreListMod
from .models import StoreWarnMod
from .serializer import StoreSerializer
from .serializer import StoreWarnSerializer
from business_list.models import BussinessListMod,BusinessImageMod
from food_list.models import FoodListMod
from mysql_con import db


# Create your views here.
class StoreQueryView(APIView):
    """
    查询所有商家信息
    """
    def get(self, request):
        try:
            StoreData = StoreListMod.objects.all()
            ret = StoreSerializer(StoreData,many=True)
            res = {
                "code":ERRORCODE.SUCCESS,
                "data":ret.data
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class StoreQueryOneView(APIView):
    """
    查询单个商家信息
    """
    def get(self, request):
        try:
            sid = request.session.get("store_id","")
            print sid
            StoreData =  StoreListMod.objects.filter(sid=sid)
            ret = StoreSerializer(StoreData, many=True)
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

class StoreEditView(APIView):
    """
    修改商家信息
    """
    def post(self, request):
        try:
            sid = request.session.get("store_id", "")
            bid = request.data.get("bid", "")
            storename = request.data.get("store_name","")
            storepwd = request.data.get("store_pwd","")
            storeaddress = request.data.get("store_address","")
            SqlData = StoreListMod.objects.get(sid=sid)
            # 判断是否修改商家名
            if SqlData.store_name == storename:
                SqlData.bid = bid
                SqlData.store_pwd = storepwd
                SqlData.store_address = storeaddress
                SqlData.save()
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "msg": ERRORMSG.SUCCESS
                }
            else:
                # 判断商家名是否存在
                storecount = StoreListMod.objects.filter(store_name=storename).count()
                if storecount == 0:
                    SqlData.store_name = storename
                    SqlData.store_pwd = storepwd
                    SqlData.store_address = storeaddress
                    SqlData.save()
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

class StoreDelView(APIView):
    """
    删除商家信息
    """
    def post(self, request):
        try:
            sid = request.data.get("sid", "")
            bid = request.data.get("bid","")
            StoreListMod.objects.filter(sid=sid).delete()
            # 判断商家有无店铺
            if bid:
                # 删除商家店铺
                BussinessListMod.objects.filter(sid=sid).delete()
                BusinessImageMod.objects.filter(bid=bid).delete()
                # 判断店铺是否含有商品
                foodinfocount = FoodListMod.objects.filter(bid=bid).count()
                if foodinfocount != 0:
                    # 删除商家店铺商品
                    cursor = db.cursor()
                    cursor.execute("SELECT * FROM food_list_foodlistmod WHERE bid='{}'".format(bid))
                    foodinfo = cursor.fetchall()
                    for i in foodinfo:
                        # print "DELETE FROM food_list_foodimagemod WHERE fid='{}'".format(i.get("fid",""))
                        cursor.execute("DELETE FROM food_list_foodimagemod WHERE fid='{}'".format(i.get("fid", "")))
                        cursor.execute("DELETE FROM food_list_foodlistmod WHERE fid='{}'".format(i.get("fid", "")))
                        # db.commit()
            res = {
                "code":ERRORCODE.SUCCESS,
                "msg":ERRORMSG.SUCCESS
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class StoreQueryAddressView(APIView):
    """
    查询商家分布情况
    """
    def post(self, request):
        try:
            address = request.data.get("address","")
            StoreCount = StoreListMod.objects.filter(store_address=address).count()
            # ret = UsersSerializer(UserData,many=True)
            res = {
                "code":ERRORCODE.SUCCESS,
                "data":StoreCount
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class StoreWarnQueryView(APIView):
    """
    查询商家警告信息
    """
    def get(self, request):
        try:
            sid = request.session.get("store_id", "")
            StoreData = StoreWarnMod.objects.filter(sid=sid)
            if StoreData.count() != 0:
                ret = StoreWarnSerializer(StoreData, many=True)
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "data": ret.data
                }
            else:
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "data": []
                }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class StoreWarnAddView(APIView):
    """
    添加商家警告信息
    """
    def post(self, request):
        try:
            sid = request.data.get("sid","")
            store_content = request.data.get("store_content","")
            storeinfo = StoreWarnMod.objects.filter(sid=sid)
            if storeinfo.count() != 0:
                StoreWarnMod.objects.filter(sid=sid).update(store_content=store_content)
            else:
                StoreWarnMod.objects.create(sid=sid,store_content=store_content)
            res = {
                "code":ERRORCODE.SUCCESS,
                "msg":ERRORMSG.SUCCESS
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class StoreWarnDelView(APIView):
    """
    删除商家警告信息
    """
    def post(self, request):
        try:
            sid = request.data.get("sid","")
            StoreWarnMod.objects.filter(sid=sid).delete()
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