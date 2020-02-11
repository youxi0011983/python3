#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
import requests
import re
 
###请求头
headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36',
           }

http_switch = True

if http_switch:
    proxy_url="http://www.xicidaili.com/wn/"
else:
    proxy_url="http://www.xicidaili.com/nn/"

proxy_url_num=1 ##设置页数 url_num * 100
 
###抓去代理IP
proxy_ip_pool=[]
for iurl in range(1,proxy_url_num+1):
    proxy_html = requests.get(proxy_url+str(iurl),headers=headers).text()
    proxy_html=proxy_html.split("\n")
    for line in range(len(proxy_html)):
        tmp_ip=""
        ip = re.findall(r'\d+.\d+.\d+.\d+', proxy_html[line])   #Find ip address for proxy
        if ip != [] and "." in str(ip):
            port=proxy_html[line+1].split(">")[1].split("<")[0] #Find proxy use port
            tmp_ip=str(ip[0])+":"+str(port)
        if tmp_ip != "":
            proxy_ip_pool.append(tmp_ip)
            
#print("Proxy ip pool len is :"+str(len(proxy_ip_pool)))
 
###验证代理IP是否可用
proxy_ip_pool_test=[]
test_url="https://www.sogou.com/" ##验证网址：搜狗
for itest in proxy_ip_pool:
    proxies = {}
    if http_switch:
        proxies["https"]="https://"+itest #使用代理IP https
    else:
        proxies["http"]="http://"+itest #使用代理IP http
    try:
        proxy_test = requests.get(test_url, headers=headers,proxies=proxies,timeout=5)
        print(proxy_test)
        if http_switch:
            proxy_ip_pool_test.append(proxies["https"])
        else:
            proxy_ip_pool_test.append(proxies["http"])  
    except:
        print("error proxy ip")
#print(len(proxy_ip_pool_test))
 
t=time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
f1 = open("/home/eveline/python/web_tools/proxy_address/"+"proxy_ip_"+t+".txt",'w')
for line in proxy_ip_pool_test:
    f1.write(line+"\n")
f1.close()
