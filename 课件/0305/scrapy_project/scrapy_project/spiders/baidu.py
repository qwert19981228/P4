import scrapy

class BaiduScrapy(scrapy.Spider):
    # 爬虫的名字
    name = 'baidu666'
    # 爬虫的任务
    start_urls = ['http://www.baidu.com']

    def parse(self,response):
        print(response.body.decode('utf-8'))
