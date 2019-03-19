# 跨平台
from multiprocessing import Process
import time
def task1():
    print('睡觉')
    time.sleep(5)

def task2():
    print('打呼噜')
    time.sleep(5)

if __name__ == '__main__': # 测试  主程序
    # start = time.time()
    # task1()
    # task2()
    # end = time.time()-start
    # print('睡觉打呼噜结束一共睡了%s时间'%end)

    start = time.time()
    # 创建进程
    p1 = Process(target=task1)
    p2 = Process(target=task2)
    # 启动进程
    p1.start()
    p2.start()
    # 等待进程 join()
    p1.join()
    p2.join()
    end = time.time()-start
    print('睡觉打呼噜结束一共睡了%s时间'%end)



