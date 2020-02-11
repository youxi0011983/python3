#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
import requests
import re
 
###请求头
headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36',
           }

http_switch = False

if http_switch:
    proxy_url="http://www.xicidaili.com/wn/"
else:
    proxy_url="http://www.xicidaili.com/wt/"

proxy_url_num=3 ##设置页数 url_num * 100


###抓去代理IP
proxy_ip_pool=[]
for iurl in range(1,proxy_url_num+1):
    proxy_html = requests.get(proxy_url+str(iurl),headers=headers).text
    proxy_html=proxy_html.split("\n")
    for line in range(len(proxy_html)):
        tmp_ip=""
        ip = re.findall(r'\d+.\d+.\d+.\d+', proxy_html[line])   #Find ip address for proxy
        if ip != [] and "." in str(ip):
            port=proxy_html[line+1].split(">")[1].split("<")[0] #Find proxy use port
            tmp_ip=str(ip[0])+":"+str(port)
        if tmp_ip != "":
            proxy_ip_pool.append(tmp_ip)
print("Proxy ip pool len is :"+str(len(proxy_ip_pool)))
print (proxy_ip_pool)
 