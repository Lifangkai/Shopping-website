# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView

from code_file import ERRORCODE
from code_file import ERRORMSG
from .models import AdminListMod,AdminImageMod
from .serializer import AdminListSerializer
from rest_framework_extensions.cache.decorators import (
    cache_response
)

# Create your views here.
class AdminQueryView(APIView):
    """
    查询所有管理员列表
    """
    def get(self, request):
        try:
            AdminData = AdminListMod.objects.all()
            ret = AdminListSerializer(AdminData,many=True)
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


class AdminQueryOneView(APIView):
    """
    查询单个管理员数据
    """
    def get(self, request):
        try:
            aid = request.session.get("admin_id","")
            AdminData = AdminListMod.objects.filter(aid=aid)
            ret = AdminListSerializer(AdminData,many=True)
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


class AdminQueryImageView(APIView):
    """
    管理员图片上传以及更新
    """
    def post(self, request):
        try:
            aid = request.data.get("aid", "")
            file = request.FILES.get("file","")
            AdminImageMod.objects.filter(aid=aid).delete()
            AdminImageMod.objects.create(aid=aid,file=file)
            admininfo = AdminListMod.objects.get(aid=aid)
            admininfo.admin_avator = file.name
            admininfo.save()
            res = {
                "code": ERRORCODE.SUCCESS,
                "data":file.name
            }
        except:
            res = {
                "code": ERRORCODE.ERROR_WEBSERVER,
                "msg": ERRORMSG.ERROR_WEBSERVER
            }
        return Response(res)