from multiprocessing import Pool,Manager
import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}

def getInfo(url,q):
    print('开启进程下载%s'%url)
    # 发送请求
    response = requests.get(url,headers=headers)
    # 验证状态码
    if response.status_code == 200:
        html = BeautifulSoup(response.text,'lxml')
        tr_list = html.select('table.tablelist tr')[1:-1]
        for tr in tr_list:
            td_list = tr.select('td')
            job_name = td_list[0].a.text
            print(job_name)

            #将结果写入到queue
            q.put(job_name)
            print('下载%s完成------------'%url)
    else:
        print('%s下载失败￥￥￥￥￥￥￥￥'%url)


if __name__ == '__main__':
    # 记录开始时间
    start = time.time()

    # 创建进程池
    po = Pool(20)
    # 实例化queue
    q = Manager().Queue()

    base_url = 'https://hr.tencent.com/position.php?&start=%d'
    url_list = [ base_url % i for i in range(0,201,10)]

    # 一页就是一个进程
    for url in url_list:
        po.apply_async(func=getInfo,args=(url,q))
    po.close()
    po.join()

    # 判断q中还有没有数据 如果有就循环读取
    while not q.empty():
        print(q.get())

    end = time.time()-start
    print('数据提取完成耗时%s'%end)




