# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BussinessListMod
from .models import BusinessImageMod

# Register your models here.

admin.site.register(BussinessListMod)
admin.site.register(BusinessImageMod)