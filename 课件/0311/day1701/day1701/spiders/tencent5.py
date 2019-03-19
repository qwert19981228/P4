# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Tencent5Spider(CrawlSpider):
    name = 'tencent5'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?keywords=&tid=0&start=0#a']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'position_detail.php'), callback='parse_info', follow=False),
    )

    # 解析的是列表页
    def parse_item(self, response):
        # with open('ten.html','w',encoding='utf-8') as f:
        #     f.write(response.text)
        # print(response.url)
        # print(response.text)
        # print(response.xpath('//tr/td/a/text()').extract())
        pass
    # 详情页
    def parse_info(self,response):
        print(response.url)
        print(response.xpath('//table/tr[@class="c"]/td/div/text()').extract())
