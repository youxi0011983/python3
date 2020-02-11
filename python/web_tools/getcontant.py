#!/usr/bin/python3
import urllib.request
import bs4 
URL= "http://www.baidu.com"
response = urllib.request.urlopen(URL)
str = response.read()

soup = bs4.BeautifulSoup(str,'html.parser')
print (soup)

'''
import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd

URL = 'https://www.timbuk2.com/collections/sale'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

scripts = soup(text=re.compile(r'products:'))[0].parent
print(scripts)
'''