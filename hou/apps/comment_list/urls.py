# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import BussCommQueryView
from .views import FoodCommQueryView
from .views import BussCommAddView
from .views import FoodCommAddView

urlpatterns = [
    url(r'^busscomm/', BussCommQueryView.as_view(), name="busscomm_query"),
    url(r'^foodcomm/', FoodCommQueryView.as_view(), name="foodcomm_query"),
    url(r'^busscreate/', BussCommAddView.as_view(), name="busscomm_add"),
    url(r'^foodcreate/', FoodCommAddView.as_view(), name="foodcomm_add"),
]