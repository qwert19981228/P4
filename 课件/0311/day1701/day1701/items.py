# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Day1701Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pname = scrapy.Field()  # 职位标题
    money = scrapy.Field()  # 薪资
    location = scrapy.Field()  # 地址
    year = scrapy.Field()  # 工作经验
    degree = scrapy.Field()  # 学历
    ptype = scrapy.Field()  # 职位类型
    tags = scrapy.Field()  # 职位标签
    date_pub = scrapy.Field()  # 发布日期
    advantage = scrapy.Field()  # 职位诱惑
    jobdesc = scrapy.Field()  # 职位描述
    jobaddr = scrapy.Field()  # 地址
    company = scrapy.Field()  # 公司
