import threading

g_num = 0

def task1():
    global g_num
    for i in range(1000000):
        # 上锁
        mutexFlag = mutex.acquire(True)
        # 检测是否获得资源 如果得到  mutexFlag True
        if mutexFlag:
            g_num += 1
            # 释放锁
            mutex.release()
    print('task1',g_num)

def task2():
    global g_num
    for i in range(1000000):
        # True 如果资源已经被其他线程上锁，就会一直等（阻塞）到对方释放锁
        # False 不等待 直接继续执行下面的代码
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()
    print('task2',g_num)

if __name__ == '__main__':
    # 实例化锁
    mutex = threading.Lock()

    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(g_num)
