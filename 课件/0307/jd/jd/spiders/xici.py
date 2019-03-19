# -*- coding: utf-8 -*-
import scrapy
from jd.settings import User_Agent


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/']

    def parse(self, response):
        print(response.status)
        print(response.request.headers)


