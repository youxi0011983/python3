#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests

def query(num,page,url):
	URL = 'https://www.wayfair.com/a/superbrowse/get_data?category_id={}&caid={}&clid=132&filter=&curpage={}&itemsperpage=96&search_id=&show_favorites_button=true&product_offset=0&load_initial_products_only=false&is_initial_render=true'.format(num,num,page)
	HEADER = {'Host': 'www.wayfair.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
	'Accept': 'application/json',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': url,
	'X-Requested-With': 'XMLHttpRequest',
	'X-Parent-TXID': 'otAgb14gUwEoujKwOBWiAg==',
	'Connection': 'keep-alive',
	'Cookie': 'CSNUtId=a2d02064-5e20-507a-8587-d422540a8202; canary=0; CSNPersist=page_of_visit%3D231%26latestRefid%3DDTR1; _px3=4986a21ba65fd997e0b3442bbb104f5be8fbd46a340a2253a1137cde67d7ddca:c8p6W/F4dnGzncSGRANIw5Zd8CqJgeZ0qo9U3IleGjTnnqYGLgrENnE6FgrS2cxu7uWX1gDYiTebBBxOOkbesA==:1000:jrsyNDiKxybF4nvOFyDywnjMOJJ5edL9b1zAwo8QjkkVQ3T+5vi3R5dt0fqIvxwob4KHfpIh2y0uXh1PZ+kQA01wp2rEpofL9j0ueL9gcOC/DEUOKDdtfCVCL2VZgKYJJgVRaphV5K3/qsgQ47++f3UB4V8FBTETM1zu7EsO5E0=; _pxvid=22c69feb-39cc-11ea-9023-0242ac12000a; _ga=GA1.2.478159346.1579176067; _gid=GA1.2.578677124.1579176067; otx=otAgbl4iwPqiQ5pPkoIsAg%3D%3D; pushNotificationsSignupSent=true; lastRskxRun=1579330461855; rskxRunCookie=0; rCookie=huexkhwm87lncivli3myk5gp0jbt; LowIntentModalSoftClosed=1; CSN=PRVW%3DW000606316%257CW002446721%26CLVW%3D132%257C340%257C128%257C80%257C295; _pxhd=6d70a2b6f78b1cfd2110e137d19cfa4d06ebdd1d6688314ec21c9d85b8a4d293:d02fc780-65bc-11e9-b971-bb43e5539738; vid=a2d0206f-5e22-8e9b-b0e6-9ff52ba24202; WFSID=ac133fb1d1a62d3155a7914599e995a6; CSNBrief=SLoc%3Dbo1%26open_in_new_tab%3D1%26TopNavCSSCachedByBrowser%3Dtrue; serverUAInfo=%7B%22browser%22%3A%22Mozilla+Firefox%22%2C%22browserVersion%22%3A72%2C%22OS%22%3A%22Windows%22%2C%22OSVersion%22%3A%2210%22%2C%22isMobile%22%3Afalse%2C%22isTablet%22%3Afalse%7D; featureDetect={"isTouch":false,"hasMQ":true,"deviceWidth":1536,"deviceHeight":728,"devicePixelRatio":1.25}; WFDC=BO; _gat_a=1; AMP_TOKEN=%24ERROR; _gat_b=1; ClickLocation=PAGINATION%3A2; ClickLocationMetadata=emptynull',
	'TE':'Trailers'}

	#print(URL,HEADER)
	response = requests.get(URL,headers = HEADER)
	result = response.json()
	response.close()
	pro_count = result['browse']['product_count']
	result = result['browse']['browse_grid_objects']
	print(pro_count)
	
	return {'result':result,'pro_count':pro_count,'url':URL}




if __name__ == '__main__':
	#data = query(1851581,2)
	detail = query(1863288,2,'https://www.wayfair.com/outdoor/cat/patio-furniture-sets-sale-c1863288.html')
	print("============================")
	data = detail['result']
	n=0
	i=0
	for detail in data:
		print("item",i)
		i = i + 1
		for item in detail.items():
			print(n,item)

			n = n + 1
		if i == 5:
			break
		n=0
