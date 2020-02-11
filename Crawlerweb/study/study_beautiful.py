#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.geekdigging.com/')
# soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

# soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

# soup = BeautifulSoup(response.content, "xml")
# print(soup.prettify())

soup = BeautifulSoup(response.content, "html5lib")
print(soup.prettify())
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.a)

tag = soup.body
print(tag.name)
print(tag['class'])
print(tag.attrs)

for i, child in enumerate(soup.body.div.descendants):
    print(i, child)

print(soup.title.parent)

print('next_sibling：', soup.title.next_sibling)
print('previous_sibling：', soup.title.previous_sibling)
print('next_siblings：', soup.title.next_siblings)
print('previous_siblings：', soup.title.previous_siblings)

# {"r":0,"subject":{"episodes_count":"","star":"40","blacklisted":"available","title":"我身体里的那个家伙 내안의 그놈‎ (2019)","url":"https:\/\/movie.douban.com\/subject\/27088750\/","collection_status":"","rate":"7.2","short_comment":{"content":"男主真的他妈帅 但是我真的接受不了和罗美兰打k ","author":"SOUL"},"is_tv":false,"subtype":"Movie","directors":["姜孝镇"],"actors":["郑振永","朴圣雄","罗美兰","李垂珉","李俊赫","金光奎","闵智雅","尹敬浩","金贤穆","朴庆惠","赵贤荣","尹颂雅","智燦","金凡振 ","郑元昌","孙光业","黄仁俊","Dae-han Kim"],"duration":"122分钟","region":"韩国","playable":false,"id":"27088750","types":["剧情","喜剧"],"release_year":"2019"}}
# https://movie.douban.com/j/subject_abstract?subject_id=27088750
