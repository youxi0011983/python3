#!/usr/bin/python3
# -*- coding: UTF-8 -*-


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

#检查模块
'''
检查模块相对也会简单一些，功能是从数据库中取出所有可以用的代理，进行轮询检查，看看是不是有代理是连不通的，如果连不通则修改连通性标记位，将此代理标记为不可用。示例代码如下：
'''
import requests 
from MysqlClient import MysqlClient


class VerifyProxy(object):
	def __init__(self): 
		self.mysql = MysqlClient()

	def verify_proxy(self, scheme, ip, port):
		""" 使用百度测试代理的连通性，并返回响应时长（单位：ms） :param scheme: :param ip: :param port: :return: """
		proxies = { scheme: scheme + '://' + ip + ':' + port + '/' }
		response_time = 0
		status = '0'
		try:
			response = requests.get(scheme + '://www.baidu.com/get', proxies=proxies, headers = header)
			if response:
				response_time = round(response.elapsed.total_seconds() * 1000)
				status = '1'
				print(status)
			else:
				response_time = 0
				status = '0'
		except:
			pass
		return ({'response_time':response_time,'status':status})

	def verify_all(self):
		""" 验证住方法，从数据库中获取所有代理进行验证 :return: """ 
		results = self.mysql.find_all() 
		for result in results: 
			res = self.verify_proxy(result[1], result[2], result[3])
			proxy = { "id": result[0], "scheme": result[1], "ip": result[2], "port": result[3], "status": res["status"], "response_time": res["response_time"], } 
			self.mysql.update_proxy(proxy) 
			print('代理验证成功')


if __name__ == '__main__': 
	VerifyProxy().verify_all()

'''
小编这里使用的是度娘进行连通性测试，如果各位同学有特殊的需要，可以使用特定的网站进行连通性测试。
'''
'''
小结

本篇的内容到这里就结束了，不过有一点要说明，本篇的示例内容只能作为 DEMO 来进行测试使用，对于一个连接池来讲，还有很多不完善的地方。

例如检测模块应该是定时启动，自行检测，现在是靠人手动启动，不过这个可以使用各种系统上的定时任务来解决。

还有，现在要获取连接信息只能自己打开数据库从中 Copy ，这里其实还可以加一个 API 模块，写成一个接口，供其他有需要使用代理的系统进行调用。

获取模块现在小编也只是简单的有一个网站写一个方法，其实可以使用 Python 高级用法，获取到类中所有的方法名，然后调用所需要的方法。

总之，这个 DEMO 非常不完善，等小编下次有空的时候完善下，到时候还可以再来一个推送。

'''