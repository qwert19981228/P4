# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=ip']

    def parse(self, response):
        print(response.body)
        print(response.xpath('//span[@class="c-gap-right"]/text()').extract())
