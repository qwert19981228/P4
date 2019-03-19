from multiprocessing import Pool
import time,random
def task(num):
    print('启动了进程%s'%num)
    time.sleep(random.random()*3)
    print('%s进程已经结束'%num)

if __name__ == '__main__':
    # 1.创建进程池
    po = Pool(3)
    for i in range(11):
        # 向进程池发送请求 异步的方式 推荐使用异步  同步是applay()
        po.apply_async(func=task,args=(i,))
    # 关闭进程池  关闭进程池之后 不能再做添加
    po.close()
    # 等待进程池当中的所有进程结束  必须写在close后面
    po.join()
