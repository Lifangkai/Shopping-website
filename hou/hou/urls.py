# -*- coding: utf-8 -*-
"""hou URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework.documentation import include_docs_urls
from django.conf.urls import url,include
from django.contrib import admin
from .views import Login


# 新引入的模块
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^[a-zA-Z0-9]*$', Login.as_view(), name="login"),
    url(r'api/', include('api.urls')),
    url(r'userlist/', include('user_list.urls')),
    url(r'businesslist/', include('business_list.urls')),
    url(r'foodlist/', include('food_list.urls')),
    url(r'orderlist/', include('order_list.urls')),
    url(r'adminlist/', include('admin_list.urls')),
    url(r'commentlist/', include('comment_list.urls')),
    url(r'storelist/', include('store_list.urls')),
    url(r'shopcartlist/', include('shopcart_list.urls')),
    url(r'^docs/', include_docs_urls(title='My REST API'))
] + static(settings.LUNBO_URL, document_root=settings.LUNBO_ROOT)
