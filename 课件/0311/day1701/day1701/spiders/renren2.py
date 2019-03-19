# -*- coding: utf-8 -*-
import scrapy


class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']
    login_url = 'http://www.renren.com/PLogin.do'
    custom_settings = {
        "ITEM_PIPELINES":  { 'day1701.pipelines.Day1701Pipeline': 300,}
    }
    def parse(self, response):
        data = {
            'email':'17611593298',
            'password':'zhy123g123j'
        }
        yield scrapy.FormRequest(url=self.login_url,formdata=data,callback=self.parse_login)

    def parse_login(self,response):
        print(response.text)