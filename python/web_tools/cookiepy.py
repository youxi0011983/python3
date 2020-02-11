#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request
import urllib
from http import cookiejar
import bs4

# 通过cookieJar（）类构建一个cookieJar（）对象，用来保存cookie的值

cookie = cookiejar.CookieJar()

# 通过HTTPCookieProcessor（）处理器类构建一个处理器对象，用来处理cookie
# 参数就是构建的CookieJar（）对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

# 构建一个自定义的opener
opener = urllib.request.build_opener(cookie_handler)

# 通过自定义opener的addheaders的参数，可以添加HTTP报头参数
opener.addhandlers = [("User-Agent", "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50")]
# 人人网的登陆接口
url = "http://www.baidu.com/"
# 需要登陆的账户密码
data = {"email": "xxxxxx", "password": "xxxxx"}
# 通过URL encode（）编码转换
data = urllib.parse.urlencode(data).encode("utf-8")

request = urllib.request.Request(url, data=data)

response = opener.open(request)

print(response.read())
