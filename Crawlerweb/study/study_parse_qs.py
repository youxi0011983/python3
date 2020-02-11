#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib.parse import parse_qs,parse_qsl


#这个方法可以让我们将一串 GET 请求中的参数转换成为字典
print(parse_qs("ie=UTF-8&wd=python"))

#还有一个parse_qsl()方法，它用于将参数转化为元组组成的列表

# parse_qsl 示例
print(parse_qsl("ie=UTF-8&wd=python"))