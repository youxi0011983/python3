#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests

r = requests.get('https://httpbin.org/get')
print(r.text)
print("="*15, "next", "="*15, "\n")


params = {
    'name': 'geekdigging',
    'age': '18'
}
r1 = requests.get('https://httpbin.org/get', params)
print(r1.text)
print("="*15, "next", "="*15, "\n")


print(type(r1.text))
print(r1.json())
print(type(r.json()))
print("="*15, "next", "="*15, "\n")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'referer': 'https://www.geekdigging.com/'
}
r2 = requests.get('https://httpbin.org/get', headers = headers)
print(r2.text)
print("="*15, "next", "="*15, "\n")


r3 = requests.get("https://www.baidu.com/img/superlogo_c4d7df0a003d3db9b65e9ef0fe6da1ec.png")
with open('baidu_logo.png', 'wb') as f:
    f.write(r3.content)
    print("save pic...")
print("="*15, "next", "="*15, "\n")
