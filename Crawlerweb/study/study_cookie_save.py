#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import http.cookiejar
import urllib.request

# cookies 保存 Mozilla 型文件示例
filename = 'cookies_mozilla.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
print('cookies_mozilla 保存成功')

# cookies 保存 LWP 型文件示例
filename = 'cookies_lwp.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
print('cookies_lwp 保存成功')


# 请求是使用 Mozilla 型文件
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookies_mozilla.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
