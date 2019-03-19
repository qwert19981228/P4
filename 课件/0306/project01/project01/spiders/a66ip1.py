# -*- coding: utf-8 -*-
import scrapy
from project01.items import Ip66Item


class A66ipSpider(scrapy.Spider):
    name = '66ip1'
    allowed_domains = ['66ip.cn']
    base_url = 'http://www.66ip.cn'
    start_urls = ['http://www.66ip.cn/1540.html']


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

        # 判断什么时候停止 当页面中没有>>后就停止
        if '»' == response.xpath('//div[@id="PageList"]/a[last()]/text()').extract()[0]:
            # 获取新的请求 并将请求发送给队列
            newurl = self.base_url + response.xpath('//div[@id="PageList"]/a[last()]/@href').extract()[0]
            # 将新的url提交到队列 callback 指定当前请求完成后由谁来解析 如果不指定默认由parse
            yield scrapy.Request(url=newurl,callback=self.parse)

