import threading,time

g_num = 0

def task1():
    global g_num
    time.sleep(1)
    g_num += 1
    print('task1',g_num)

def task2():
    global g_num
    time.sleep(1)
    g_num += 1
    print('task2',g_num)

if __name__ == '__main__':
    # task1()
    # task2()
    # print('结束的值',g_num)
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('主线程里的值',g_num)