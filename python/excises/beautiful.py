#coding=utf-8
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
url='http://httpbin.org/get'
response = requests.get(url)
json_text = response.json()

html_doc = str(json_text)


'''
html_doc="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="tile"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters；and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
'''

soup = BeautifulSoup(html_doc,features="lxml")
print(soup.prettify())