import requests
from lxml import etree
from urllib import request
# 请求贴吧列表页 帖子列表的连接
def getList():
    base_url = 'https://tieba.baidu.com/f?kw=%E9%BB%91%E4%B8%9D&pn='
    for p in range(0,50,50):
        newurl = base_url + str(p)
        # 发送请求
        response = requests.get(newurl)
        text = response.text
        html = etree.HTML(text)
        print(html)
        # res = html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]//a[@rel="noreferrer"]/@href')
        res = html.xpath('//a[@class="j_th_tit "]/@href')
        getInfo(res)


# 进入帖子的详情页
def getInfo(url_list):
    # 便利url的列表
    for i in url_list:
        newurl = 'https://tieba.baidu.com'+i
        # 发送请求
        response = requests.get(newurl)
        text = response.text

        html = etree.HTML(text)
        res = html.xpath('//img[@class="BDE_Image"]/@src')
        downimg(res)

# 下载图片
def downimg(img_url):
    if len(img_url):
        for i in img_url:
            filename = i.split('/')[-1]
            print('正在下载.......%s'%filename)
            request.urlretrieve(i,'./tieba/'+filename)

if __name__ == '__main__':
    getList()