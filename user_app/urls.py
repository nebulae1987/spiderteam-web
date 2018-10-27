#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 9:24
# @Author  : Jun
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('loginPage',views.loginPage,name = 'loginPage'),        #登录页面
    path('loginLogic',views.loginLogic,name = 'loginLogic'),
    path('registPage',views.registPage,name = 'registPage'),     #注册页面
    path('registLogic',views.registLogic,name = 'registLogic'),
    path('checkEmail',views.checkEmail,name = 'checkEmail'),       #检测邮箱可用性
    path('forgetPwdPage',views.forgetPwdPage,name = 'forgetPwdPage'),  #忘记密码页面
    path('forgetLogic',views.forgetLogic,name = 'forgetLogic'),     #忘记密码验证
    path('changePwdPage',views.changePwdPage,name = 'changePwdPage'),  #修改密码页面
    path('changePwd',views.changePwd,name = 'changePwd'),     #修改密码
    path('index',views.index,name = 'index'),                 #修改密码
]