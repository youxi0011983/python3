# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from way_fair.items import WayFairItem
import uuid


class WayfairSpider(Spider):
    name = 'wayfair'
    allowed_domains = ['www.wayfair.com']
    start_urls = ['http://www.wayfair.com/']

    def start_requests(self):
        base_url = 'https://www.wayfair.com/outdoor/sb0/patio-furniture-covers-c417301.html'
        headers = {
            'Host': 'www.wayfair.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Referer': 'http://www.wayfair.com/',
        }
        # how may page?
        #url = base_url+'?itemsperpage=96'
        #response = Request(url= url, headers= headers)
        #print(response)
        #print("\n")
        #pages = response.css('.Pagination-item Pagination-item--disabled::text')
        #print(pages)
        pages = self.settings.get('MAX_PAGE')
        for page in range(1, pages + 1):
            url = base_url+'?itemsperpage=96&curpage='+str(page)
            yield Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        products = response.css()
        for product in products:
            item = WayFairItem()
            item['id'] = str(uuid.uuid1())
            item['average_overall_rating'] = product.css
            item['consumer_price'] = product.css
            item['display_price'] = product.css
            item['list_price'] = product.css
            item['manufacturer'] = product.css
            item['product_name'] = product.css
            item['review_count'] = product.css
            item['size_option_count'] = product.css
            item['sku'] = product.css
            item['url'] = product.css
            yield item
