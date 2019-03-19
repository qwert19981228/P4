from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.chrome.options import  Options
import time
from jd.settings import User_Agent
import random
import scrapy
class PhantomjsMiddleware(object):
    def __init__(self):
        # 浏览器配置
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        # 实例化浏览器
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
    def process_request(self, request, spider):
        '''
        :param request:  请求对象
        :param spider:   爬虫程序
        :return:
        '''
        # 判断当前的请求需要不需要selenium
        if request.meta.get('selenium',None):
            self.browser.get(request.url)
            time.sleep(1)
            #控制滚动条滚动
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)
            html = self.browser.page_source

            return HtmlResponse(url=request.url,encoding='utf-8',body=html,request=request)



    def __del__(self):
        self.browser.quit()



class MyUserAngent(object):
    def process_request(self,request,spider):
        request.headers['User-Agent']=random.choice(User_Agent)


