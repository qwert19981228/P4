#//div[@id="content-left"]/div//h2   人名
# //div[@id="content-left"]/div//div[@class="content"]/span[1]  n内容

import requests
from lxml import etree
from urllib import request


def getPage():
    # 发送请求
    response = requests.get(base_url,headers=headers)
    html = etree.HTML(response.text)
    content_list = html.xpath('//div[@id="content-left"]/div')
    # 信息列表
    duanzi_info = []
    for div in content_list:
        name = div.xpath('.//h2/text()')[0]
        age = div.xpath('.//div[@class="articleGender manIcon"]/text() | .//div[@class="articleGender womenIcon"]/text()')
        # 判断是否有年龄
        if len(age):
            age = age[0]
        else:
            age = '100'
        # 性别
        sex = div.xpath('./div[1]/div/@class')
        if len(sex):
            if sex[0] == 'articleGender manIcon':
                sex = '男'
            else:
                sex = '女'
        else:
            sex = '妖'
        # 获取内容
        content = div.xpath('.//div[@class="content"]/span/text()')[0]
        # 获取图片
        img_url = div.xpath('./div[@class="thumb"]//img/@src')
        #判断有没有图片 如果有图片就下载
        if len(img_url):
            img_url = 'https:'+img_url[0]
            filename = img_url.split('/')[-1]
            request.urlretrieve(img_url,'./duanziimg/'+filename)
        else:
            img_url = ''
        # 好笑
        stats_vote = div.xpath('./div[@class="stats"]/span[@class="stats-vote"]/i/text()')[0]
        # 评论
        stats_omments = div.xpath('./div[@class ="stats"]/span[@ class ="stats-comments"]//i/text()')
        if len(stats_omments):
            stats_omments = stats_omments[0]
        else:
            stats_omments = 0
        data={
            'name':name.strip(),
            'age':age,
            'sex':sex,
            'content':content.strip(),
            'img_url':img_url,
            'stats_vote':stats_vote,
            'stats_omments':stats_omments
        }
        duanzi_info.append(data)

    return duanzi_info

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
    }
    base_url = "https://www.qiushibaike.com/hot/page/1/"
    duanzi_info =  getPage()
    print(duanzi_info)
