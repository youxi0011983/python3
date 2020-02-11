#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib.parse import urlencode

# urlencode 示例
dictname = {
    "name": "极客挖掘机",
    "age": 18
}
print("https://www.geekdigging.com/" + urlencode(dictname))
