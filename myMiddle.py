#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 22:46
# @Author  : Jun
# @Site    : 
# @File    : myMiddle.py
# @Software: PyCharm
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
import requests,json
from lxml import etree

class ToLogin(MiddlewareMixin):
    def process_request(self,request):
        ip = request.META['REMOTE_ADDR']
        print('middle guest ip:', ip)
        session_login = request.session.get('login')
        #访客信息：

        ip = request.META['REMOTE_ADDR']
        road = request.get_full_path()    #包含关键字：搜索职位和城市
        print('request.url：', road,type(road))
        sea_city,sea_position = '',''
        if 'city' in road:
            sea_city = road[road.find('?'):].split('&')[0][6:]
            print(111,sea_city)
        if 'position' in road:
            sea_position = road[road.find('?'):].split('&')[1][9:]
            print(222,sea_position)

        city = '局域网'
        # net_ip = json.loads(requests.get('http://httpbin.org/ip').text)['origin']
        # if net_ip:
        #     print('访客ip：',net_ip)
        #     url = 'https://ip.cn/index.php?ip='+net_ip
        #     print('url:',url)
        #     #访客城市：
        #     city = (etree.HTML(requests.get(url).text)).xpath('//div[@class="well"]/p/code/text()')[1]
        #     print('city:',city)


        # if 'user' not in request.path:
        #     if not session_login:
        #         return redirect('user:loginPage')



