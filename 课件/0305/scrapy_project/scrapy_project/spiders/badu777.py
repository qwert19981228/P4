# -*- coding: utf-8 -*-
import scrapy


class Badu777Spider(scrapy.Spider):
    name = 'badu777'
    allowed_domains = ['jd.com']  # 限制域名
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        res = response.xpath('//title/text()').extract()
        print(res)
