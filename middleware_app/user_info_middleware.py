#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 8:47
# @Author  : mxt
# @Site    :
# @File    : user_info_middleware.py
# @Software: PyCharm
import happybase
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
import time, re, urllib
from urllib import request

class MyMiddleware2(MiddlewareMixin):
    # 每次请求都会获取请求的信息（ip等等）
    pre_ip=''
    count=0
    flag=0
    def process_request(self, request):
        # 获得用户的访问时间
        request_time = time.strftime('%Y-%m-%d %H:%M:%S')
        datas = request.META
        try:
            # 获得用户的访问路径
            path_info = datas['PATH_INFO']
        except Exception:
            path_info = ''
            path_info = path_info.split('?')[1].split('&')
            #获得用户访问的城市和职位
        try:
            city_info = path_info[0].split('=')[1]
        except Exception:
            city_info=''
        try:
            job_info = path_info[1].split('=')[1]
        except Exception:
            job_info=''
        try:
            # 获得访问用户的ip
            ip = datas['REMOTE_ADDR']
        except Exception:
            ip = datas['HTTP_X_FORWARDED_FOR']
        # try:

        ipaddr = ip
        if self.pre_ip=='':
            self.pre_ip=ipaddr
            self.flag=1
            time_s=time.time()
        elif self.pre_ip==ipaddr:
            self.count += 1
        else:
            self.pre_ip=''
            self.count=0
            self.flag=0
        if self.count==300:
            time_e=time.time()
            time_u=time_e-time_s
            if time_u<300:
                return HttpResponseForbidden('<h1 style="text-align:center;margin-top:20px;">检测到您的ip异常，请稍后再试</h1>')
        print('ip:', ipaddr)
        # 根据ip获得用户详细信息（所在城市等）
        if ipaddr != "" or ipaddr != 'exit':
            print('符合判断条件，进入程序')
            url = "http://www.ip138.com/ips138.asp?ip=" + ipaddr + "&action=2"
            print('url:',url)
            u = urllib.request.urlopen(url)
            s = u.read()
            s = s.decode('gbk')
            # print('s:',s)
            ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s)
            print("\n****** Below Result From IP138 Database *****")
            result = re.findall(r'(<li>.*?</li>)', s)
            info1=''
            for i in result:
                #将ip详细信息拼接为字符串
                info1+= ''.join(i[4:-5])
            print('info1:',info1)
        #     print("没有获得数据")
        if info1 !='':
            conn = happybase.Connection(host='192.168.0.99', port=9090, autoconnect=False)
            conn.open()
            table = conn.table('spiderteam:t_logs')
            row_key = ipaddr+'_'+request_time
            table.put(row_key, {'info:ip_info': info1, 'info:request_time':request_time,'info:request_city':city_info,'info:request_job':job_info})
            print('日志已保存')
                # query = "RowFilter(=,'substring:ipaddr')"
                # t = table.scan(filter=query)
                # count=0
                # l=[]
                # for i in t:
                #     a=bytes.decode(i[0])#获得每个rowkey的字符串
                #     b=a.split('_')#将ip和时间分开，获得列表b
                #     ip=b[0]#获得ip
                #     if ip==ipaddr:#将ip和刚才访问的ipaddr比较，如果一样，累加器加一
                #         count+=1
                #     timeStamp=time.mktime(b[1])#将rowkey的日期转换为时间戳
                #     l.append(timeStamp)#将时间戳添加到列表l中
                #     l.sort()#将列表排序（从大到小顺序）
                #     n=len(l)#获得列表长度
                #     count_time=l[0]-l[n-1]#用时间戳最大值减去最小值，获得时间段
                #     if count>60 and count_time<10:#判断条件
                #         return HttpResponseForbidden('<h1 style="text-align:center;margin-top:20px;">检测到您的ip异常，请稍后再试</h1>')


    # def process_response(self, request, response):
    #     print("response:", request, response)
    #     return response  # 持续返回响应

