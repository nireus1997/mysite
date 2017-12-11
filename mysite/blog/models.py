# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Menu(models.Model):
    """
    导航菜单
    """

    name = models.CharField('菜单名称', max_length=16, default='Web安全')
    href_name = models.CharField('链接', max_length=16, default='')
    descript = models.CharField('描述', max_length=16, default='')

    def __unicode__(self):
        return self.name
    def __unicode__(self):
        return self.descript

class Category(models.Model):
    """
    一级目录
    """

    name = models.CharField('目录名称', max_length=16)
    menu = models.ForeignKey(Menu, verbose_name='菜单')

    def __unicode__(self):              # __str__ on Python 3
        return self.name

class Tag(models.Model):
    """
    标签
    """

    name = models.CharField('标签名称', max_length=16)

    def __unicode__(self):              # __str__ on Python 3
        return self.name


class Blog(models.Model):
    """
    博客
    """

    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='一级目录')
    tags = models.ManyToManyField(Tag, verbose_name='标签')


    def __unicode__(self):              # __str__ on Python 3
        return self.title
    def __unicode__(self):              # __str__ on Python 3
        return self.author
    def __unicode__(self):              # __str__ on Python 3
        return self.content


class Comment(models.Model):
    """
    评论
    """

    blog = models.ForeignKey(Blog, verbose_name='博客')

    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)

    created = models.DateTimeField('发布时间', auto_now_add=True)

    def __unicode__(self):              # __str__ on Python 3
        return self.name
    def __unicode__(self):              # __str__ on Python 3
        return self.content
