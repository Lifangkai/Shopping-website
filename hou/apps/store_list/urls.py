# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import StoreQueryView
from .views import StoreQueryOneView
from .views import StoreEditView
from .views import StoreDelView
from .views import StoreQueryAddressView
from .views import StoreWarnQueryView
from .views import StoreWarnAddView
from .views import StoreWarnDelView

urlpatterns = [
    url(r'^query/', StoreQueryView.as_view(), name="store_query"),
    url(r'^queryone/', StoreQueryOneView.as_view(), name="store_query_one"),
    url(r'^edit/', StoreEditView.as_view(), name="store_edit"),
    url(r'^delete/', StoreDelView.as_view(), name="store_delete"),
    url(r'^querywarn/', StoreWarnQueryView.as_view(), name="store_warn_query"),
    url(r'^addwarn/', StoreWarnAddView.as_view(), name="store_warn_add"),
    url(r'^deletewarn/', StoreWarnDelView.as_view(), name="store_warn_delete"),
    url(r'^queryaddress/', StoreQueryAddressView.as_view(), name="store_query_address")
]