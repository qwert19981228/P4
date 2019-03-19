# 定义一个进程用于向queue当中写消息
# 定义一个进程用于向queue当中读消息

from multiprocessing import Process,Manager,Pool
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
    q = Manager().Queue()
    # 创建进程池
    po = Pool()
    # 创建线程
    pw =po.apply_async(func=write,args=(q,))
    pr = po.apply_async(func=read,args=(q,))

    po.close()
    po.join()
