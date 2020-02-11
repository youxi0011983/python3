#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib import request, error

# 访问明显不存在的地址，使用 HTTPError 捕捉异常
try:
    response = request.urlopen('https://www.geekdigging.com/aa')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')

try:
    response = request.urlopen('https://www.geekdigging.com/aa')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Success!')
