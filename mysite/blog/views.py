# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Blog, Category
from .models import Menu
# Create your views here.



#Functions Common
def get_WebSec_category_info():
    category_Cnt = []
    for category in Category.objects.all():
        category_Cnt.append([category.name, len(Blog.objects.all().filter(category__name__exact = category.name)), '?cat=' + str(category.id)])
    return category_Cnt


def get_footer_info():
    site = {
        'weichat': '',
        'qq': 'http://wpa.qq.com/msgrd?v=3&uin=8354882&site=qq&menu=yes',
        'weibo': '',
        'github': '',
    }

    return site
