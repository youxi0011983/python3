#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from lxml import etree
import requests

response = requests.get('https://www.geekdigging.com/')
html_str = response.content.decode('UTF-8')
html = etree.HTML(html_str)

# result_1 = html.xpath('/html/body/section/div/div/main/article[1]/div[2]/div/h3/a/text()')
# result_1 = html.xpath('/html/body/div[1]/div/div/div[3]/ul[3]/li[4]/div/h2/a/text()')
result_1 = html.xpath('/html/body/div[1]/div/div/div[3]/ul[1]/li[1]/div[1]/a[1]/@href')
# result_2 = html.xpath('/html/body/div[1]/div/div/div[3]/ul[3]/li[4]/div/h2/a/@href')
result_2 = html.xpath('/html/body/div[1]/div/div/div[3]/ul[1]/li[1]/div[2]/div[1]/p/text()')
print(type(result_1), result_1)
print(result_2)

result_3 = html.xpath('//div[@class="item-img"]')
print(result_3)

# result_4 = html.xpath('//img[@class="j-lazy" and @alt="小白学 Python 爬虫（42）：春节去哪里玩（系列终篇）"]')
result_4 = html.xpath('//img[@class="attachment-post-thumbnail size-post-thumbnail wp-post-image j-lazy" and '
                      '@alt="小白学 Python 数据分析（2）：Pandas （一）概述"]')
print(result_4)

result_5 = html.xpath('//article/div/div/h3[@class="post-title"]/a/text()')
print(result_5)
result_6 = html.xpath('//article[1]/div/div/h3[@class="post-title"]/a/text()')
print(result_6)
result_7 = html.xpath('//article[last()]/div/div/h3[@class="post-title"]/a/text()')
print(result_7)
result_8 = html.xpath('//article[position() < 5]/div/div/h3[@class="post-title"]/a/text()')
print(result_8)

'''
/bookstore/book[1] 	选取属于 bookstore 子元素的第一个 book 元素。
/bookstore/book[last()] 	选取属于 bookstore 子元素的最后一个 book 元素。
/bookstore/book[last()-1] 	选取属于 bookstore 子元素的倒数第二个 book 元素。
/bookstore/book[position()<3] 	选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
//title[@lang] 	选取所有拥有名为 lang 的属性的 title 元素。
//title[@lang='eng'] 	选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
/bookstore/book[price>35.00] 	选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
/bookstore/book[price>35.00]/title 	选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。
'''
# 节点轴示例
# 获取所有祖先节点
result_9 = html.xpath('//article/ancestor::*')
print(result_9)
# 获取祖先节点 main 节点
result_10 = html.xpath('//article/ancestor::main')
print(result_10)

'''
轴名称	结果
ancestor	选取当前节点的所有先辈（父、祖父等）。
ancestor-or-self	选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
attribute	选取当前节点的所有属性。
child	选取当前节点的所有子元素。
descendant	选取当前节点的所有后代元素（子、孙等）。
descendant-or-self	选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following	选取文档中当前节点的结束标签之后的所有节点。
namespace	选取当前节点的所有命名空间节点。
parent	选取当前节点的父节点。
preceding	选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling	选取当前节点之前的所有同级节点。
self	选取当前节点。
'''
