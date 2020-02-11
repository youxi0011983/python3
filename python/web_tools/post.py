#!/usr/bin/python3
import urllib.request
import urllib
import bs4 
URL= "http://www.baidu.com"

form = {'name':'abc','password':'1234'}
form_data = urllib.parse.urlencode(form).encode(encoding='UTF8')
request = urllib.request.Request(URL,form_data)

reponse = urllib.request.urlopen(request)
str = reponse.read()

with  open('post.html','wb') as file:
    file.write(str)

#print (str)