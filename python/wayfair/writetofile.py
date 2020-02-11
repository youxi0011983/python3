#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request
import urllib
from http import cookiejar
from bs4 import BeautifulSoup
import time
import requests
import re
import numpy as np
import pandas as pd
import os

#要访问具体页面
URL="https://www.wayfair.com/outdoor/sb0/patio-conversation-sets-c35236.html?curpage="
HEADER={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

def reponse_postweb(url,headers):
	request = urllib.request.Request(url,headers=headers)
	reponse = urllib.request.urlopen(request)
	return reponse

def reponse_getweb(url,headers):
	reponse = requests.get(url,headers=headers).text
	return reponse

#Can't use this web www.wayfair.com
def reponse_web(url,headers):
	return urllib.request.urlopen(url).read()

def writetofile(reponse):
	with open('wayfairpost2.html','wb') as file:
		file.write(reponse)
	file.close()


reponse = reponse_postweb(URL+'1',HEADER)
writetofile(reponse.read())