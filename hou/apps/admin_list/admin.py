# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import AdminListMod
from .models import AdminImageMod

# Register your models here.

admin.site.register(AdminListMod)
admin.site.register(AdminImageMod)
