import threading
import time
def task1():
    time.sleep(3)
    print('我是写bug的')

def task2():
    time.sleep(3)
    print('我是修复上个项目的bug')


# 创建线程
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
# 启动线程
t1.start()
t2.start()
