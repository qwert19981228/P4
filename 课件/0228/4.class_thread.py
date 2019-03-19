import threading
import time,random

class MyThread(threading.Thread):
    def __init__(self,num):
        # threading.Thread.__init__(self)
        super(MyThread,self).__init__()
        self.num = num
    def run(self):
        print('开启了一个子线程进行下载%s'%self.num)
        time.sleep(random.random()*5)
        print('下载完成%s。。。'%self.num)

if __name__ == '__main__':
    for i in range(3):
        t = MyThread(i)
        t.start()
