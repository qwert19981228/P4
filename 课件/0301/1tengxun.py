# 导包
import threading
import requests
from queue import Queue
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}

def getPage(url,data_q):
    # 发送请求
    response = requests.get(url,headers=headers)
    # 解析页面
    # 验证状态码
    if response.status_code == 200:
        html = BeautifulSoup(response.text, 'lxml')
        tr_list = html.select('table.tablelist tr')[1:-1]
        for tr in tr_list:
            td_list = tr.select('td')
            job_name = td_list[0].a.text
            print(job_name)

            # 将结果写入到queue
            data_q.put(job_name)
            print('下载%s完成------------' % url)
    else:
        print('%s下载失败￥￥￥￥￥￥￥￥' % url)




if __name__ == '__main__':
    start = time.time()
    base_url = 'https://hr.tencent.com/position.php?&start=%d'
    url_list = [base_url % i for i in range(0, 201, 10)]
    data_q = Queue()
    # 开启线程取爬取
    thread_list=[]
    for url in url_list:
        t = threading.Thread(target=getPage,args=(url,data_q))
        t.start()
        thread_list.append(t)

    # 线程等待
    for i in thread_list:
        i.join()

    # 读取数据
    while not data_q.empty():
        print(data_q.get())

    end = time.time()-start
    print('耗时%s'%end)