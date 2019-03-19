from multiprocessing import Process
import os,time
def download(url,name):
    print('开启一个下载进程%s,下载%s'%(os.getpid(),url))
    print(name)
    time.sleep(10)
    print('下载结束..')

if __name__ == '__main__':
    # 创建进程
    p1 = Process(target=download,args=('怒晴湘西第-集',),kwargs={'name':'bablala'},name="狗蛋")
    print(p1.name)
    # 启动
    p1.start()