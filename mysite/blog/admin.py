# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Tag, Blog, Menu
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Menu)
