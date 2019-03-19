# -*- coding: utf-8 -*-
import scrapy
from project01.items import TencentItem
import datetime

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']
    base_url = 'https://hr.tencent.com/'

    headers = {}


    def parse(self, response):
        # 解析数据
        tr_list = response.xpath('//table[@class="tablelist"]//tr[@class="even"] | //table[@class="tablelist"]//tr[@class="odd"]')
        for tr in tr_list:

            td_list = tr.xpath('./td')
            job_name = td_list[0].xpath('./a/text()').extract()[0]
            url = self.base_url + td_list[0].xpath('./a/@href').extract()[0]
            #       extract_first  如果没有获取到就返回none
            job_type = td_list[1].xpath('./text()').extract_first()

            job_number = td_list[2].xpath('./text()').extract()[0]
            address = td_list[3].xpath('./text()').extract()[0]
            add_time = td_list[4].xpath('./text()').extract()[0]
            item={}
            item['job_name']=job_name
            item['url']= url
            item['job_type']=job_type
            item['job_number']=job_number
            item['address']=address
            item['add_time']=add_time
            item['create_time'] = datetime.datetime.now().strftime('%Y-%m-%d')


            print(url)

            # 创建详情页的请求
            yield scrapy.Request(url=url,callback=self.infoparse,meta={'data':item})

        # 获取下一页的url 并且强写一页的url发送
        nex_url = self.base_url + response.xpath('//a[@id="next"]/@href').extract()[0]
        yield scrapy.Request(url=nex_url,callback=self.parse,headers=self.headers)

    # 解析详情页的方法
    def infoparse(self,response):
        # print(response.meta)
        item = TencentItem()
        # 获取所有的tr
        tr_list = response.xpath('//table[@class="tablelist textl"]//tr')
        duty = tr_list[2].xpath('./td//li/text()').extract()
        duty = ''.join(duty)
        requirement = tr_list[3].xpath('./td//li/text()').extract()
        requirement = ''.join(requirement)
        for key,value in response.meta['data'].items():
            item[key] = value
        item['requirement'] = requirement
        item['duty'] = duty
        yield item




