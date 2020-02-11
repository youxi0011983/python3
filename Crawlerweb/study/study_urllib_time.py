#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import urllib.request
import urllib.parse
import urllib.error
import socket


response = urllib.request.urlopen('http://httpbin.org/get', timeout = 1)
print(response.read().decode('utf-8'))

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('请求超时啦~~~')
    else:
        print(e)
#classurllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)