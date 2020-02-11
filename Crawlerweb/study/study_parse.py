#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib.parse import urlparse, urlunparse

result = urlparse('https://docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse')
print(type(result))
print(result)
print(result.netloc)
print(result[1])

result1 = urlparse('docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse', scheme = "https", allow_fragments = False)
print(result1)

params = ('https', 'www.geekdigging.com', 'index.html', 'people', 'a=1', 'geekdigging')
print(urlunparse(params))

