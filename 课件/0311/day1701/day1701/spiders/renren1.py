# -*- coding: utf-8 -*-
import scrapy


class Renren1Spider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']
    login_url = 'http://www.renren.com/969685801'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        # "Cookie": "anonymid=jt3n4fonc6lpu5; depovince=BJ; jebecookies=50715c2c-8c6b-406c-8169-542fbe64d388|||||; _r01_=1; JSESSIONID=abcUhG_32Jju56fQbrQLw; ick_login=d37c590c-db2d-461e-91f8-a4e183a02262; _de=F8ACC661CB0C81B0D50364A326E8DA93; p=e0f455e0e9d0b5e050a018881d8af59e1; first_login_flag=1; ln_uact=17611593298; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=a5f22a6014882b081925b4b731b648cc1; societyguester=a5f22a6014882b081925b4b731b648cc1; id=969685801; xnsid=95bb4d71; ver=7.0; loginfrom=null; jebe_key=dc5e56c2-cb7d-4a51-923e-105be8556cb2%7Cd9baafb2d9acfdd31adc4a02a63486c3%7C1552266092460%7C1%7C1552266094161; wp_fold=0",
        "Host": "www.renren.com",
        "Referer": "http://www.renren.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    }
    cookies = {
        "anonymid": "jt3n4fonc6lpu5",
        "depovince": "BJ",
        "jebecookies": "50715c2c-8c6b-406c-8169-542fbe64d388|||||",
        "_r01_": "1",
        "JSESSIONID": "abcUhG_32Jju56fQbrQLw",
        "ick_login": "d37c590c-db2d-461e-91f8-a4e183a02262",
        "_de": "F8ACC661CB0C81B0D50364A326E8DA93",
        "p": "e0f455e0e9d0b5e050a018881d8af59e1",
        "first_login_flag": "1",
        "ln_uact": "17611593298",
        "ln_hurl": "http://head.xiaonei.com/photos/0/0/men_main.gif",
        "t": "a5f22a6014882b081925b4b731b648cc1",
        "societyguester": "a5f22a6014882b081925b4b731b648cc1",
        "id": "969685801",
        "xnsid": "95bb4d71",
        "ver": "7.0",
        " loginfrom": "null",
        " jebe_key": "dc5e56c2-cb7d-4a51-923e-105be8556cb2%7Cd9baafb2d9acfdd31adc4a02a63486c3%7C1552266092460%7C1%7C1552266094161",
        " wp_fold": "0",
    }
    def parse(self, response):
        yield scrapy.Request(url=self.login_url,callback=self.login_parse,headers=self.headers,cookies=self.cookies)

    def login_parse(self,response):
        print(response.text)
