# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import BussinessQueryView
from .views import BussinessEditView
from .views import BussinessDelView
from .views import BussQueryOneView
from .views import BussinessImageView
from .views import BussinessPermitView
from .views import BussinessCaterView
from .views import BussinessAddView

# 新引入的模块
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^query/', BussinessQueryView.as_view(), name="bussiness_query"),
    url(r'^create/', BussinessAddView.as_view(), name="bussiness_add"),
    url(r'^edit/', BussinessEditView.as_view(), name="bussiness_edit"),
    url(r'^delete/', BussinessDelView.as_view(), name="bussiness_delete"),
    url(r'^queryone/', BussQueryOneView.as_view(), name="bussiness_query_one"),
    url(r'^queryimg/', BussinessImageView.as_view(), name="bussiness_query_img"),
    url(r'^querypermit/', BussinessPermitView.as_view(), name="bussiness_query_permit"),
    url(r'^querycater/', BussinessCaterView.as_view(), name="bussiness_query_cater"),
] + static(settings.BUSSINESS_URL, document_root=settings.BUSSINESS_ROOT)

# urlpatterns += static(settings.BUSSINESS_URL, document_root=settings.BUSSINESS_ROOT)