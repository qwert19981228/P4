# 定义一个进程用于向queue当中写消息
# 定义一个进程用于向queue当中读消息

from multiprocessing import Process,Queue
import time
def write(q):
    for i in ['A','B','C']:
        print('将消息%s写入到q'%i)
        q.put(i)


def read(q):
    while True:
        print('读取消息%s'%q.get())



if __name__ == '__main__':
    # 实例化queue
    q = Queue()
    # 创建线程
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()