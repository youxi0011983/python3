#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib.parse import urlsplit

result_urlsplit = urlsplit("https://www.geekdigging.com/index.html;people?a=1#geekdigging")
print(type(result_urlsplit))
print(result_urlsplit)

print(result_urlsplit.netloc)
print(result_urlsplit[1])