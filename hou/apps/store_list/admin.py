# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import StoreListMod
from .models import StoreWarnMod

# Register your models here.

admin.site.register(StoreListMod)
admin.site.register(StoreWarnMod)