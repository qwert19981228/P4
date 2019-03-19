import os

num = 0

# 单进程
# def demo1():
#     global num
#     num+=1
#     print('demo1',num)
#
# def demo2():
#     global num
#     num+=1
#     print('demo2',num)
#
# if __name__ == '__main__':
#     demo1()
#     demo2()
#     print('最后的num',num)

# 多进程

pid = os.fork()

if pid == 0:
    num+=1
    print('我是子进程的num=%s'%num)
else:
    num += 1
    print('我是主进程的num=%s' % num)


