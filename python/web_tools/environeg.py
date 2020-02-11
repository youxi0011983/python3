#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import urllib.request


username=os.environ.get("username")
password =os.environ.get("password")
user = os.environ['USER']		#当前使用用户。
#lc = os.environ['LC_COLLATE']	#路径扩展的结果排序时的字母顺序。
#shell = os.environ['SHELL']		#使用shell的类型。
#lan = os.environ['LAN']			#使用的语言。

ssh = os.environ['SSH_AUTH_SOCK']#ssh的执行路径。


print(username)
print(password)
print(user)
print(lc)
print(shell)
print(lan)
print(ssh)


url ="http://www.baidu.com/"

header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

}

# 构建一个私密代理Handler，需要加上私密代理账户的用户名和密码

authproxy_handler=urllib.request.ProxyHandler({"http" :username+':'+"password@61.135.217.7:80"})

opener = urllib.request.build_opener(authproxy_handler)

request = urllib.request.Request(url,headers=header)

response = opener.open(request)

print(response.read().decode('utf-8'))