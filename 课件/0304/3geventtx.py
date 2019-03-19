import gevent
from gevent import monkey
import time
# 补丁  替换系统的默认库
monkey.patch_all()
from queue import Queue
import requests
from bs4 import BeautifulSoup
from models import Mydb
from threading import Lock
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}

def foo(task):
    # 判断是否为空
    while not task.empty():
        url = task.get()
        response = requests.get(url, headers=headers)
        # 验证状态码
        if response.status_code == 200:
            html = BeautifulSoup(response.text, 'lxml')
            tr_list = html.select('table.tablelist tr')[1:-1]
            for tr in tr_list:
                td_list = tr.select('td')
                job_name = td_list[0].a.text
                job_url = td_list[0].a.get('href')

                # 指定规则
                pat = re.compile('id=(\d+)')
                res  = pat.search(job_url)
                url_id = res.group(1)


                # 将结果写入到数据库
                sql = 'insert into user values(null,"%s",%d) on duplicate key update name = values(name)'%(job_name,int(url_id))

                exute.acquire(True)
                mydb.excute(sql)
                exute.release()



        else:
            print('%s下载失败￥￥￥￥￥￥￥￥' % url)

        print('线程下载%s完成------------' % (url))


if __name__ == '__main__':
    start = time.time()
    exute = Lock()
    mydb = Mydb(host="127.0.0.1",user="root",port=3306,database="py17",password="123456")
    base_url = 'https://hr.tencent.com/position.php?&start=%d'
    url_list = [base_url % i for i in range(0,10, 10)]
    task_q = Queue()
    for url in url_list:
        task_q.put(url)
    g_list = []
    for i in range(1):
        g = gevent.spawn(foo,task_q)
        g_list.append(g)

    gevent.joinall(g_list)
    print('代码结束,耗时%s'%(time.time()-start,))
