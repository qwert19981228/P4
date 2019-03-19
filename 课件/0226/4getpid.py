import os

pid = os.fork()

if pid == 0:
    # 获取子进程的pid获取自己的pid
    print('启动子进程%s,父进程是%s'%(os.getpid(),os.getppid()))
else:
    print('主进程%s...,子进程是%s'%(os.getpid(),pid))
