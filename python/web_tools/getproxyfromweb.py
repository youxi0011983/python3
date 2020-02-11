#coding=utf-8

import requests
import re
from bs4 import BeautifulSoup as bs
import queue as Queue
import threading 

class proxyPick(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            url = self._queue.get()

            proxy_spider(url)

def proxy_spider(url):
    headers = {
            ...
    }

    r = requests.get(url = url,headers = headers)
    soup = bs(r.content,"html.parser")
    data = soup.find_all(name = 'tr',attrs = {'class':re.compile('|[^odd]')})

    for i in data:

        soup = bs(str(i),'html.parser')
        data2 = soup.find_all(name = 'td')
        ip = str(data2[1].string)
        port = str(data2[2].string)
        types = str(data2[5].string).lower() 


        proxy = {}
        proxy[types] = '%s:%s'%(ip,port)
        try:
            proxy_check(proxy,ip)
        except Exception as e:
            print(e)
            pass

def proxy_check(proxy,ip):
    url = 'http://1212.ip138.com/ic.asp'
    r = requests.get(url = url,proxies = proxy,timeout = 6)

    f = open('E:/url/ip_proxy.txt','a+')

    soup = bs(r.text,'html.parser')
    data = soup.find_all(name = 'center')
    for i in data:
        a = re.findall(r'\[(.*?)\]',i.string)
        if a[0] == ip:
            #print proxy
            f.write('%s'%proxy+'\n')
            print('write down')
            
    f.close()

#proxy_spider()

def main():
    queue = Queue.Queue()
    for i in range(1,2288):
        queue.put('http://www.xicidaili.com/nn/'+str(i))

    threads = []
    thread_count = 10

    for i in range(thread_count):
        spider = proxyPick(queue)
        threads.append(spider)

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    print("It's down,sir!")

if __name__ == '__main__':
    main()