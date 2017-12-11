# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Blog, Category
from .models import Menu
from blog import views as Common


def ShowAbout(request):
    ctx = {
        'menus':Menu.objects.all().order_by('id'),
        'site': Common.get_footer_info(),
    }
    return render(request, 'blank.html', ctx)
