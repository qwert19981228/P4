import requests
from lxml import etree
from urllib import request
import time
import json
headers = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
   "Accept-Encoding": "gzip, deflate",
   "Accept-Language": "zh-CN,zh;q=0.9",
   "Cache-Control": "max-age=0",
   "Cookie": "yd_cookie=793ea1da-e591-48d08d6641fb1c3ec0a4f15e08420d38d96a; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1550645662,1550650610,1550708950,1550799866; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1550800168",
   "Host": "www.66ip.cn",
   "Proxy-Authorization": "Basic YWxpY2U6MTIzNDU2",
   "Proxy-Connection": "keep-alive",
   "Referer": "http://www.66ip.cn/areaindex_1/1.html",
   "Upgrade-Insecure-Requests": "1",
   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
}


# 获取所有的地区的href
def getIndex():
   base_url="http://www.66ip.cn/"
   response = requests.get(base_url,headers=headers)
   response.encoding='gbk'
   text = response.text

   html = etree.HTML(text)

   res = html.xpath('//ul[@class="textlarge22"]/li/a/@href')
   getInfo(res)

# 进入帖子的详情页
def getInfo(url_list):
    datalist= []
    for i in url_list[1:]:
        time.sleep(1)
        newurl =  url_list[0]+i

        response = requests.get(newurl,headers=headers)
        response.encoding='gbk'
        text = response.text

        html = etree.HTML(text)
        res = html.xpath('//table[@bordercolor="#6699ff"]//td/text()')
        arr = []
        for i in range(0,len(res),5):
            arr.append(res[i:i+5])
        data = []
        for i in arr:
            dic = {}
            dic['ip']=i[0]
            dic['port']=i[1]
            data.append(dic)
        # for i in res[5::5]:
        #     print(i)
        datalist+=data

    with open('./66ip.json','a+',encoding='utf-8') as f:
        f.write(json.dumps(datalist,indent=4,ensure_ascii=False))






if __name__ == '__main__':
    getIndex()