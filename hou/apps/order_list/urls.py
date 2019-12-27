# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import OrderQueryView
from .views import OrderEditView
from .views import OrderAddView
from .views import OrderDelView

# 新引入的模块
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    url(r'^query/', OrderQueryView.as_view(), name="order_query"),
    url(r'^edit/', OrderEditView.as_view(), name="order_edit"),
    url(r'^add/', OrderAddView.as_view(), name="order_add"),
    url(r'^delete/', OrderDelView.as_view(), name="order_delete"),
]

# urlpatterns += static(settings.FOOD_URL, document_root=settings.FOOD_ROOT)