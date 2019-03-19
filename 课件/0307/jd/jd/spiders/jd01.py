# -*- coding: utf-8 -*-
import scrapy


class Jd01Spider(scrapy.Spider):
    name = 'jd01'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E8%BF%9E%E8%A1%A3%E8%A3%99%E6%96%B0%E5%93%81&enc=utf-8&wq=%E8%BF%9E%E8%A1%A3%E8%A3%99%E6%96%B0%E5%93%81&pvid=0537a1f59dc64f3fa3d0f3f72c375205']

    def parse(self, response):
        base_url = 'https://search.jd.com/Search?keyword=%E8%BF%9E%E8%A1%A3%E8%A3%99%E6%96%B0%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%BF%9E%E8%A1%A3%E8%A3%99%E6%96%B0%E5%93%81&zx=2&page='
        for i in range(1,3,2):
            new_url = base_url+str(i)
            yield scrapy.Request(url=new_url,callback=self.parse_list,meta={'selenium':True})

    def parse_list(self,response):
        # docuemnt.xpath()
        goods_list = response.xpath('//ul[@class="gl-warp clearfix"]/li')
        for i in goods_list:
            goods_url = 'http:'+ i.xpath('.//div[@class="p-name p-name-type-2"]/a/@href').extract()[0]
            # 手动创建请求
            yield scrapy.Request(url=goods_url,callback=self.parse_info,meta={'selenium':True})


    def parse_info(self,response):
        # print(response.status)
        goods_name = response.xpath('//div[@class="sku-name"]/text()').extract()
        goods_price = response.xpath('//span[@class="p-price"]/span[last()]/text()').extract()
        goods_id = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li[2]/@title').extract()
        goods_img = response.xpath('//img[@id="spec-img"]/')





