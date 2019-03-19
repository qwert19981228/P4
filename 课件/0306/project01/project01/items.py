# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Project01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Ip66Item(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()



class TencentItem(scrapy.Item):
    job_name = scrapy.Field()
    job_type = scrapy.Field()
    job_number = scrapy.Field()
    address = scrapy.Field()
    add_time = scrapy.Field()
    url = scrapy.Field()
    create_time = scrapy.Field()

    duty = scrapy.Field()
    requirement = scrapy.Field()