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


t=time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
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






#设置页数要访问页面数 url_num 
url_max_num=1
#建立产品池，保存产品内容,数据的列名
product_pool = pd.DataFrame(columns=['Name', 'Color', 'Manufacturer', 'Price', 'Last_price', 'Messaging', 'Reviews', 'Shipping','category'])

'''
with open('wayfairpost2.html','rb') as file:
	web_html=file.read()
file.close()

#web_html=reponse_postweb(URL+"1",HEADER)
soup = BeautifulSoup(web_html,"html.parser")
temp_tag = soup.find("div", class_ = 'Grid-item--row u-mt-6 BrowseCore-footer')
max_num = temp_tag.find("span", class_ = 'Pagination-item Pagination-item--disabled')
url_max_num=int(max_num.string)
print(url_max_num)
'''

#访问所有页面
for iurl in range(1,url_max_num+1):
	#web_url = URL + str(iurl)
	#print(web_url)
	#print("\n")
	#web_html=reponse_postweb(web_url,HEADER)
	with open('wayfairpost2.html','rb') as file:
		web_html=file.read()
	file.close()
	#print(web_html)

	

	#判断标签所包含内容
	soup = BeautifulSoup(web_html,"html.parser")
	temp_tag = soup.find("div", class_ = 'BrowseProductGrid')
	div_tag = temp_tag.find_all("div",class_ = 'ProductCard-details')
	category_tag = soup.find_all("li",class_ = 'Breadcrumbs-listItem')



	
	#定义所用到变量，数据到处表格excel文件。
	len_num=0
	Name=''
	Color_option=0
	Manufacturer=''
	Price=0
	Last_price=0
	Messaging=''
	Reviews=0
	Shipping=''
	category=''

	#具体是那个分类
	for line in category_tag:
		category = category+"/"+str(line.contents[0].string)
	
	#产品的详细内容
	for line in div_tag:
		#找到产品的颜色或则种类
		Color_option=None
		match = line.find(class_='ProductCard-options')
		if match != []:
			tagstr = match.find(class_='pl-VisuallyHidden')
			if tagstr != None:
				Color_option = str(tagstr.string)
			else:
				Color_option=None
		#print(Color_option)
		
		#找到产品名称，没有返回空
		Name = None
		Manufacturer = None
		match = line.find(class_='ProductCard-header')
		if match != []:
			tagstr = match.find(class_='ProductCard-name')
			if tagstr != []:
				Name = str(tagstr.string)
			else:
				Name = None

			tagstr = match.find("p",class_='ProductCard-manufacturer')
			#print(tagstr)
			if tagstr != []:
				Manufacturer = str(tagstr.contents[1])
			else:
				Manufacturer = None			
		#print(Manufacturer)

		#price 
		Price = None
		match = line.find(class_='ProductCard-pricing')
		match_2 = line.find(class_='ProductCard-specialPricing')
		if match != None :
			#print(match)
			tagstr = match.find(class_='ProductCard-price ProductCard-price--sale')
			tagstr_2 = match.find(class_ = 'from_text emphasis wf_bodycolortext note')
			tagstr_3 = match.find('span', class_ = 'ProductCard-price')
			#print(tagstr_2)
			#print(tagstr)
			if tagstr_2 != None:
				Price = str(tagstr_2.next_sibling)
			elif tagstr != None:
				Price = str(tagstr.string)
			elif tagstr_3 != None:
				Price = str(tagstr_3.string)
		elif match_2 !=[]:
			tagstr = match_2.find(class_='LightningDealsBanner-price')
			if tagstr != None:
				Price = str(tagstr.string)
			else:
				Price = None
		#print(Price)

		Last_price = None
		match = line.find(class_='ProductCard-pricing')
		match_2 = line.find(class_ = 'ProductCard-specialPricing')
		if match != None:
			tagstr = match.find(class_='ProductCard-price ProductCard-price--listPrice')
			if tagstr != None:
				Last_price = str(tagstr.string)
			else:
				Last_price=None
		elif match_2 != None:
			tagstr = match_2.find(class_ = 'LightningDealsBanner-price-strikethrough')
			if tagstr != None:
				Last_price = str(tagstr.string)
			else:
				Last_price=None			
		#print(Last_price)



		Reviews = 0
		match = line.find(class_='ProductCard-reviews')
		if match != None:
			tagstr = match.find(class_='pl-ReviewStars-reviews')
			if tagstr != None:
				Reviews = int(tagstr.string)
			else:
				Reviews = 0
		#print(Reviews)


		Shipping = None
		match = line.find(class_ = 'ProductCardShipping')
		match_2 = line.find(class_ = 'LightningDealsBanner-shipping')
		if match != None:
			tagstr = match.find(class_='ShippingHeadline-text')
			if tagstr != None:
				Shipping = str(tagstr.string)
			else:
				Shipping = None
		elif match_2 != None:
			tagstr = match_2.find(class_='LightningDealsBanner-freeShipping')
			if tagstr != None:
				Shipping = str(tagstr.string)
			else:
				Shipping = None
		#print(Shipping)


		len_num=len_num+1
		print(len_num,"\n")

		#保存数据，
		lstemp=[{'Name':Name,'Color_option':Color_option,'Manufacturer':Manufacturer,'Price':Price,'Last_price':Last_price,'Messaging':'','Reviews':Reviews,'Shipping':Shipping,'category':category}]
		product_pool=product_pool.append(lstemp,ignore_index=True,sort=True)
	
	print(product_pool.category)
	
	
product_pool.to_excel("foo"+t+".xlsx", sheet_name='Sheet1')