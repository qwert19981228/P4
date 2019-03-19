import os,time


start = time.time()
pid = os.fork()
print('~~~~~')

ppid = os.fork()
print('!!!!')
time.sleep(3)

end = start-time.time()
print('执行的时间',end)
'''
进程和进程之间是相互独立
进程的执行是同时执行的 没有顺序
'''
