from greenlet import greenlet

def foo1():
    print(12)
    g2.switch()
    print(34)
    g2.switch()

def foo2():
    print(56)
    g1.switch()
    print(78)

if __name__ == '__main__':
    g1 = greenlet(foo1)
    g2 = greenlet(foo2)


    g1.switch()