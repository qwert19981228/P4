# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from day1701.items import Day1701Item


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']

    custom_settings = {
        "DEFAULT_REQUEST_HEADERS" :{
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "_ga=GA1.2.1714103551.1547433909; user_trace_token=20190114104509-681bea39-17a6-11e9-adcf-525400f775ce; LGUID=20190114104509-681bef9a-17a6-11e9-adcf-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; WEBTJ-ID=20190304142911-169476456c4333-0e4ca5a04bc718-541f3415-1327104-169476456c591; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1551630897,1551680955; JSESSIONID=ABAAABAAADEAAFIF3102E151E3B7B42262674FE38A78647; _gat=1; _gid=GA1.2.451333058.1552274573; LGSID=20190311112250-f37b8e55-43ac-11e9-9117-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; SEARCH_ID=e8ba889864dd4afc9bc4bd716ec669d0; LGRID=20190311112614-6c889462-43ad-11e9-a1bf-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552274776",
            "Host": "www.lagou.com",
            "Referer": "https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
        }
    }
    rules = (
        # allow 正则 提取url连接的规则 LinkExtractor 如果什么都不写默认提取页面中所有a标签的连接
        # callback 回调函数 处理本次请求的页面解析
        # follow 默认为true 是否继续跟进url
        Rule(LinkExtractor(allow=r'/zhaopin/\w+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/jobs/\d+.html'), callback='parse_list', follow=False),
    )

    def parse_item(self, response):
       # print(response.url)
        pass

    def parse_list(self,response):
        pname = response.xpath('//div[@class="job-name"]/@title').extract()[0]  # 职位标题
        money = response.xpath('//span[@class="salary"]/text()').extract()[0]  # 薪资
        location = response.xpath('//dd[@class="job_request"]//span[2]/text()').extract()[0].replace('/','')  # 地址
        year = response.xpath('//dd[@class="job_request"]//span[3]/text()').extract()[0].replace('/','')  # 工作经验
        degree = response.xpath('//dd[@class="job_request"]//span[4]/text()').extract()[0].replace('/','')  # 学历
        ptype = response.xpath('//dd[@class="job_request"]//span[5]/text()').extract()[0].replace('\n','')  # 职位类型
        tags =  response.xpath('//ul[@class="position-label clearfix"]/li/text()').extract()
        # tags = ''.join(tags)

        date_pub = response.xpath('//p[@class="publish_time"]/text()').extract()[0].replace('\xa0','').strip()  # 发布日期
        advantage = response.xpath('//dd[@class="job-advantage"]/p/text()').extract()  # 职位诱惑
        advantage = ','.join(advantage)
        jobdesc = response.xpath('//div[@class="job-detail"]/p/text()').extract()  # 职位描述
        jobdesc = ','.join(jobdesc)
        jobaddr = response.xpath('//div[@class="work_addr"]/a/text()').extract()[:-1] # 地址
        jobaddr = ','.join(jobaddr)
        company = response.xpath('//h2[@class="fl"]/em[@class="fl-cn"]/text()').extract()[0].strip()  # 公司
        # company = ','.join(company)
        item=Day1701Item()
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
        yield item
        # print(pname,money,location,year,degree,ptype,tags,date_pub,advantage,jobdesc,jobaddr,company)