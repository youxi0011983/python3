#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request
import urllib
import bs4 
URL= "http://www.baidu.com"
header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

proxy_web="http://www.xicidaili.com/"

proxy_ipaddress = "121.226.214.14"
proxy_port = "9999"

proxy_URL=proxy_ipaddress+':'+proxy_port


#爬虫时使用代理，经常会出现
#<urlopen error [Errno 111] Connection refused>
#或者
#<urlopen error timed out>
#这类的错误，造成这类问题的原因是代理ip不可用或者质量差
def crawl_web_data(url, proxy_ip_list):
    if len(proxy_ip_list) == 0:
        return ''
    proxy_ip_dict = proxy_ip_list[0]

    try:
        html = download_by_proxy(url, proxy_ip_dict)
        print(url, 'ok')
            
    except Exception as e:
        #print('e', e)
        #删除无效的ip
        index = proxy_ip_list.index(proxy_ip_dict)
        proxy_ip_list.pop(index)
        print('proxy_ip_list', len(proxy_ip_list))
        
        return crawl_web_data(url, proxy_ip_list)#再次尝试爬取
        
    return html


# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
#python2---urllib2.ProxyHandler({"http":"http://xx.xx.xx.xx:xxxx"})
httpproxy_handler = urllib.request.ProxyHandler({"http":proxy_URL})
nullproxy_handler = urllib.request.ProxyHandler({})

proxySwitch = True #定义一个代理开关

# 通过 urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
# 根据代理开关是否打开，使用不同的代理模式
if proxySwitch:
    #python2---opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)


request = urllib.request.Request(URL,headers=header)

response = opener.open(request)
#urllib2.install_opener(opener)
#content = urllib2.urlopen('http://xxxx').read()

print(response.read().decode('utf-8'))

#urllib.error.URLError: <urlopen error [Errno 111] Connection refused>
#这类的错误，造成这类问题的原因是代理ip不可用或者质量差，解决方法如下
