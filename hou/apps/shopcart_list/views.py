# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import json
import copy
from django_redis import get_redis_connection
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from code_file import ERRORCODE
from code_file import ERRORMSG
from comm_func import create_id
from .models import ShopCartListMod
from .serializer import ShopCartSerializer
from order_list.models import OrderListMod
from comment_list.models import BussCommentListMod,FoodCommentListMod
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
# Create your views here.

# 购物车部分
class CartQueryView(APIView):
    """
    搜索购物车信息
    """
    def get(self, request):
        try:
            uid = request.session.get("user_id","")
            CartData = ShopCartListMod.objects.filter(uid=uid)
            ret = ShopCartSerializer(CartData,many=True)
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

class CartAddView(APIView):
    """
    添加购物车信息
    """
    def post(self, request):
        try:
            uid = request.session.get("user_id","")
            fid = request.data.get("fid","")
            data = request.data
            # print data
            cartcount = ShopCartListMod.objects.filter(uid=uid,fid=fid).count()
            if cartcount == 0:
                ShopCartListMod.objects.create(**data)
            else:
                cartinfo = ShopCartListMod.objects.get(uid=uid,fid=fid)
                cartinfo.food_number += 1
                cartinfo.save()
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

class CartDelView(APIView):
    """
    删除购物车信息
    """
    def post(self, request):
        try:
            uid = request.session.get("user_id","")
            fid = request.data.get("fid","")
            ShopCartListMod.objects.filter(uid=uid,fid=fid).delete()
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

class CartEditView(APIView):
    """
    修改购物车信息
    """
    def post(self, request):
        try:
            uid = request.session.get("user_id","")
            fid = request.data.get("fid","")
            data = request.data
            cartinfo = ShopCartListMod.objects.get(uid=uid,fid=fid)
            cartinfo.food_avator = data.get("food_avator", "")
            cartinfo.food_name = data.get("food_name", "")
            cartinfo.food_introduction = data.get("food_introduction", "")
            cartinfo.food_price = data.get("food_price", "")
            cartinfo.food_number = data.get("food_number", "")
            cartinfo.save()
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

# 支付宝部分

# 沙箱环境地址：https://openhome.alipay.com/platform/appDaily.htm?tab=info

# "https://openapi.alipaydev.com/gateway.do", APP_ID, APP_PRIVATE_KEY, "json", CHARSET, ALIPAY_PUBLIC_KEY, "RSA2"

def ali_pay():
    # 为阿里支付实例化一个配置信息对象
    alipay_config = AlipayClientConfig(sandbox_debug=True)
    # 初始化各种配置信息
    # 阿里提供服务的接口
    alipay_config.server_url = "https://openapi.alipaydev.com/gateway.do"
    # 申请的沙箱环境的app_id
    alipay_config.app_id = "2016101600702492"
    # 商户的私钥
    with open("keys/app_private_key.txt") as f:
        alipay_config.app_private_key = f.read()
    # 阿里的公钥
    with open("keys/alipay_public_key.txt") as f:
        alipay_config.alipay_public_key = f.read()
    # 实例化一个支付对象并返回
    alipay_client = DefaultAlipayClient(alipay_client_config=alipay_config)
    return alipay_client

class AliPayView(APIView):
    # 生成支付宝自带页面的API
    def post(self, request):
        out_trade_no = create_id()
        total_amount = str(request.data.get("order_allprice",""))
        subject = request.data.get("order_name","").encode("utf-8")
        buyer_id = request.data.get("uid","").encode("utf-8")
        modelBody = request.data.get("modelBody","")
        # redis存储商品列表
        conn = get_redis_connection()
        conn.set(out_trade_no,json.dumps(modelBody),5 * 60)
        # 得到阿里支付的实例化对象
        client = ali_pay()
        # 为API生成一个模板对象 初始化参数用的
        model = AlipayTradePagePayModel()
        model.out_trade_no = out_trade_no
        model.total_amount = total_amount
        model.subject = subject
        model.buyer_id = buyer_id
        # 商品列表
        goods_list = list()
        for i in modelBody:
            goods = GoodsDetail()
            goods.goods_id = i.get("fid","").encode("utf-8")
            goods.goods_name = i.get("order_name","").encode("utf-8")
            goods.price = str(i.get("order_allprice",""))
            goods.quantity = str(i.get("food_number",""))
            goods_list.append(goods)
        model.goods_detail = goods_list
        # 销售产品码，与支付宝签约的产品码名称
        model.product_code = "FAST_INSTANT_TRADE_PAY"
        # 实例化一个请求对象
        request = AlipayTradePagePayRequest(biz_model=model)
        # get请求 用户支付成功后返回的页面请求地址
        request.return_url = "http://127.0.0.1:8000/shopcartlist/alipay_handler/"
        # post请求 用户支付成功通知商户的请求地址
        request.notify_url = "http://127.0.0.1:8000/shopcartlist/alipay_handler/"
        # 利用阿里支付对象发一个获得页面的请求 参数是request
        response = client.page_execute(request)
        return Response(response)

class PayHandlerView(APIView):
    def get(self, request):
        # return_url的回调地址
        processed_dict = {}
        for key, value in request.GET.items():
            processed_dict[key] = value
        # redis查找商品列表
        conn = get_redis_connection()
        good_list = json.loads(conn.get(processed_dict["out_trade_no"]))
        for i in good_list:
            obj = copy.deepcopy(i)
            food_number =obj.get("food_number","")
            # 店铺食品销量增加
            businessinfo = BussCommentListMod.objects.get(bid=obj.get("bid",""))
            businessinfo.bus_sell += food_number
            businessinfo.save()
            foodinfo = FoodCommentListMod.objects.get(fid=obj.get("fid",""))
            foodinfo.food_sell += food_number
            foodinfo.save()
            # 删除购物车信息
            ShopCartListMod.objects.filter(fid=obj.get("fid", "")).delete()
            del obj["fid"]
            del obj["food_number"]
            OrderListMod.objects.create(**obj)
        response = redirect("http://127.0.0.1:8000/")
        return response

    def post(self, request):
        print(request.data)
        # 用户支付成功 在这里修改订单状态以及优惠券贝里等等情况
        pass