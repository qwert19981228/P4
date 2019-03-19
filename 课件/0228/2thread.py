import threading
import time,random
def download(filename):
    print('开始下载%s'%filename)
    time.sleep(random.random()*10)
    print('下载完成%s' % filename)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=download,args=(i,))
        t.start()
    while True:
        length = len(threading.enumerate())
        if length==1:
            break
    print('全部下载完成')
