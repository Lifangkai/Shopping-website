# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import LoginUserView
from .views import LoginStoreView
from .views import LoginAdminView
from .views import UserRegisterView
from .views import StoreRegisterView

urlpatterns = [
    url(r'^userlogin/', LoginUserView.as_view(), name="user_login"),
    url(r'^storelogin/', LoginStoreView.as_view(), name="store_login"),
    url(r'^adminlogin/', LoginAdminView.as_view(), name="admin_login"),
    url(r'^userregister/', UserRegisterView.as_view(), name="user_register"),
    url(r'^storeregister/', StoreRegisterView.as_view(), name="store_register"),
    # url(r'^text/', BookHandle.as_view(), name="text"),
]