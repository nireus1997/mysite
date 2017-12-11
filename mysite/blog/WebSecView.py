# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Blog, Category
from .models import Menu
from blog import views as Common

def ShowMainPage(request):
    return Show_WebSecPage_by_Cat(request)

def Show_WebSecPage_by_Cat(request):
    '''
    显示传入类型id对应的文章列表
    '''
    category_id = int(request.GET.get('cat', 0))
    category = ''
    for item in Category.objects.all():
        if category_id == item.id:
            category = item.name
            break
        else:
            category = "OWASP TOP 10"
    ctx = {
        'menus':Menu.objects.all().order_by('id'),
        'blogs':Blog.objects.all().filter(category__name__exact = category).order_by('-created'),
        'Categorys':Common.get_WebSec_category_info(),
        'site': Common.get_footer_info(),
    }
    return render(request, 'WebSec.html', ctx)

def Show_WebSecPage_blog_detail(request, article_id):
    article_id = int(article_id.encode('utf-8'))
    ctx = {
        'menus':Menu.objects.all().order_by('id'),
        'Categorys':Common.get_WebSec_category_info(),
        'article':Blog.objects.all().filter(id__exact = article_id)
        'site': Common.get_footer_info(),
    }
    return render(request, 'WebSec-article.html', ctx)
    pass
