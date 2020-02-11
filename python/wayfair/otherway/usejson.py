#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests

#pre_url = "https://www.wayfair.com/outdoor/cat/outdoor-patio-furniture-sale-c1851581.html"
#URL = pre_url+'?itemsperpage=96&curpage=1'
URL = 'https://www.wayfair.com/a/quickbrowse/get_data?category_id=1851581&caid=1851581&maid=0&filter=&solr_event_id=0&registry_type=0&ccaid=0&curpage=2&itemsperpage=96&search_id=&collection_id=0&show_favorites_button=true&registry_context_type_id=0&product_offset=0&load_initial_products_only=false&is_initial_render=false'

HEADER = {'Host': 'www.wayfair.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
'Accept': 'application/json',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.wayfair.com/outdoor/cat/outdoor-patio-furniture-sale-c1851581.html?itemsperpage=96',
'X-Requested-With': 'XMLHttpRequest',
'X-Parent-TXID': 'otAgb14gUwEoujKwOBWiAg==',
'Connection': 'keep-alive',
'Cookie': 'CSNUtId=a2d02064-5e20-507a-8587-d422540a8202; vid=a2d02064-5e20-507a-8587-d422540a8202; WFSID=c1c1ba872cd1816f111d0f235fa058c0; canary=0; WFDC=BO; CSNBrief=is_new_user%3D1%26SLoc%3Dbo1%26open_in_new_tab%3D1%26TopNavCSSCachedByBrowser%3Dtrue; serverUAInfo=%7B%22browser%22%3A%22Mozilla+Firefox%22%2C%22browserVersion%22%3A72%2C%22OS%22%3A%22Windows%22%2C%22OSVersion%22%3A%2210%22%2C%22isMobile%22%3Afalse%2C%22isTablet%22%3Afalse%7D; CSNPersist=page_of_visit%3D20%26latestRefid%3DDTR1; _px3=a37b2f0e4916744ee74eb7830d6cf9ac84ec755d66881c7b31776e2a5a18aacf:SdiSUGqCanz0Hx6yYfhGca2QO/CCp4XZHgvU6S0M0xF1InQJaE+Ruqu/6E+YZ3kTen/q8CSvi0Bvht6pNlow0w==:1000:HnmAssQvgblBcrbEl52Ega+ejKmQTbBzt87uV5RGuHtKO4Q7wPudkfrSkEh/DijkeaspPro099eixTWfA8moq6iy54vk8PzKf5xu36p0Mt3BhRFnmUqUVzoJK9gaVnfYwWBy7i4WxGvPoiiO/x9m0t77M4Sa+pfcZE/62d3J4Oc=; _pxvid=e0899f6c-3857-11ea-aedf-0242ac12000b; _ga=GA1.2.478159346.1579176067; _gid=GA1.2.578677124.1579176067; otx=otAgb14gUmgo4zKyPrIZAg%3D%3D; pushNotificationsSignupSent=true; dtr=1; lastRskxRun=1579176667862; rskxRunCookie=0; rCookie=huexkhwm87lncivli3myk5gp0jbt; LowIntentModalSoftClosed=1; ClickLocation=PAGINATION%3A2; ClickLocationMetadata=emptynull; Scribe=RefTxid%3DotAgb14gUwEoujKwOBWiAg%3D%3D%26ClickType%3Ddata-click-location',
'TE':'Trailers'}


response = requests.get(URL,headers = HEADER)
result = response.json()
result = result['browse']['browse_grid_objects']


n=0
i=0
for detail in result:
	print("item",i)
	i = i + 1
	for item in detail.items():
		print(n,item)
		n = n + 1
	n=0
