from multiprocessing import Queue

# 1.创建queue
q = Queue(3)

# 存消息
q.put('A')
q.put('B')
# q.full() 检测当前队列有没有满 满了返回True 没满返回false
# print(q.full())
# print(q.qsize())
q.put('C')

# if not q.full():
#     q.put('D',block=False)
# else:
#     print('已经满了')

# 设置等待时间 如果超过等待时间 队列还是满的 抛出异常
# q.put('D',timeout=3)

# 不会阻塞 如果满了强制添加 会抛出异常
# q.put_nowait('消息666')  # put(block=False)

# 读消息 get 会阻塞程序 ，如果消息队列当中内容已经没有了 就一直等待
print(q.get())
print(q.get())

print(q.get())

# 添加block 不会等待 会抛出异常 queue.Empty
if not q.empty():
    # print(q.get(block=False))
    print(q.get_nowait())
else:
    print('已经读完了。没有消息了')