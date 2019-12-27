# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import CartQueryView
from .views import CartAddView
from .views import CartDelView
from .views import CartEditView
from .views import PayHandlerView
from .views import AliPayView

urlpatterns = [
    url(r'^query/', CartQueryView.as_view(), name="cart_query"),
    url(r'^edit/', CartEditView.as_view(), name="cart_edit"),
    url(r'^delete/', CartDelView.as_view(), name="cart_delete"),
    url(r'^create/', CartAddView.as_view(), name="cart_add"),
    url(r'^alipay/', AliPayView.as_view(), name="alipay"),
    url(r'^alipay_handler/', PayHandlerView.as_view(), name="alipay_after")
]

# urlpatterns += static(settings.FOOD_URL, document_root=settings.FOOD_ROOT)