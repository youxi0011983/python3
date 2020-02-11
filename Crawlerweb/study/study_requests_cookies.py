#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests

r = requests.get("https://www.csdn.net")
print(type(r.cookies), r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)
print("="*15, "next", "="*15, "\n")

cookies = '_zap=d5ecf276-4da1-4ad8-85ae-2e0b8fff296c; d_c0="AKAY057LtRCPTqgqgzp22VB9l4oYDmCH3a0=|1579857989"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1579857991,1580028811; _xsrf=jsekATXkfm8O4dYSV83XavQa1us9sLU6; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1580029111|1580028805; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1580029034; capsion_ticket="2|1:0|10:1580029052|14:capsion_ticket|44:NTZhMjE3ZTk3Y2QwNGNmMmEzZmI4ZmQwZGU3ZjZlMzE=|c2e19623f4a1a195061580f005bdd7a4f22dc775678dbd8e274ca7c619f08d48"; l_n_c=1; r_cap_id="OTk0NDdmNWE4NmVhNDFlNjk5NWM3OGZlNzAwZGZiYWE=|1580028844|cb6959fa6cad938c48584c76fb67b9ad617446d5"; cap_id="MjM5NjU1YzQ3YmJhNDczOWFmZDUyNGI3MzA5NjA1OWQ=|1580028844|8b42db64916fc456d6c271362ba3a338b8d4c273"; l_cap_id="ODQ3YmNhYWExZjgwNGZiNGJhZjkwYzZkNzM5Y2ZjMjI=|1580028844|5ae80dab870fd52a682094e568bdde3223977cb7"; n_c=1; auth_type=d2VjaGF0|1580029043|0beb6db3849b86bdd1f65da724194e595be8a2c6; atoken=29_Nqw8xT1QOTRUy6L6hKpRklDaqHGf0wf0fkunA_MKulpmQYdV5Q_H-TbSmD6A4Ur44zxe20MmDs_A34yl_gZYK-pi3WdmxPOLUs37hs11mgY; atoken_expired_in=7200; token="MjlfTnF3OHhUMVFPVFJVeTZMNmhLcFJrbERhcUhHZjB3ZjBma3VuQV9NS3VscG1RWWRWNVFfSC1UYlNtRDZBNFVyNDR6eGUyME1tRHNfQTM0eWxfZ1pZSy1waTNXZG14UE9MVXMzN2hzMTFtZ1k=|1580029043|c23fe11cfde6cb6b548e3d4f2351cba41cc40224"; client_id="bzNwMi1qc3FqRzRxb3JyaDdfY3ZRclc1Uk9iYw==|1580029043|779bc723fe57250bb39253f4a0ef69ed48bd6af1"; z_c0="2|1:0|10:1580029112|4:z_c0|92:Mi4xa3pUY0NnQUFBQUFBb0JqVG5zdTFFQ2NBQUFDRUFsVk50LUZVWGdDcnFCWFhNa0tOQXYyZUhNaThBZ3I1Yks3aUhn|4991bb7388ebac64922c35a49b620c3493f21cc79da0987c318ec1dc8f3455d7"'
headers = {
    'cookie': cookies,
    'host': 'www.zhihu.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

r = requests.get('https://www.zhihu.com', headers = headers)
#print(r.text)
print("="*15, "next", "="*15, "\n")

# 构建 RequestsCookieJar 对象
jar = requests.cookies.RequestsCookieJar()

for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
print(jar)

headers_request = {
    'host': 'www.zhihu.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

r = requests.get('https://www.zhihu.com', cookies = jar, headers = headers_request)
#print(r.text)
print("="*15, "next", "="*15, "\n")


