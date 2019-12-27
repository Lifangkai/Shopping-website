# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserListMod
from .models import UserWarnMod

# Register your models here.

admin.site.register(UserListMod)
admin.site.register(UserWarnMod)