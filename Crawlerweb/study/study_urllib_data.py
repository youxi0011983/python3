#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import urllib.request
import urllib.parse

post_data = bytes(urllib.parse.urlencode({'name': 'geekdigging', 'hello':'world'}), encoding='utf8')
response = urllib.request.urlopen('https://httpbin.org/post', data = post_data)
print(response.read().decode('utf-8'))