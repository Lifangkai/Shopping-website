# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import FoodQueryView
from .views import FoodEditView
from .views import FoodDelView
from .views import FoodQueryListView
from .views import FoodImageView
from .views import FoodAddListView

# 新引入的模块
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^query/', FoodQueryView.as_view(), name="food_query"),
    url(r'^querylist/', FoodQueryListView.as_view(), name="food_query_one"),
    url(r'^queryimg/', FoodImageView.as_view(), name="food_query_img"),
    url(r'^edit/', FoodEditView.as_view(), name="food_edit"),
    url(r'^delete/', FoodDelView.as_view(), name="food_delete"),
    url(r'^create/', FoodAddListView.as_view(), name="food_add")
] + static(settings.FOOD_URL, document_root=settings.FOOD_ROOT)

# urlpatterns += static(settings.FOOD_URL, document_root=settings.FOOD_ROOT)