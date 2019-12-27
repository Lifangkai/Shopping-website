# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import AdminQueryView
from .views import AdminQueryOneView
from .views import AdminQueryImageView

# 新引入的模块
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^query/', AdminQueryView.as_view(), name="admin_query"),
    url(r'^queryone/', AdminQueryOneView.as_view(), name="admin_query_one"),
    url(r'^queryimg/', AdminQueryImageView.as_view(), name="admin_query_img"),
] + static(settings.ADMIN_URL, document_root=settings.ADMIN_ROOT)

# urlpatterns += static(settings.ADMIN_URL, document_root=settings.ADMIN_ROOT)