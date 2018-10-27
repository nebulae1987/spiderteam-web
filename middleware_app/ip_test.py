#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 9:46
# @Author  : mxt
# @Site    :
# @File    : ip_test.py
# @Software: PyCharm
import datetime
import urllib
from urllib import request
import re
import happybase
# try:
#     ipaddr = '118.26.72.101'
#     # ipaddr = raw_input("Enter IP Or Domain Name:")
#     if ipaddr != "" or ipaddr != 'exit':
#         url = "http://www.ip138.com/ips138.asp?ip=" + ipaddr + "&action=2"
#         print(url)
#         u = urllib.request.urlopen(url)
#         s = u.read()
#         s = s.decode('gbk')
#         # Get IP Address
#         ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s)
#         request_time = datetime.datetime.now().strftime('%Y-%m-%d')
#         print(request_time)
#         print("\n****** Below Result From IP138 Database *****")
#         print("IP Address:", ip[0])
#         # Get IP Address Location
#         result = re.findall(r'(<li>.*?</li>)', s)
#         for i in result:
#             info=''.join(i[4:-5])
#             print(info)
#         # print("*" * 45)
#         # print("\n")
# except Exception:
#     print("Not Data Find")

conn = happybase.Connection(host='192.168.0.99', port=9090, autoconnect=False)
conn.open()
table = conn.table('spiderteam:t_logs')
# query="RowFilter(=,'substring:127.0.0.1')"
t=table.scan()
# print(list(t))
l=[]
for i in t:
    print(type(i[0].decode('utf-8')))




