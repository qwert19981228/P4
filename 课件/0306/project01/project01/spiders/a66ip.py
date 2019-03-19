# -*- coding: utf-8 -*-
import scrapy
from project01.items import Ip66Item


class A66ipSpider(scrapy.Spider):
    name = '66ip'
    allowed_domains = ['66ip.cn']
    base_url = 'http://www.66ip.cn/%s.html'
    start_urls = []
    for url in range(1,1600):
        fullur = base_url % url
        start_urls.append(fullur)

    def parse(self, response):
        # 解析数据
        tr_list = response.xpath('//div[@align="center"]/table//tr')[1:]
        for i in tr_list:
            item = Ip66Item()
            td = i.xpath('./td/text()').extract()
            ip = td[0]
            port = td[1]

            item['ip']=ip
            item['port']=port

            yield item
