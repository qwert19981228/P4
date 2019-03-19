import os

# 开启一个新的进程(子进程)
pid = os.fork()

print(pid)
if pid == 0:
    print('我是子进程')
else:
    print('我是主进程')