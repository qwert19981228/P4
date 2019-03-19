import gevent
from gevent import monkey
import time
# 补丁  替换系统的默认库
monkey.patch_all()

def foo(i):
    time.sleep(4)
    print(i)

if __name__ == '__main__':
    start = time.time()
    g_list = []
    for i in range(10):
        g = gevent.spawn(foo,i)
        g_list.append(g)

    gevent.joinall(g_list)
    print('代码结束,耗时%s'%(time.time()-start,))
