import threading

g_list=[1,2,3]

def task1(newlist):
    print(newlist)
    newlist.append(4)
    print('task1',newlist)

def task2(newlist):
    print('task2',newlist)

if __name__ == '__main__':
    t1 = threading.Thread(target=task1,args=(g_list,))
    t2 = threading.Thread(target=task2,args=(g_list,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(g_list)