# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import FoodListMod
from .models import FoodImageMod

# Register your models here.

admin.site.register(FoodListMod)
admin.site.register(FoodImageMod)