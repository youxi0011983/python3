#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import time
import re
import random
import os
from query_json_request import *


page_url_arry = []
#读取data文件，提取地址所需的数字。
pattern_number=r'[0-9][0-9]+'
pattern_url=r'https://[a-z,\.,\/,\-,0-9]+'
with open('data2','r') as file:
	number = 0 
	while True:
		number += 1 
		line = file.readline()
		match_number = re.search(pattern_number,line)
		match_url = re.search(pattern_url,line)
		if line == '':
			break
		page_url_arry.append({'page_number':match_number.group(0),'url':match_url.group(0)})



def readweb_toexecl(page_number,url):
	t=time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
	product_pool=pd.DataFrame()
	newdata=[]
	newdict=dict()
	list_title = ['sku','url','product_name','manufacturer','average_overall_rating','review_count','display_price','consumer_price','list_price','size_option_count']
	result = []

	#读取所有页面的json值
	pro_data =query(page_number,1,url)
	pro_count = pro_data['pro_count']
	page_count = int(pro_count/96)
	result.extend(pro_data['result'])
	print(pro_data['url'])
	print("page  1 finish")
	for count_num in range(page_count):
		pro_data.clear()
		#url = url + str(count_num+2)
		pro_data = query(page_number,count_num+2,url)
		result.extend(pro_data['result'])
		print("page ",count_num+2,"finish")
		time.sleep(random.randint(1,5))


	for data in result:
		#确定display价格是否存在，处理display_price列内容多余的html标记。
		if 'display_price' in data: 
			pattern = r'\>from \<'
			patternnum =r'\<\/span\>' 
			match = re.findall(pattern,data['display_price'])
			if match != []:
				match = re.split(patternnum,data['display_price'])
				data['display_price']='from '+match[-1]

		#把需要的列添加到新字典里面
		newdata=[]
		for i in list_title:
			if i not in data:
				data[i] = ""
				newdata.append(data[i])
			else:
				newdata.append(data[i])
		newdict = dict(zip(list_title,newdata)) 	


		product_pool=product_pool.append(newdict,ignore_index=True,sort=True)
		data.clear()
		newdict.clear()
	product_pool.to_excel("foo"+t+".xlsx", sheet_name='Sheet1')
	print("write to excel,done.")



if __name__ == '__main__':
	for page in page_url_arry:
		print(page)
		readweb_toexecl(page['page_number'],page['url'])