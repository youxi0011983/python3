#!/usr/bin/python3
# -*- coding: UTF-8 -*-


header = {
    'Host': 'www.xicidaili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWQ0NDE4MjRhMjQzYzgxMzE2YWZjZjM3YzZlZGQ3NWU1BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTkrcUNFcmtpVWVFT0lEQmF6THlONDBxM0JXaDUyMzFuRUsxbHFzNjI4M0U9BjsARg%3D%3D--0b1a46336d05cfdceddebb38b270ee6b5a9e3e10; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1579357493; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1579357541',
    'Upgrade-Insecure-Requests': '1'
}

# 获取模块
'''
获取模块相对比较简单，主要功能就是从各个免费代理网站上将我们所需要的代理信息抓取下来。示例如下：
'''

import requests
from pyquery import PyQuery
from MysqlClient import MysqlClient
from VerifyProxy import VerifyProxy


class CrawlProxy(object):
    def __init__(self):
        self.mysql = MysqlClient()
        self.verify = VerifyProxy()

    def get_page(self, url, charset):
        response = requests.get(url, headers=header)
        response.encoding = charset
        return response.text

    def crawl_ip(self, page_num=3):
        """ 获取代理 ip3366 :param page_num: :return: """
        proxy = []
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'
        urls = [start_url.format(page) for page in range(1, page_num + 1)]
        for url in urls:
            print('crawl:', url)
            html = self.get_page(url, 'gb2312')
            if html:
                d = PyQuery(html)
                trs = d('table tbody tr').items()
                for tr in trs:
                    scheme = tr.find('td:nth-child(4)').text().lower()
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    print(scheme, ip, port)
                    verify_result = self.verify.verify_proxy(scheme, ip, port)
                    if verify_result["status"] == '1':
                        proxy = {"scheme": scheme, "ip": ip, "port": port, "status": verify_result["status"],
                                 "response_time": verify_result["response_time"], }
                        # 存入数据库
                        self.mysql.add_proxy(proxy)
                        print('代理', ip, '连通测试已通过，已保存 Mysql')
                    else:
                        print('代理', ip, '连通测试未通过')


if __name__ == '__main__':
    CrawlProxy().crawl_ip(page_num=3520)
'''

小编这里出于示例只演示了从 ip3366 上抓取免费代理，并且在抓取到代理后，调用检查模块的检查方法对当前的代理进行连通性检查，如果连通性测试未通过则不会写入数据库中。
'''
