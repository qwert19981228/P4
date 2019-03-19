# -*- coding: utf-8 -*-
import scrapy
from scrapy_project.items import BlogItem


class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://python.jobbole.com/all-posts/']

    def parse(self, response):
        # 解析数据
        div_list = response.xpath('//div[@id="archive"]/div[@class="post floated-thumb"]')

        for div in div_list:
            item = BlogItem()
            title = div.xpath('.//a[@class="archive-title"]/text()').extract()[0]
            href = div.xpath('.//a[@class="archive-title"]/@href').extract()[0]
            types = div.xpath('.//a[@rel="category tag"]/text()').extract()[0]


            item['title']=title
            item['href']=href
            item['types']=types

            yield item





