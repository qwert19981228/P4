# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lagoudemo.items import LagoudemoItem
import datetime,re
class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS" :{
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "_ga=GA1.2.1388328988.1550029757; user_trace_token=20190213114711-0b5b405a-2f42-11e9-8179-5254005c3644; LGUID=20190213114711-0b5b43d4-2f42-11e9-8179-5254005c3644; WEBTJ-ID=20190311112627-1696ac98d4e40a-096cd22f7e6f13-414c042a-1440000-1696ac98d4f44e; _gid=GA1.2.344658191.1552274788; JSESSIONID=ABAAABAAAIAACBIEBFA6BF6D9E3451EDF92403A768FA0B8; index_location_city=%E4%B8%8A%E6%B5%B7; LGSID=20190311193828-30995ec7-43f2-11e9-a805-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D04tAEskQ1CIGw69gnGRHIGxk5yBLRiZF182ua6qR6OC%26wd%3D%26eqid%3D9c2b01840000138b000000035c8648b0; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1551790222,1552274788,1552274793,1552304352; TG-TRACK-CODE=index_navigation; SEARCH_ID=5c0e154b591d4d8faec8c1f5e76339ca; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552305148; LGRID=20190311195144-0aac7f3c-43f4-11e9-a821-525400f775ce",
            "Host": "www.lagou.com",
            "Referer": "https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
        }
}

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/\w+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_list', follow=True),

    )

    def parse_item(self, response):
        item = {}
        pass
    def parse_list(self, response):
        pname = response.xpath('//div[@class="job-name"]/@title').extract()[0]  # 职位标题
        pname = str(pname)
        money = response.xpath('//span[@class="salary"]/text()').extract()[0]  # 薪资
        nomoney = money.split('-')
        startmoney = nomoney[0][:-1]+'k'
        endmoney = nomoney[1][:-2]+'k'
        location = response.xpath('//dd[@class="job_request"]//span[2]/text()').extract()[0].replace('/', '')  # 地址
        year = response.xpath('//dd[@class="job_request"]//span[3]/text()').extract()[0].replace('/', '')  # 工作经验
        degree = response.xpath('//dd[@class="job_request"]//span[4]/text()').extract()[0].replace('/', '')  # 学历
        ptype = response.xpath('//dd[@class="job_request"]//span[5]/text()').extract()[0].replace('\n', '')  # 职位类型
        tags = response.xpath('//ul[@class="position-label clearfix"]/li/text()').extract()
        tags = ''.join(tags)
        date_pub = response.xpath('//p[@class="publish_time"]/text()').extract()[0].replace('\xa0', '').replace('\'', '').replace('"', '').replace('\n','').replace('\'','')  # 发布日期
        date_pub = ''.join(date_pub)
        advantage = response.xpath('//dd[@class="job-advantage"]/p/text()').extract()  # 职位诱惑
        advantage = ','.join(advantage)
        jobdesc = response.xpath('//div[@class="job-detail"]/p/text()').extract()  # 职位描述
        jobdesc = ','.join(jobdesc)
        jobaddr = response.xpath('//div[@class="work_addr"]/a/text()').extract()[:-1]  # 地址
        jobaddr = ','.join(jobaddr)
        company = response.xpath('//h2[@class="fl"]/em[@class="fl-cn"]/text()').extract()[0].strip()  # 公司
        item = LagoudemoItem()
        item["pname"] = pname
        item["money"] = money
        item["location"] = location
        item["year"] = year
        item["degree"] = degree
        item["ptype"] = ptype
        item["tags"] = tags
        item["date_pub"] = date_pub
        item["advantage"] = advantage
        item["jobdesc"] = jobdesc
        item["jobaddr"] = jobaddr
        item["company"] = company
        item['startmoney'] = startmoney
        item['endmoney'] = endmoney
        yield item