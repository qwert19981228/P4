# 进程

> 是为了解决多任务处理 并发



## 程序和进程之间的关系

1. 程序运行起来之后就是进程
2. 没有运行的时候就是代码
3. 进程的执行需要环境支持

## 进程的特点

- 进程和进程之间 完全独立 分别有自己的资源
- 多个进程是同时执行 没有顺序




## fork()

- 程序执行到os.fork()时，操作系统会创建一个新的进程（子进程）
- 然后复制父进程的所有信息到子进程中然后父进程和子进程都会从fork()函数得到一个返回值
- 在子进程中这个值一定是0，而父进程中是子进程的id号
- 子进程在复制父进程资源的时候，也将父进程的执行进程也复制过去了，所以子进程中的代码并非全部从头到尾执行。部从头到尾执行

### getpid()

os.getpid():当前进程ID

### getppid()

os.getppid():当前进程的父进程ID---parent:双亲，忽略性别（father,只是父的意思），这里用parent更严谨



> 多进程中，每个进程中所有数据（包括全局变量）都各有拥有一份，互不影响



## multiprocessing

### 创建格式

​	p=Process(target=函数名)

### 启动格式

​	进程对象名.start()

### 参数列表

​	Process([group[,target[,name[,args[,kwargs]]]]])

- target：表示这个进程实例所调用对象
- args：表示调用对象的位置参数元组
- kwargs：表示调用对象的关键字参数字典
- name：为当前进程实例的别名
- group：大多数情况下用不到

### join()

可以等待子进程结束后再继续往下运行（阻塞阻塞），通常用于进程间的同步。

join()			表示一直等

join(时间秒数)	表示具体阻塞几秒

### is_alive()

判断进程实例是否还在执行

### terminate()

不管任务是否完成，立即终止



## Pool

### 创建进程池

Pool(p)

p为指定的最大进程数

### 异步与同步

向进程池发送请求

异步是apply_async()  ----- 推荐

同步是apply()

### 关闭与等待

关闭进程池  关闭进程池之后不能再做添加

对象.close()

等待进程池当中的所有进程结束  必须写在close后面

对象.join()



## Queue

> 进程间通信-Queue

### 初始化Queue()对象

q=Queue()

若括号中没有指定最大可接收的消息数量，或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）

- Queue.qsize()：返回当前队列包含的消息数量
- Queue.empty()：如果队列为空，返回True，反之False
- Queue.full()：如果队列满了，返回True,反之False
- Queue.get([block[,timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True

> 1. 如果block使用默认值，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态），直到从消息列队读到消息为止，
> 2. 如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常
> 3. 如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常

- Queue.get_nowait()：相当Queue.get(False)；
- Queue.put(item,[block[,timeout]])：将item消息写入队列，block默认值为True；

> 1. 如果block使用默认值，且没有设置timeout（单位秒），消息列队如果已经没有空间可写入，此时程序将被阻塞（停在写入状态），直到从消息列队腾出空间为止，
> 2. 如果设置了timeout，则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；
> 3. 如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常

- Queue.put_nowait(item)：相当Queue.put(item,False)



### Manager

如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，而不是multiprocessing.Queue()，

否则会得到一条如下的错误信息RuntimeError:Queueobjectsshouldonlybesharedbetweenprocessesthroughinheritance



# 线程

## threading

多任务可以由多进程完成，也可以由一个进程内的多线程完成。
进程是由若干线程组成的，一个进程至少有一个线程。

### 线程执行代码的封装

- 通过使用threading模块能完成多任务的程序开发，
- 为了让每个线程的封装性更完美，
- 所以使用threading模块时，往往会定义一个新的子类class，
- 只要继承threading.Thread就可以了，然后重写run方法

### 线程的执行顺序

​	    启动			   调度                        结束

新建 ------------>> 就绪 <<-------------->> 运行 -------------->>死亡

​			       <----- 等待(阻塞)  <-------

​				满足		       等待

### 共享全局变量

- 在一个进程内的所有线程共享全局变量，能够在不适用其他方式的前提下完成多线程之间的数据共享（这点要比多进程要好）
- 线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全）

### 解决线程不安全

#### 方法 ---- 加锁

1. 实例化锁 mutex = threading.Lock()
2. 加锁 mutex.acquire([blocking])        blocking 为true阻塞 反之不阻塞
3. 释放锁 mutex.release()





# 多线程VS多进程

### 功能

- 进程，能够完成多任务，比如在一台电脑上能够同时运行多个QQ
- 线程，能够完成多任务，比如一个QQ中的多个聊天窗口

### 定义

- 进程是系统进行资源分配和调度的一个独立单位
- 线程是进程的一个实体，是CPU调度和分派的基本单位

### 区别

- 一个程序至少有一个进程，一个进程至少有一个线程
- 线程的划分尺度小于进程（资源比进程少），使得多线程程序的并发现高
- 进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率
- 线程不能够独立执行，必须依存在进程中

### 优缺点

线程执行开销小，但不利于资源的管理和保护，而进程正相反

#### 进程

- 定义：进程是系统进行资源分配的基本单位
- 提升代码的执行效率
- 进程开启个数：理论来说是cpu核心的1-2倍
- 使用场景：计算密集的应用
- 缺点：资源消耗较大，cpu切换进程时也会消耗资源，资源共享困难

#### 线程

- 定义: 一个进程中可以开启多个线程，多个线程共享当前进程的资源，系统（cpu）可调度的进本单位
- 提升代码的执行效率线
- 线程的开启个数：线程的可开启个数一定大于进程的可开启个数
- 应用场景：IO密集型应用
- 缺点：开启个数也是有一定限制的，如果开启过多的线程，或造成线程混乱，进程崩塌

