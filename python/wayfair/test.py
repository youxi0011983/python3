#!/usr/bin/python3
# -*- coding: UTF-8 -*-

request = urllib2.Request(self.url)
request.add_header('Cookie','PHPSESSID=79lo60cmtl1ck70h4ufruq6n53; mmf_searchhotkeyandroid=%E5%A4%A9%E6%B6%AF%E7%A4%BE%E5%8C%BA%2C%E7%A9%BF%E8%A1%A3%E5%8A%A9%E6%89%8B%2C%E5%A4%A9%E6%B0%94%2C%E9%B3%84%E9%B1%BC%E5%B0%8F%E9%A1%BD%E7%9A%AE%E7%88%B1%E6%B4%97%E6%BE%A12%2C%E6%B0%B4%E6%9E%9C%E5%BF%8D%E8%80%85%2C%E4%B8%96%E7%95%8COL%2C%E6%88%98%E5%A4%A9; mmf_msisdn=08e2b01ad5dd5b3d297ef6558a60ec26; mmf_us=08e2b01ad5dd5b3d297ef6558a60ec26.39; mmf_userVisitPageIndex=79lo60cmtl1ck70h4ufruq6n53.2')
request.add_header('Connection','keep-alive')
request.add_header('Accept','*/*')
request.add_header('Accept-Language','zh-CN,zh;q=0.8')
request.add_header('Accept-Encoding','gzip,deflate,sdch')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36')
response = urllib2.urlopen(request)
print response.code
    if response.info().get('Content-Encoding')=='gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj = buf)
        data = f.read()
        f.close()