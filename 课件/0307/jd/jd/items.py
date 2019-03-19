# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goods_title = scrapy.Field()
    goods_price = scrapy.Field
    goods_comment = scrapy.Field()
    goods_url = scrapy.Field()
    shop_name = scrapy.Field()
