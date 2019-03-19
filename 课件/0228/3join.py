import threading
import time,random
def download(filename):
    print('开始下载%s'%filename)
    time.sleep(random.random()*10)
    print('下载完成%s' % filename)

if __name__ == '__main__':
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=download,args=(i,))
        t.start()
        thread_list.append(t)

    print(thread_list)

    for i in thread_list:
        i.join()

    print('全部下载完成')