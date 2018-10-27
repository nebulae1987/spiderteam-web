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
    path('sys_main/',views.page_list,name='sys_main'),
    path('page_menu/',views.page_menu,name='page_menu'),
    path('page_introduce/',views.page_introduce,name='page_introduce'),
]

