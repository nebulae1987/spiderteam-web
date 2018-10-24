#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 20:01
# @Author  : ZJ
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path

from sys_main import views

app_name='sys_main'
urlpatterns = [
    path('sys_main/',views.page_list),
]

