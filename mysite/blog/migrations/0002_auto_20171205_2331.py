# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=16, verbose_name='\u5206\u7c7b\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=16, verbose_name='\u6807\u7b7e\u540d\u79f0'),
        ),
    ]
