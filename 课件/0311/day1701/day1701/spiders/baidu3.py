# -*- coding: utf-8 -*-
import scrapy


class Baidu3Spider(scrapy.Spider):
    name = 'baidu3'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/s?wd=ip']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES" : {}
    }
    def parse(self, response):
        print(response.text)
