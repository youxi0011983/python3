#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
from datetime import datetime

start = datetime.now()

for i in range(100):
    print(i)
    print(requests.get('https://www.baidu.com/').text)

end = datetime.now()

print("request花费时间为：", end - start)
