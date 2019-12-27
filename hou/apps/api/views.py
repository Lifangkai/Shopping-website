# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.views import APIView
from code_file import ERRORCODE
from code_file import ERRORMSG
from comm_func import create_id
from user_list.models import UserListMod
from store_list.models import StoreListMod
from admin_list.models import AdminListMod


# Create your views here.
class LoginUserView(APIView):
    """
    用户系统登陆
    """
    def post(self, request):
        try:
            user_name = request.data.get("username","")
            pwd = request.data.get("password","")
            usercount = UserListMod.objects.filter(user_name=user_name).count()
            # 判断用户是否存在
            if usercount != 0:
                userinfo = UserListMod.objects.get(user_name=user_name)
                # 判断密码是否正确
                if userinfo.user_pwd == pwd:
                    request.session["user_id"] = userinfo.uid
                    res = {
                        "code":ERRORCODE.SUCCESS,
                        "msg":ERRORMSG.SUCCESS
                    }
                else:
                    res = {
                        "code": ERRORCODE.ERROR_LOGIN,
                        "msg": ERRORMSG.ERROR_PASSWORD
                    }
            else:
                res = {
                    "code": ERRORCODE.ERROR_LOGIN,
                    "msg": ERRORMSG.ERROR_USERNAME
                }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class LoginStoreView(APIView):
    """
    商家系统登陆
    """
    def post(self, request):
        try:
            store_name = request.data.get("username","")
            pwd = request.data.get("password","")
            storecount = StoreListMod.objects.filter(store_name=store_name).count()
            # 判断商家是否存在
            if storecount != 0:
                storeinfo = StoreListMod.objects.get(store_name=store_name)
                # 判断密码是否正确
                if storeinfo.store_pwd == pwd:
                    request.session["store_id"] = storeinfo.sid
                    # print storeinfo.sid
                    res = {
                        "code":ERRORCODE.SUCCESS,
                        "msg":ERRORMSG.SUCCESS
                    }
                else:
                    res = {
                        "code":ERRORCODE.ERROR_LOGIN,
                        "msg":ERRORMSG.ERROR_PASSWORD
                    }
            else:
                res = {
                    "code": ERRORCODE.ERROR_LOGIN,
                    "msg": ERRORMSG.ERROR_USERNAME
                }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class LoginAdminView(APIView):
    """
    管理员系统登陆
    """
    def post(self, request):
        try:
            admin_name = request.data.get("username","")
            pwd = request.data.get("password","")
            admincount = AdminListMod.objects.filter(admin_name=admin_name).count()
            # 判断管理员是否存在
            if admincount != 0:
                admininfo = AdminListMod.objects.get(admin_name=admin_name)
                # 判断密码是否正确
                if admininfo.admin_pwd == pwd:
                    request.session["admin_id"] = admininfo.aid
                    res = {
                        "code": ERRORCODE.SUCCESS,
                        "msg": ERRORMSG.SUCCESS
                    }
                else:
                    res = {
                        "code": ERRORCODE.ERROR_LOGIN,
                        "msg": ERRORMSG.ERROR_PASSWORD
                    }
            else:
                res = {
                    "code": ERRORCODE.ERROR_LOGIN,
                    "msg": ERRORMSG.ERROR_USERNAME
                }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)

class UserRegisterView(APIView):
    """
    用户系统注册
    """
    def post(self, request):
        try:
            data = request.data
            uid = create_id()
            usercount = UserListMod.objects.filter(user_name=data.get("username","")).count()
            if usercount is 0:
                dic = {
                    "uid":uid,
                    "user_name":data.get("username", ""),
                    "user_pwd":data.get("password", ""),
                    "user_time":data.get("time", ""),
                    "user_address":data.get("address", "")
                }
                UserListMod.objects.create(**dic)
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "msg": ERRORMSG.SUCCESS
                }
            else:
                res = {
                    "code": ERRORCODE.ERROR_REGISTER,
                    "msg": ERRORMSG.ERROR_ADD
                }
        except:
                res = {
                    "code": ERRORCODE.ERROR_WEBSERVER,
                    "msg": ERRORMSG.ERROR_WEBSERVER
                }
        return Response(res)

class StoreRegisterView(APIView):
    """
    商家系统注册
    """
    def post(self, request):
        try:
            data = request.data
            sid = create_id()
            storecount = StoreListMod.objects.filter(store_name=data.get("username","")).count()
            if storecount is 0:
                dic = {
                    "sid":sid,
                    "store_name":data.get("username", ""),
                    "store_pwd":data.get("password", ""),
                    "store_time":data.get("time", ""),
                    "store_address":data.get("address", "")
                }
                StoreListMod.objects.create(**dic)
                res = {
                    "code": ERRORCODE.SUCCESS,
                    "msg": ERRORMSG.SUCCESS
                }
            else:
                res = {
                    "code": ERRORCODE.ERROR_REGISTER,
                    "msg": ERRORMSG.ERROR_ADD
                }
        except:
                res = {
                    "code": ERRORCODE.ERROR_WEBSERVER,
                    "msg": ERRORMSG.ERROR_WEBSERVER
                }
        return Response(res)