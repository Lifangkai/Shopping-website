# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BussCommentListMod
from .models import FoodCommentListMod

# Register your models here.

admin.site.register(BussCommentListMod)
admin.site.register(FoodCommentListMod)