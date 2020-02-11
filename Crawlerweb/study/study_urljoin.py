#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib.parse import urljoin

#只有在第二个参数链接缺失 scheme 、 netloc 和 path 这三个内容的时候，才会从第一个参数中获取对应的内容进行组合
print(urljoin("https://www.geekdigging.com/", "index.html"))
print(urljoin("https://www.geekdigging.com/", "https://www.geekdigging.com/index.html"))
print(urljoin("https://www.geekdigging.com/", "?a=aa"))
print(urljoin("https://www.geekdigging.com/#geekdigging", "https://docs.python.org/zh-cn/3.7/library/urllib.parse.html"))