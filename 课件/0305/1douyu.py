from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import time
from lxml import etree
chrome_options = Options()
chrome_options.add_argument('window-size=1920x1080')
# 实例化浏览器
browser = webdriver.Chrome(chrome_options=chrome_options)



def getpage():
    # 发送请求
    browser.get('https://www.douyu.com/directory/all')
    time.sleep(1)
    browser.find_element_by_css_selector('.ZoomTip-tipHide').click()

    # 获取源代码
    text = browser.page_source
    parse(text)
    while True:
        # 单击下一页 获取源码解析
        browser.find_element_by_css_selector('.dy-Pagination-next').click()
        time.sleep(0.5)
        text = browser.page_source
        parse(text)
       # 判断是不是最后一页
        if 'dy-Pagination-disabled' in text:
            break

def parse(text):
    html = etree.HTML(text)
    li_lit = html.xpath('//div[@class="layout-Module-container layout-Cover ListContent"]/ul[@class="layout-Cover-list"]/li')

    for li in li_lit:
        # 直播间名字
        name = li.xpath('.//h3/text()')[0]
        type = li.xpath('.//span[@class="DyListCover-zone"]/text()')[0]
        hot = li.xpath('.//span[@class="DyListCover-hot"]/text()')[0]
        user = li.xpath('.//h2/text()')[0]

        print(name,type,hot,user)

if __name__ == '__main__':
    getpage()




