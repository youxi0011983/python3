#coding=utf-8
#import urllib.request
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
#url='http://www.baidu.com'
url='http://httpbin.org/get'
#response = urllib.request.urlopen('http://wwww.baidu.com')

#html = response.read()
#print(html)

response = requests.get(url)
json_text = response.json()
print(json_text)
#json_text=response.json()
#print(response.url)
#print(response.status_code)
#print(response.text)