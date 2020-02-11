#!/usr/bin/python3
# -*- coding: UTF-8 -*-		

import requests 
from pyquery import PyQuery 


header ={
'Host': 'www.xicidaili.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWQ0NDE4MjRhMjQzYzgxMzE2YWZjZjM3YzZlZGQ3NWU1BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTkrcUNFcmtpVWVFT0lEQmF6THlONDBxM0JXaDUyMzFuRUsxbHFzNjI4M0U9BjsARg%3D%3D--0b1a46336d05cfdceddebb38b270ee6b5a9e3e10; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1579357493; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1579357541',
'Upgrade-Insecure-Requests': '1'
}


page_num=1

def get_page(url, charset): 
		response = requests.get(url,headers=header) 
		response.encoding = charset 
		return response.text 

start_url = 'https://www.kuaidaili.com/free/inha/{}/' 
urls = [start_url.format(page) for page in range(1, page_num + 1)] 
for url in urls: 
	print(url)
	print('crawl:', url) 
	html = get_page(url, 'gb2312') 
	if html: 
		d = PyQuery(html) 
		trs = d('table tbody tr').items()
		for tr in trs: 
			#print(tr)
			#print("="*40)
			scheme = tr.find('td:nth-child(4)').text().lower() 
			ip = tr.find('td:nth-child(1)').text() 
			port = tr.find('td:nth-child(2)').text() 
			print(scheme,ip,port,"\n")
			print("="*40)