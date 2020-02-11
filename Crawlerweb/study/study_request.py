#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request

request = urllib.request.Request('https://www.geekdigging.com/')
with urllib.request.urlopen(request) as response:
    print(response.read().decode('utf-8'))
