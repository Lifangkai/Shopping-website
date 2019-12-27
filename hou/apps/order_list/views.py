# -*- coding: utf-8 -*-
# from rest_framework_extensions.cache.mixins import CacheResponseMixin
from comment_list.models import BussCommentListMod
from comment_list.models import FoodCommentListMod
from rest_framework.response import Response
from rest_framework.views import APIView

from code_file import ERRORCODE
from code_file import ERRORMSG
from .models import OrderListMod
from .serializer import OrderListSerializer


class OrderQueryView(APIView):
    """
    查询订单列表
    """
    def get(self, request):
        try:
            uid = request.query_params.get("uid")
            bid = request.query_params.get("bid")
            if uid is not None and bid is None:
                OrderData = OrderListMod.objects.filter(uid=uid)
                ret = OrderListSerializer(OrderData,many=True)
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "data":ret.data
                }
            elif uid is None and bid is not None:
                OrderData = OrderListMod.objects.filter(bid=bid)
                ret = OrderListSerializer(OrderData, many=True)
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

class OrderDelView(APIView):
    """
    删除订单列表
    """
    def post(self, request):
        try:
            oid = request.data.get("oid","")
            OrderListMod.objects.filter(oid=oid).delete()
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

class OrderEditView(APIView):
    """
    修改订单信息
    """
    def post(self, request):
        try:
            oid = request.data.get("oid","")
            order_allprice = request.data.get("order_allprice","")
            order_status = request.data.get("order_status","")
            OrderListMod.objects.filter(oid=oid).update(order_allprice=order_allprice,
                                                        order_status=order_status)
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

class OrderAddView(APIView):
    """
    添加订单信息
    """
    def post(self, request):
        try:
            oid = request.data.get("oid","")
            bid = request.data.get("bid","")
            fid = request.data.get("fid", "")
            food_number = request.data.get("food_number","")
            uid = request.session.get("user_id","")
            data = request.data
            # 店铺食品销量增加
            businessinfo = BussCommentListMod.objects.get(bid=bid)
            businessinfo.bus_sell += food_number
            businessinfo.save()
            foodinfo = FoodCommentListMod.objects.get(fid=fid)
            foodinfo.food_sell += food_number
            foodinfo.save()
            dic = {"oid":oid,
                   "bid":bid,
                   "uid":uid,
                   "order_name":data.get("order_name",""),
                   "order_allprice":data.get("order_allprice",""),
                   "order_status":data.get("order_status","")}
            OrderListMod.objects.create(**dic)
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