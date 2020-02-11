#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from pyquery import PyQuery

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

d = PyQuery(html)
print(d('p'))
print("="*15, "next", "="*15, "\n")

d_url = PyQuery(url='https://www.geekdigging.com/', encoding='UTF-8')
print(d_url('title'))
'''
上面两端代码和下面相识
r = requests.get('https://www.geekdigging.com/')
r.encoding = 'UTF-8'
d_requests = PyQuery(r.text)
print(d_requests('title'))
'''
print("="*15, "next", "="*15, "\n")


d_css = PyQuery(html)
print(d_css('.story .sister'))
print(type(d_css('.story .sister')))
print("="*15, "next", "="*15, "\n")

# 查找子节点
items = d('body')
print('子节点：', items.find('p'))
print(type(items.find('p')))

# 查找父节点
items = d('#link1')
print('父节点：', items.parent())
print(type(items.parent()))

# 查找兄弟节点
items = d('#link1')
print('兄弟节点：', items.siblings())
print(type(items.siblings()))

print("="*15, "next", "="*15, "\n")

a = d('a')
for item in a.items():
    print(item)
    print(type(item))
    print(item.text())
print("="*15, "next", "="*15, "\n")


a_1 = d('#link1')
print(a_1.text())

a_2 = d('.story')
print(a_2.html())
print("="*15, "next", "="*15, "\n")

attr_1 = d('#link1')
print(attr_1.attr('href'))
print("="*15, "next", "="*15, "\n")

print(attr_1.attr.href)
