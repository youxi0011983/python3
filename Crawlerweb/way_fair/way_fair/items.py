# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WayFairItem(scrapy.Item):
    collection = table = 'way_fair_products'
    id = scrapy.Field()
    average_overall_rating = scrapy.Field()
    consumer_price = scrapy.Field()
    display_price = scrapy.Field()
    list_price = scrapy.Field()
    manufacturer = scrapy.Field()
    product_name = scrapy.Field()
    review_count = scrapy.Field()
    size_option_count = scrapy.Field()
    sku = scrapy.Field()
    url = scrapy.Field()
