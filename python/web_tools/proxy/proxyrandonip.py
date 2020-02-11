#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request
import urllib
import os
import re
import random

URL= "http://www.baidu.com"
header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}


proxy_list = []
proxy_address=[]


#Open file imput ipadress list
#设置文件的路径
dir = "/home/eveline/python/web_tools/proxy_address/"

#查看目录下文件名，是否是txt文件，如果有读取文件内容
pattern_file = r'.*(txt)$'
for root, dirs, files in os.walk(dir):
    for file in files:
        matchfile=re.match(pattern_file,file)
        if matchfile == None:
            exit()
        proxy_file=open(dir+file,'r') 
        proxy_address.extend(proxy_file.readlines()) #####################
        #print (proxy_address)
        proxy_file.close()


#定义代理服务器的ip地址和http协议用。   
diction = {}
#print(proxy_address)

#从读取的文件中提取所有的IP地址和端口，保存到proxy_list 里
for num  in range(len(proxy_address)):
    #print(num)
    proxy_address[num]=proxy_address[num].strip()
    pattern_char = r'^(http://).*'
    match_char=re.match(pattern_char,proxy_address[num])
    if match_char == None:    
        proxy_address[num]=proxy_address[num].strip('https://')
        diction["https"]=proxy_address[num]
        proxy_list.append(diction)
    else:
        proxy_address[num]=proxy_address[num].strip('http://')
        diction["http"]=proxy_address[num]
        proxy_list.append(diction)

print(proxy_list)


#确认代理服务器可以下载目标网站内容，如果不行返回错误代码
def download_by_proxy(url,proxy_ip_dict):
    httpproxy_handler = urllib.request.ProxyHandler(proxy_ip_dict)
    opener = urllib.request.build_opener(httpproxy_handler)
    request = urllib.request.Request(url,headers=header)
    response = opener.open(request)
    return response


#使用proxy_list列表，访问目的网站，不能访问就排除IP地址
def crawl_web_data(url, proxy_ip_list):
    if len(proxy_ip_list) == 0:
        return ''
    proxy_ip_dict = proxy_ip_list[0]
    try:
        proxy_web = download_by_proxy(url, proxy_ip_dict)
        print(url, 'ok')     
    except Exception as e:
        #print('e', e)
        #删除无效的ip
        print('\nWrong ipadress:'+str(proxy_ip_list[0]))
        print(e)
        index = proxy_ip_list.index(proxy_ip_dict)
        proxy_ip_list.pop(index)
        print('proxy_ip_list\'s len change to:', len(proxy_ip_list))
        
        return crawl_web_data(url, proxy_ip_list)#再次尝试爬取
        
    return proxy_web


'''
# 随机选择一个代理
proxy = random.choice(proxy_list)
# 随机选择一个代理
httpproxy_handler = urllib.request.ProxyHandler(proxy)
nullproxy_handler = urllib.request.ProxyHandler({})

proxySwitch = True  #定义一个代理开关

# 根据代理开关是否打开，使用不同的代理模式
if proxySwitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

request = urllib.request.Request(URL,headers=header)
response = opener.open(request)
'''
response = crawl_web_data(URL,proxy_list)

if response=='':
    print('No ipadress can be use!')
else:
    print(response.read().decode('utf-8'))
