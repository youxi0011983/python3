#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.wayfair.com/outdoor/cat/outdoor-patio-furniture-sale-c1851581.html',
            'https://www.wayfair.com/outdoor/sb0/outdoor-pillows-c416222.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)