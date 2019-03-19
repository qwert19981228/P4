from multiprocessing import Process
import os,time
class Process_class(Process):
    #初始化
    def __init__(self,timeOut):
        # 先去初始化父类 调用父类的__init__()方法
        Process.__init__(self)
        self.timeOut = timeOut

    def run(self):
        print('开启了一个进程',os.getpid())
        time.sleep(self.timeOut)
        print('进程执行结束-----------')

if __name__ == '__main__':
    # 实例化自定义类
    p1 = Process_class(3)
    p1.start()
    p1.join()
    print('程序执行结束')