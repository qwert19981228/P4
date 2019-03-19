from multiprocessing import Process

def leijia(num):
    sum=0
    for i in range(1,int(num)+1):
        sum+=i
    print('%s的累加和'%num,sum)

class JieCheng(Process):
    def __init__(self,num):
        Process.__init__(self)
        self.jiecheng = 1
        self.num=num

    def run(self):
        for i in range(1,int(self.num)+1):
            self.jiecheng = self.jiecheng*i
        print('阶乘',self.jiecheng)

if __name__ == '__main__':
    num = input('计算：')
    # 计算累加和
    p1 = Process(target=leijia,args=(num,))
    # 结算阶乘
    p2 = JieCheng(num)

    # 启动进程
    p1.start()
    p2.start()
