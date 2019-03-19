```python
1.简述说明scrapy的基本机构流程
    1. 在创建好scrapy项目后，spider需要有初始的start_url 或者start_requests()，之后会在内部生成request到Engine；
    2. Engine将初始的Request发送给Scheduler，Engine也会从Scheduler中获取request，以便提交给Downloader下载页面；
    3. 之后Engine会向Scheduler进行请求一下个需要爬取的url；
    4. 如果Engine将url 发送给Downloader进行下载，这个过程会经过DownloaderMiddleware，此时会通过函数process_request()进行request处理
    5. Downloader在下载页面之后，生成response并返回给Engine，这个过程同样会经过DownloaderMiddleware，此时会通过process_response()进行response处理，如果出现错误异常，则会经过process_exception()进行错误处理；
    6. Engine在从Downloader接收到Response返回给spider，整个过程会经过SpiderMiddleware，在处理过程中response通过process_spider_input()进行处理；
    7. Spider处理response时，会有两种情况，获取新的request给Engine，或者返回item到Engine，两种情况下都会从SpiderMiddleware下经过process_spider_output()，再出现错误异常的时候回经过process_spider_exception()进行处理；
    8. Engine将Spider返回的item给到Item Pipeline进行处理，如果是新的request，则继续返回给Scheduler；
    9. 重复直到Scheduler不再产生新的request，此时Engine关闭，程序执行结束。
```

```python
2.scrapy分为哪几个组成部分?分别有什么作用?
答案:
	Spiders(爬虫类): Spiders是开发者自定义的一个类，用于解析相应并提取item或下个爬取的URL

	Scrapy Engine(引擎): Engine负责控制数据流在系统中的流动走向，并在指定条件下触发一些事件。同时，也可以简单理解为Scrapy中数据流的中转站

	Scheduler(调度器): Scheduler接收Engine发出的requests，并将这些requests放入到处理队列中，以便之后Engine需要时再提供

	Downloader(下载器): Downloader负责抓取网页信息并提供给Engine，进而转发至Spider

	Item Pipeline(处理管道): Item Pipeline负责处理Spiders类处理提取之后的item，典型的处理有数据清洗，验证以及持久化
```

```python
3.写出下面a,b,c,d四个变量的值
	import copy 
	a = [1,2,3,4,['a','b']]  # 原始对象
	b = a
	c = copy.copy(a)
	d = copy.deepcopy(a)
	a.append(5)
	a[4].append('c')
	print('a的值是',a)
	print('b的值是',b)
	print('c的值是',c)
	print('d的值是',d)
答案: 
a的值是 [1, 2, 3, 4, ['a', 'b', 'c'], 5]
b的值是 [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c的值是 [1, 2, 3, 4, ['a', 'b', 'c']]
d的值是 [1, 2, 3, 4, ['a', 'b']]
```

```python
4.1 * 2 . . . * 2014 的结果末尾有多少个0？请写出解题思路或者计算过程
    因数5的个数决定末尾0的个数
    2014÷5=402（取整）
    2014÷25=80（取整）
    2014÷125=16（取整）
    2014÷625=3（取整）
    402+80+16+3=501
    所以1*2*3*……*2012*2014的计算结果的末尾有501个连续的0
```

