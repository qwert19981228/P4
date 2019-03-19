from threading import Thread

class MyThread(Thread):
    def run(self):
        print('当前进程的名字是%s'%self.name)

for i in range(5):
    t = MyThread(name='666')
    t.start()