#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'referer': 'https://www.geekdigging.com/'
}

params = {
    'name': 'geekdigging',
    'age': '18'
}

r = requests.post('https://httpbin.org/post', data = params, headers = headers)
print(r.text)
print("="*15, "next", "="*15, "\n")


r = requests.get('https://www.baidu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
print("="*15, "next", "="*15, "\n")


try:
    r = requests.get("https://www.geekdigging.com/", timeout = 0.1)
    print(r.status_code)
except Exception as e:
    print(e)
print("="*15, "next", "="*15, "\n")


proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

requests.get("https://www.geekdigging.com/", proxies=proxies)
print("="*15, "next", "="*15, "\n")

proxies_socket = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}

requests.get("https://www.geekdigging.com/", proxies = proxies_socket)
