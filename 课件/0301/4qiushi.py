import threading
import requests
from queue import  Queue
from lxml import etree
from urllib import request
import json

class GetPage(threading.Thread):

    def __init__(self,task_q,data_q,headers):
        super(GetPage,self).__init__()
        self.task_q = task_q
        self.data_q = data_q
        self.headers= headers

    def run(self):
        while not self.task_q.empty():
            base_url = self.task_q.get()
            response = requests.get(base_url, headers=self.headers)
            if 200 <= response.status_code <300:
                self.data_q.put(response.text)
            else:
                print('%s请求失败'%base_url)

class Parse(threading.Thread):
    def __init__(self,data_q,get_list,f):
        super(Parse, self).__init__()
        self.data_q = data_q
        self.get_list = get_list
        self.flag = True
        self.f=f
    def run(self):
        while True:
            for i in self.get_list:
                # 判断只要有一个线程或者 或者 queue有内容就 取解析
                if i.is_alive() or not self.data_q.empty():
                    # 读取源代码
                    try:
                        html = self.data_q.get(timeout=3)
                        self._parse(html)
                    except:
                        html = None
                else:

                    self.flag = False
                    break

            # 判断标志位 如果为false 代表已经全部解析完成 结束循环
            if not self.flag:
                print('解析完成。。。。。')
                break

    def _parse(self,text):
        html = etree.HTML(text)
        content_list = html.xpath('//div[@id="content-left"]/div')
        # 信息列表

        for div in content_list:
            name = div.xpath('.//h2/text()')[0]
            age = div.xpath(
                './/div[@class="articleGender manIcon"]/text() | .//div[@class="articleGender womenIcon"]/text()')
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
            # 判断有没有图片 如果有图片就下载
            if len(img_url):
                img_url = 'https:' + img_url[0]
                filename = img_url.split('/')[-1]
                request.urlretrieve(img_url, './duanziimg/' + filename)
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
            data = {
                'name': name.strip(),
                'age': age,
                'sex': sex,
                'content': content.strip(),
                'img_url': img_url,
                'stats_vote': stats_vote,
                'stats_omments': stats_omments
            }
           # 写入文件
            self.f.write(json.dumps(data,ensure_ascii='utf-8')+'\n')





if __name__ == '__main__':

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
    }

    f = open('./qiushi.json','w',encoding='utf-8')

    task_q = Queue()
    data_q = Queue()

    base_url = "https://www.qiushibaike.com/hot/page/%d/"
    url_list=[base_url % i for i in range(1,3)]
    for i in url_list:
        task_q.put(i)
    thread_list = []
    for i in range(3):
        t = GetPage(task_q,data_q,headers)
        t.start()
        thread_list.append(t)

    parse_list=[]
    for i in range(3):
        t = Parse(data_q,thread_list,f)
        t.start()
        parse_list.append(t)


    for i in thread_list:
        i.join()

    for i in parse_list:
        i.join()

    f.close()


