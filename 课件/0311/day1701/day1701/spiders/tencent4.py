# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor # 提取超链接
from scrapy.spiders import CrawlSpider, Rule


class Tencent4Spider(CrawlSpider):
    name = 'tencent4'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/']

    # url的规则
    rules = (
        Rule(LinkExtractor(allow=r'position.php\?tid=\d+'),callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=r'faq'),callback='type_item', follow=False),
    )
    # 解析url的response
    def parse_item(self, response):
        # print(response.xpath('//div[@class="butcjwt2"]/text()').extract())
        pass

    def type_item(self,response):
        print(response.url,'11111')
        # print(response.text)
        print(response.xpath('//h3[@class="pb9"]/text()').extract())
