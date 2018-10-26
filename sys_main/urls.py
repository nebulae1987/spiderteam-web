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
    path('main/',views.page_list,name='main_page'),
    path('introduce/',views.introduce_page,name='introduce_page'),
    path('meue/',views.meue_page,name='meue_page'),
    path('add_page/',views.add_page,name='add_page'),
    path('add_logic/',views.add_logic,name='add_logic'),

]

