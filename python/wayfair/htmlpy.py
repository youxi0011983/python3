#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import re

url = "http://www.baidu.com"

result = requests.get(url)

result.encoding = "utf-8"

content = result.text


#print(content)

soup = BeautifulSoup(content,"html.parser")

div_tag = soup.find_all("div")

pattern = r'<.*\"wrapper\">'
for line in div_tag:
	#print(str(line)+"\n")
	match = re.findall(pattern,str(line))
	print(match)
	if match != []:
		print(line)


'''
print(title_tag)

print(title_tag.text)
'''