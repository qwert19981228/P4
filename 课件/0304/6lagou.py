from selenium import webdriver
import time
from lxml import etree
browser = webdriver.Chrome()

def getPage():
    browser.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')
    time.sleep(1)
    text = browser.page_source
    # 第一页数据
    getInfo(text)

    while True:
        # 去单机下一页
        browser.find_element_by_css_selector('span[class="pager_next "]').click()
        time.sleep(3)
        text = browser.page_source
        getInfo(text)

        # 判断是否到了最后一页
        if 'pager_next_disabled' in text:
            break


def getInfo(text):
    html = etree.HTML(text)
    # li_list
    li_list = html.xpath('//ul[@class="item_con_list"]/li')
    for item in li_list:
        job_name = item.xpath('.//h3/text()')[0]
        job_position = item.xpath('.//span[@class="add"]/em/text()')[0]
        print(job_name,job_position)

if __name__ == '__main__':
    getPage()
    browser.quit()


