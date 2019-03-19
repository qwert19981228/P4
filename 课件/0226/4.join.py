from multiprocessing import Process
import time
def download():
    print('开启下载进程')
    time.sleep(5)

if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=download)
    p1.start()
    # join() 进程等待  等待子进程执行结束在继续执行
    # p1.join() # 一直等到子进程执行结束
    # p1.join(3) # 设置超时时间 只等待3秒钟，超过3秒不在等待
    # print(p1.is_alive())  # is_alive()  检测进程是否执行结束，如果结束返回false 没有结束返回true
    p1.join(10)  # 设置等待时间，最多等待10秒，如果10没有执行完就不在等待，如果10之内执行下结束，也不在等待
    end = time.time()-start
    # print('下载成功耗时%s'%end)
    print(p1.is_alive())

    # 设置等待时间为3秒  3秒之后检测进程是否执行结束，如果没有执行结束 强制关闭进程
    if p1.is_alive():
        p1.terminate()
        print('下载失败，请重新下载')
    else:
        print('下载成功')

