from queue import Queue

q = Queue(3)

q.put('1')
q.put('2')
print(q.full())
q.put('3')
print(q.full())
# q.put('4')

print(q.get())
print(q.get())
print(q.empty())
print(q.get())
print(q.empty())  # 如果为空了 就是true
