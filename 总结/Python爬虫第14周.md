# 协程

### 作用

- 由代码进行调度
- 轻量级的线程 用户线程
- 协程的切换消耗资源更小 并发量可以更大

### 安装

##### 程序的切换

pip install greenlet

##### 协程

 pip install gevent



# JS正向过程

> 耗费资源 速度慢

selenium 测试工具

### 安装

pip install selenium==3.8

推荐使用ChromeDriver

PhanyomJs不好用

##### 安装两个驱动

chromeDriver的安装：

下载地址：<https://chromedriver.storage.googleapis.com/index.html>

PhantomJS安装地址：

下载地址：<http://phantomjs.org/download.html>

### 使用

##### 导包

```
from selenium import webdriver
```

##### 实例化浏览器

```
browser = webdriver.PhantomJS()/Chrome()
```

##### 访问网页

```
browser.get(URL地址)
```

##### 输入搜索内容

```
browser.find_element_by_id('id值').send_keys(“搜索的内容”)
```

##### 单机搜索

```
browser.find_element_by_id('id值').click()
```

##### 截图

```
browser.save_screenshop('图片名字‘)
```

##### 退出浏览器

```
browser.quit()
```

##### 设置 请求头信息

```
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
```



# Scrapy

### 安装

```
pip install Twisted
pip install Scrapy
pip install pywin32
```

### 流程图

![](.\Scrapy流程.png)

- Scheduler(调度器): 它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队（Queue），当引擎需要时，交还给引擎。
- Downloader（下载器）：负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理，
- Spider（爬虫）：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)，
- Item Pipeline(管道)：它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方.
- Downloader Middlewares（下载中间件）：你可以当作是一个可以自定义扩展下载功能的组件。
- Spider Middlewares（Spider中间件）：你可以理解为是一个可以自定扩展和操作引擎和Spider中间通信的功能组件（比如进入Spider的Responses;和从Spider出去的Requests）

### 步骤

- 新建项目 (scrapy startproject xxx)：新建一个新的爬虫项目
- 明确目标 （编写items.py）：明确你想要抓取的目标
- 制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
- 存储内容 （pipelines.py）：设计管道存储爬取内容
  - 创建项目 scrapy startproject demo
  - 启动项目 scrapy crawl  name
  - 创建爬虫 scrapy genspider name 域名



### 分页爬取

1. 对于URL地址可以拼接的网站

   ```python
    base_url = 'http://www.66ip.cn/%s.html'
    start_urls = []
    for url in range(1,5):
    	fullur = base_url % url
    	start_urls.append(fullur)
   ```

2. 对于不可以拼接的网站(获取下一页按钮的链接地址)

   ```python
   # 获取新的请求 并将请求发送给队列
   newurl = self.base_url + response.xpath('//div[@id="PageList"]/a[last()]/@href').extract()[0]
   # 将新的url提交到队列 callback 指定当前请求完成后由谁来解析 如果不指定默认由parse
   yield scrapy.Request(url=newurl,callback=self.parse)
   ```

   

### 获取详情

```python
# 创建详情页的请求(放在Parse()最后 即代替之前的 yield item)
yield scrapy.Request(url=url,callback=self.infoparse,meta={'data':item})
# 解析详情页的方法
def infoparse(self,response):
    item = TencentItem()
    # 获取所有的tr
   	# 写要获取详情页的xpath 并且join以下  ,例如:
    # duty = tr_list[2].xpath('./td//li/text()').extract()
    # duty = ''.join(duty)
    
    for key,value in response.meta['data'].items():
    	item[key] = value
    # 写 item键值 ,例如:
    # item['duty'] = duty
    yield item
```



### 添加selenium

![1551966423419](C:\Users\qwert\AppData\Roaming\Typora\typora-user-images\1551966423419.png)

如上图所示   基本上selenium都这么加

### 添加请求头

![1551966525092](C:\Users\qwert\AppData\Roaming\Typora\typora-user-images\1551966525092.png)

![1551966546203](C:\Users\qwert\AppData\Roaming\Typora\typora-user-images\1551966546203.png)

![1551966565834](C:\Users\qwert\AppData\Roaming\Typora\typora-user-images\1551966565834.png)

- 第一张图为 setting 里的数据  先在里面添加user-agent池

  必须要加中间件

- 第二张图为 中间件 里的数据  自定义一个类，随机获取请求头

- 第三张图为 爬虫文件 设置 headers



### 添加代理

1. 普通代理的切换

   在settings 中头添加

   ```
   PROXIEX = [
   {‘host’:'http://ip:port'}
   ...
   ]
   ```

   在中间件中创建随机代理的中间建

   ```
   class RandomProxy(object):
   	def __init__(self,cralwer):
   		self.cralwer = cralwer
   	def from_cralwer(cls,cralwer):
   		return cls(cralwer)
   
   	def process_request(self,request,spider):
   		# 获取代理
   		proxies = self.cralwer.settings['PROXIES']
   		proxy = random.chice(proxies)
   
   		request.meta = proxy['host'] 
   ```

   开启配置文件中的配置信息

2. 认证代理的使用

     配置文件中添加

   ```
   AUTH_PROXIES = [
   	{‘host’:'http://ip:port','auth':'用户名：密码'}
   ]
   ```

   添加中间建

   ```
   import base64
      class RandomProxy(object):
      def __init__(self,cralwer):
          self.cralwer = cralwer
      def from_cralwer(cls,cralwer):
          return cls(cralwer)
               
      def process_request(self,request,spider):
      		# 获取代理
      		auth_proxies = self.cralwer.settings['AUTH_PROXIES']
      		proxy = random.choice(proxies)
   
   # 设置用户名和密码（用户名密码）  这里需要用到base64下的b4encode(bytes())
   		auth = proxy['auth']
   		auth = base64.b64encode(bytes(auth,''utf-8)).
   		request.headers['Proxy-Authorization'] = b'Basic' + auth
   
   		# 设置代理ip和端口号
   		request.meta['proxy'] = proxy['host'] 
   ```

3. 随机获取代理

   ```
   在中间件中
   from py04_spider_day14.utils import mydb
   
   class RandomProxy(object):
       def __init__(self, cralwer):
           self.crawler = cralwer
           mysql = cralwer.settings['MYSQL_INFO']
           self.mysql = mydb.Mydb(mysql['MYSQL_HOST'], mysql['MYSQL_USER'], mysql['MYSQL_PASS'], mysql['MYSQL_DB'])
   
       @classmethod
       def from_crawler(cls, cralwer):
           return cls(cralwer)
   
       def process_request(self,request,spider):
           res = self.mysql.query('select * from proxy ORDER BY rand() limit 1')
           proxy = res[0]
           proxy = 'http://' + proxy['host'] + ':' + str(proxy['port'])
           request.meta['proxy'] = proxy
   ```

   