#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import urllib.request
from lxml import etree
import time
import gzip
#url = 'https://www.mzitu.com/xinggan/'

# 请求头添加 UA
HEADERS = {
    #'Host': 'www.mzitu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    #'Accept-Encoding': 'gzip, deflate, br',
    #'Connection': 'keep-alive',
    #'Cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1579949630; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1579949718',
    #'Upgrade-Insecure-Requests': '1',
    'referer': 'https://www.mzitu.com/'
}

# 保存路径
save_path = '/spider_file'


# 创建文件夹,并切换到所创建的文件夹
def create_file(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    # 切换路径至上面创建的文件夹
    os.chdir(file_path)


# 抓取外页数据
def get_outer(outer_url):
    req = urllib.request.Request(url=outer_url, headers=HEADERS, method='GET')
    resp = urllib.request.urlopen(req)

    html = etree.HTML(resp.read().decode('utf-8'))
    # 获取文件夹名称列表
    title_list = html.xpath('//*[@id="pins"]/li/a/img/@alt')
    # 获取跳转链接列表
    src_list = html.xpath('//*[@id="pins"]/li/a/@href')

    print('当前页面' + outer_url + ', 共计爬取' + str(len(title_list)) + '个文件夹')

    for i in range(len(title_list)):
        file_path = save_path + '\\' + title_list[i]
        img_url = src_list[i]
        # 创建对应文件夹
        create_file(file_path)
        # 写入对应文件
        get_inner(img_url, file_path)


# 抓取内页数据并写入文件
def get_inner(url, file_path):
    req = urllib.request.Request(url=url, headers=HEADERS, method='GET')
    resp = urllib.request.urlopen(req)

    html = etree.HTML(resp.read().decode('utf-8'))

    # 获取当前页面最大页数
    max_num = html.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()')[0]
    print('当前页面url：', url, ', 最大页数为', max_num)

    for i in range(1, int(max_num)):
        # 访问过快会被限制，增加睡眠时间
        time.sleep(1)
        try:
            inner_url = url + '/' + str(i)
            inner_req = urllib.request.Request(url=inner_url, headers=HEADERS, method='GET')
            inner_resp = urllib.request.urlopen(inner_req)
            inner_html = etree.HTML(inner_resp.read().decode('utf-8'))
        except Exception as e:
            print("inner_html 页面错误")

        # 获取图片 url
        img_src = inner_html.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')[0]
        file_name = str(img_src).split('/')[-1]
        # 下载图片
        try:
            request = urllib.request.Request(url=img_src, headers=HEADERS, method='GET')
            response = urllib.request.urlopen(request)
            get_img = response.read()
            file_os_path = file_path + '\\' + file_name
            if os.path.isfile(file_os_path):
                print('图片已存在：', file_os_path)
                pass
            else:
                with open(file_os_path, 'wb') as fp:
                    fp.write(get_img)
                    print('图片保存成功：', file_os_path)
                    fp.close()
        except Exception as e:
            print('图片保存失败')


def main():
    url = 'https://www.mzitu.com/xinggan/page/'
    for i in range(120, 163):
    #for i in range(1, 163):
        get_outer(url + str(i))


if __name__ == '__main__':
    main()
