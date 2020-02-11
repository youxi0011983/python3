#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib import request, error
import socket

# 异常类型示例
try:
    response = request.urlopen('https://www.baidu.com', timeout=0.001)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
