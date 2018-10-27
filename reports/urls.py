#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 16:31
# @Author  : Jun
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path,include
from . import views
app_name = 'reports'
urlpatterns=[
    path('reportsPie/',views.reports,name='reportsPie'),
]