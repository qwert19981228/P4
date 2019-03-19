from selenium import webdriver
import time
from lxml import etree
from urllib import request
# 初始化浏览器
browser = webdriver.Chrome()
def getpage():
    # 发送请求
    browser.get('https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE%B4%F3%CD%BC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111')
    time.sleep(1)
    text = browser.page_source

    # 获取第一页数据
    getimg(text)
    browser.save_screenshot('美女.png')
    while True:
        # execute_script 执行js代码
        browser.execute_script('scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        browser.save_screenshot('美女2.png')
        text = browser.page_source
        # print(text)
        getimg(text)



def getimg(text):
    html = etree.HTML(text)
    img_li = html.xpath('//div[@id="imgid"]/div[@class="imgpage"][last()]//ul/li')
    print(img_li)
    for item in img_li:
        imgurl = item.xpath('.//img/@data-imgurl')[0]
        fname = imgurl.split('/')[-1]
        print(imgurl)
        # request.urlretrieve(imgurl,'./baiduimg/'+fname)

if __name__ == '__main__':
    getpage()


