# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import UserQueryView
from .views import UserQueryOneView
from .views import UserQueryAddressView
from .views import UserEditView
from .views import UserDelView
from .views import UserWarnQueryView
from .views import UserWarnAddView
from .views import UserWarnDelView

urlpatterns = [
    url(r'^query/', UserQueryView.as_view(), name="user_query"),
    url(r'^edit/', UserEditView.as_view(), name="user_edit"),
    url(r'^delete/', UserDelView.as_view(), name="user_delete"),
    url(r'^querywarn/', UserWarnQueryView.as_view(), name="user_warn_query"),
    url(r'^addwarn/', UserWarnAddView.as_view(), name="user_warn_add"),
    url(r'^deletewarn/', UserWarnDelView.as_view(), name="user_warn_delete"),
    url(r'^queryone/', UserQueryOneView.as_view(), name="user_query_one"),
    url(r'^queryaddress/', UserQueryAddressView.as_view(), name="user_query_address")
]