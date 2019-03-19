# -*- coding: utf-8 -*-
import scrapy
from day1602.items import Day1602Item

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=1672%2C2575%2C5257&go=0']

    def parse(self, response):
        img_list=response.xpath('//div[@class="p-img"]//img/@src').extract()
        for i in img_list:
            item = Day1602Item()
            item['pic_url']=['http:'+i]
            yield item

