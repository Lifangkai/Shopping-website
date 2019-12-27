# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.cache.decorators import (
    cache_response
)
from code_file import ERRORCODE
from code_file import ERRORMSG
from .models import UserListMod
from .models import UserWarnMod
from .serializer import UserWarnSerializer
from .serializer import UsersSerializer
from shopcart_list.models import ShopCartListMod


# Create your views here.
class UserQueryView(APIView):
    """
    查询所有用户信息
    """
    def get(self, request):
        try:
            UserData = UserListMod.objects.all()
            ret = UsersSerializer(UserData,many=True)
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

class UserQueryOneView(APIView):
    """
    查询单个用户信息
    """
    def get(self, request):
        try:
            uid = request.session.get("user_id", "")
            UserData = UserListMod.objects.filter(uid=uid)
            ret = UsersSerializer(UserData, many=True)
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

class UserEditView(APIView):
    """
    修改用户信息
    """
    def post(self, request):
        try:
            # 获取数据
            uid = request.session.get("user_id","")
            username = request.data.get("user_name", "")
            userpwd = request.data.get("user_pwd","")
            userads = request.data.get("user_address","")
            SqlData = UserListMod.objects.get(uid=uid)
            # 判断是否修改用户名
            if SqlData.user_name == username:
                SqlData.user_pwd = userpwd
                SqlData.user_address = userads
                SqlData.save()
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "msg": ERRORMSG.SUCCESS
                }
            else:
                # 判断用户名是否存在
                usercount = UserListMod.objects.filter(user_name=username).count()
                if usercount is 0:
                    SqlData.user_name = username
                    SqlData.user_pwd = userpwd
                    SqlData.user_address = userads
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

class UserDelView(APIView):
    """
    删除用户信息
    """
    def post(self, request):
        try:
            uid = request.data.get("uid","")
            UserListMod.objects.filter(uid=uid).delete()
            # 判断用户是否有购物车
            cartinfo = ShopCartListMod.objects.filter(uid=uid)
            if cartinfo.count() != 0:
                cartinfo.delete()
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

class UserQueryAddressView(APIView):
    """
    查询用户分布情况
    """
    def post(self, request):
        try:
            address = request.data.get("address","")
            UserCount = UserListMod.objects.filter(user_address=address).count()
            res = {
                "code":ERRORCODE.SUCCESS,
                "data":UserCount
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class UserWarnQueryView(APIView):
    """
    查询用户警告信息
    """
    def get(self, request):
        try:
            uid = request.session.get("user_id", "")
            UserData = UserWarnMod.objects.filter(uid=uid)
            if UserData.count() != 0:
                ret = UserWarnSerializer(UserData, many=True)
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

class UserWarnAddView(APIView):
    """
    添加用户警告信息
    """
    def post(self, request):
        try:
            uid = request.data.get("uid","")
            user_content = request.data.get("user_content","")
            userinfo = UserWarnMod.objects.filter(uid=uid)
            if userinfo.count() != 0:
                UserWarnMod.objects.filter(uid=uid).update(user_content=user_content)
            else:
                UserWarnMod.objects.create(uid=uid,user_content=user_content)
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

class UserWarnDelView(APIView):
    """
    删除用户警告信息
    """
    def post(self, request):
        try:
            uid = request.data.get("uid","")
            userinfo = UserWarnMod.objects.filter(uid=uid)
            if userinfo.count() == 0:
                res = {
                    "code": ERRORCODE.ERROR_ADD,
                    "msg": ERRORMSG.ERROR_ADD
                }
            else:
                userinfo.delete()
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