import threading
import requests
from queue import Queue
from bs4 import BeautifulSoup
import time


class MyThread(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
    }
    def __init__(self,url_q,data_q,num):
        super(MyThread,self).__init__()
        self.url_q = url_q
        self.data_q = data_q
        self.num = num
        print('%d号线程开始采集数据'%self.num)


    def run(self):
        while not self.url_q.empty():
            url=self.url_q.get()
            response = requests.get(url,headers=self.headers)
            # 验证状态码
            if response.status_code == 200:
                html = BeautifulSoup(response.text, 'lxml')
                tr_list = html.select('table.tablelist tr')[1:-1]
                for tr in tr_list:
                    td_list = tr.select('td')
                    job_name = td_list[0].a.text
                    # print(job_name)

                    # 将结果写入到queue
                    self.data_q.put(job_name)

            else:
                print('%s下载失败￥￥￥￥￥￥￥￥' % url)

            print('%s号线程下载%s完成------------' % (self.num, url))




if __name__ == '__main__':
    thread_num = input('请输入线程数：')

    base_url = 'https://hr.tencent.com/position.php?&start=%d'
    url_list = [base_url % i for i in range(0, 201, 10)]
    # 创建两个消息队列
    url_q = Queue()
    data_q = Queue()

    # 将url存入到queue
    for i in url_list:
        url_q.put(i)

    # 开启线程
    thread_list = []
    for i in range(int(thread_num)):
        t = MyThread(url_q,data_q,i)
        t.start()
        thread_list.append(t)

    # 等待线程结束
    for i in thread_list:
        i.join()

    # 读取数据
    while not data_q.empty():
        print(data_q.get())
