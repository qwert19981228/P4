# MongoDB

## 什么是MongoDB?

**MongoDB 是由C++语言编写的,是一个基于分布式文件存储的开源数据库系统**

**在高负载的情况下,添加更多的节点,可以保证服务器性能**

*它介于关系型数据库 和 非关系型数据库之间 但仍是非关系型数据库*

MongoDB旨在为WEB应用提供可扩展的高性能数据存储解决方案

MongoDB将数据存储为一个文档,数据结构由键值对组成. MongoDB文档类似于JSON对象. 字段值可以包含其他文档,数组及文档数组



## MongoDB特点

- MongoDB是一个面向文档存储的数据库,操作起来比较简单和容易
- 可以在MongoDB记录中设置任何属性的索引来实现更快的排序
- 可以通过本地或者网络创建数据镜像,这使得MongoDB有更强的扩展性
- 如果负载的增加,它可以分布在计算机网络中的其他节点上这就是所谓的分片
- MongoDB支持丰富的查询表达式. 查询指令使用JSON形式的标记,可轻易查询文档中内嵌的对象及数组
- MongoDB使用update()命令可以实现替换完成的文档(数据)或者一些指定的数据字段
- MongoDB中的 Map/Reduce 主要是用来对数据进行批量处理和聚合操作
- Map和Reduce. Map函数调用emit(key,value)遍历集合中所有的记录,将key与value传给Reduce函数进行处理
- Map函数和Reduce函数是使用JavaScript编写的, 并可以通过db.runCommand或mapreduce命令来执行MapReduce操作
- GridFS是MongoDB中的一个内置功能,可以用于存放大量小文件
- MongoDB允许在服务端执行脚本,可以用JavaScript编写某个函数,直接在服务端执行,也可以把函数的定义存储在服务端,下次直接调用即可
- MongoDB支持各种编程语言:Ruby, Python, Java, PHP, C#等多种语言
- MongoDB安装简单



## MongoDB适用场景

- 网站数据: MongoDB 非常适合实时的插入,更新与查询,并具备网站实时数据存储所需的复制及高度伸缩性
- 缓存: 由于性能很高, MongoDB 也适合作为信息基础设施的缓存层,在系统重启之后,由MongoDB搭建的持久化缓存层可以避免下层的数据源过载
- 大尺寸、低价值的数据: 使用传统的关系型数据库存储一些数据时可能会比较昂贵,在此之前,很多时候往往会选择传统的文件进行存储
- 高伸缩性的场景: MongoDB非常适合由数十或数百台服务器组成的数据库, MongoDB的路线图中已经包含对MapReduce引擎的内置支持
- 用于对象及JSON数据的存储: MongoDB的BSON数据格式非常适合文档化格式的存储及查询





## MongoDB常用命令

### MongoDB 连接

1. 启动服务
2. 使用默认端口来连接**MongoDB**的服务

```linux
$ mongo
MongoDB shell version: 3.0.6
connecting to: test
... 
```

使用用户名和密码连接登陆到指定数据库

```
mongodb://admin:123456@localhost/test
```



### MongoDB 创建数据库

**创建数据库**

```
use 数据库名
```

如果数据库不存在,则创建数据库,否则切换到指定数据库

**查看所有数据库**

```
show dbs
```

**注意点**

- 刚创建的数据库并不存在数据库的列表中,要显示它,我们需要向新的数据库插入一些数据
- MongoDB 中默认的数据库为 test，如果你没有创建新的数据库，集合将存放在 test 数据库中
- 在 MongoDB 中，集合只有在内容插入后才会创建! 就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建



### MongoDB 删除数据库

**删除数据库**

```
db.dropDatabase()
```

删除当前数据库，默认为 test，你可以使用 db 命令查看当前数据库名



### MongoDB 创建集合

**创建集合**

```
db.createCollection(name, options)
```

**参数说明**

**name**: 要创建的集合名称 

**options**: 可选参数, 指定有关内存大小及索引的选项 

| 字段        | 类型 |                             描述                             |
| ----------- | ---- | :----------------------------------------------------------: |
| capped      | 布尔 | 如果为 true,则创建固定集合.固定集合是指有着固定大小的集合,当达到最大值时,它会自动覆盖最早的文档.当该值为 true 时,必须指定 size 参数 |
| autoIndexId | 布尔 |        如为 true,自动在 _id 字段创建索引.默认为 false        |
| size        | 数值 | 为固定集合指定一个最大值(以字节计),如果 capped 为 true,也需要指定该字段 |
| max         | 数值 |               指定固定集合中包含文档的最大数量               |

在插入文档时,MongoDB 首先检查固定集合的 size 字段，然后检查 max 字段

如果要查看已有集合，可以使用 show collections 命令

```
show collections 
```

在 MongoDB 中，你不需要创建集合。当你插入一些文档时，MongoDB 会自动创建集合。



### MongoDB 删除集合

**删除集合**

```
db.collection.drop()
```

如果成功删除选定集合，则 drop() 方法返回 true，否则返回 false。



### MongoDB 插入文档

**插入文档**

```
db.COLLECTION_NAME.insert(document)
```

如果该集合不在该数据库中， MongoDB 会自动创建该集合并插入文档。

我们也可以将数据定义为一个变量，如下所示：

```
> document=(
{	title: 'MongoDB 教程', 
    description: 'MongoDB 是一个 Nosql 数据库',
    by: 'boke',
    url: 'http://www.runoob.com',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 100
});
```

 **save插入**

插入文档你也可以使用 db.col.save(document) 命令。如果不指定 _id 字段 save() 方法类似于 insert() 方法。如果指定 _id 字段，则会更新该 _id 的数据。



### MongoDB 更新文档

#### update() 方法

```
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)
```

##### 参数说明

- query : update的查询条件，类似sql update查询内where后面的。
- update : update的对象和一些更新的操作符（如,,inc…）等，也可以理解为sql update查询内set后面的
- upsert : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。
- multi : 可选，mongodb - 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。
- writeConcern :可选，抛出异常的级别。

##### 修改多条语句(multi 参数为 true)

如果你要修改多条相同的文档，则需要设置 multi 参数为 true。



#### save() 方法

```
db.collection.save(
   <document>,
   {
     writeConcern: <document>
   }
)
```

##### 参数说明

- document : 文档数据。 
- writeConcern :可选，抛出异常的级别。



### MongoDB 删除文档

#### remove() 方法

```
db.collection.remove(
   <query>,
   {
     justOne: <boolean>,
     writeConcern: <document>
   }
)
```

##### 参数说明

- query :（可选）删除的文档的条件。 
- justOne : （可选）如果设为 true 或 1，则只删除一个文档，如果不设置该参数，或使用默认值 false，则删除所有匹配条件的文档。 
- writeConcern :（可选）抛出异常的级别。



### MongoDB 查询文档

**查询文档**

```
db.collection.find(query, projection)
```

##### 参数说明

- query ：可选，使用查询操作符指定查询条件 
- projection ：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）。

如果你需要以易读的方式来读取数据，可以使用 pretty() 方法

```
>db.col.find().pretty()
```



### MongoDB AND 条件

#### 格式

```
>db.col.find({key1:value1, key2:value2}).pretty()
```



### MongoDB OR 条件

#### 格式

```
>db.col.find(
   {
      $or: [
         {key1: value1}, {key2:value2}
      ]
   }
).pretty()
```



### MongoDB 条件操作符

(>) 大于 -- gt

(<)小于 -- lt 
(>=) 大于等于 -- gte

(<=)小于等于 -- lte



# 网络

## 网络简介

### 什么是网络

网络是辅助双方能够连接在一起的工具

### 为什么要用网络

为了联通多方然后进行通讯，能够让软件在不同的电脑上运行，相互传输数据



## 网络协议

### 什么是协议

约定俗成的，没有理由

### 网络模型

实际应用四层模型

- 链路层/网络接口层
- 网络层
- 传输层
- 应用层

理论七层网络模型

- 物理层
- 数据链路层
- 网络层
- 传输层
- 会话层
- 表示层
- 应用层



## IP

### 什么是地址

地址是用来标记地点的

**127.0.0.1代表本机**



## 端口

### 端口号

端口号是通过端口来标记的，范围是从0-65535

### 知名端口

知名端口是众所周知的端口号，一般是从0-1023

80分配给HTTP服务

21分配给FTP服务

### 动态端口

- 动态端口的范围一般是从1024到65535
- 之所以称之为动态端口，是因为它一般不固定分配某种服务，而是动态分配



## UDP和TCP

### UDP的特点

安全性差，传输速度快，无序，大小有限制64kb

### TCP的特点

- 安全性高，稳定性好，有序
- 速度相对较慢

### 三次握手的过程

![](.\三次握手.png)

ACK：确认标志

SYN：同步标志

第一次握手：主机A发送位码为syn＝1,随机产生seq number=1234567的数据包到服务器，主机B由SYN=1知道，A要求建立联机；  

第二次握手：主机B收到请求后要确认联机信息，向A发送ack number=(主机A的seq+1),syn=1,ack=1,随机产生seq=7654321的包  

第三次握手：主机A收到后检查ack number是否正确，即第一次发送的seq number+1,以及位码ack是否为1，若正确，主机A会再发送ack number=(主机B的seq+1),ack=1，主机B收到后确认seq值与ack=1则连接建立成功。  

完成三次握手，主机A与主机B开始传送数据。

## Python实现UDP和TCP的通讯

![UDP](.\UDP.png)

**服务端：**

1. 创建套接字对象
2. 绑定ip地址和端口号
3. 接受消息
4. 返回消息
5. 关闭套接字

**客户端:**

1. 创建套接字对象
2. 发送消息
3. 关闭套接字对象



![](.\TCP.png)

**服务端：**

1. 创建套接字对象
2. 绑定ip地址和端口号
3. 监听
4. 接受消息
5. 返回消息
6. 关闭套接字

**客户端：**

1. 创建套接字对象
2. 创建连接
3. 发送消息
4. 关闭套接字对象



## HTTP协议

### 什么是HTTP协议

**HTTP协议**主要工作在客户端-服务端的架构上，浏览器作为HTTP客户端通过URL向HTTP服务端即 WEB服务器发送请求，服务器根据接受到的请求，向客户端发送相应信息 **超文本传输协议**

### URL

URL即统一资源定位符(Uniform Resource Locator)，用来唯一地标识万维网中的某一个文档

### 特性

#### 无状态性

是指同一个客户端(浏览器)第二次访问同一个Web服务器上的页面时，服务器无法知 道这个客户曾经访问过

### 连接方式

1. 非持久性连接 
2. 持久性连接

### HTTP的基本原理

![img](https://note.youdao.com/yws/public/resource/e5b454028777eea520adb980ed82203e/xmlnote/WEB587ba75b57487019b6a002c90a46c3a8/WEBRESOURCEb3c8744e30bbc207177c21db7d5652f1/1767)

### URL的请求过程

1. 浏览器分析超链接中的URL
2. 浏览器向DNS请求解析www.sxtyu.com的IP地址
3. DNS将解析出的IP地址202.2.16.21返回浏览器
4. 浏览器与服务器建立TCP连接(80端口)
5. 浏览器请求文档：GET /index.html(发送HTTP请求)
6. 服务器给出响应，将文档 index.html发送给浏览器
7. 释放TCP连接
8. 浏览器显示index.html中的内容

### HTTP报文的基本结构

![img](https://note.youdao.com/yws/public/resource/e5b454028777eea520adb980ed82203e/xmlnote/WEB587ba75b57487019b6a002c90a46c3a8/WEBRESOURCEe1ba37ca428cd77e9c2150860a465694/1776)

#### 请求报文

即从客户端(浏览器)向Web服务器发送的请求报文。报文的所有字段都是ASCII码。

#### 返回报文

即从Web服务器到客户机(浏览器)的应答。报文的所有字段都是ASCII码。



## 状态码

状态码(Status-Code)是响应报文状态行中包含的一个3位数字

- 1xx：指示信息--表示请求已接收，继续处理。
- 2xx：成功--表示请求已被成功接收、理解、接受。
- 3xx：重定向--要完成请求必须进行更进一步的操作。
- 4xx：客户端错误--请求有语法错误或请求无法实现。
- 5xx：服务器端错误--服务器未能实现合法的请求。



## HTTP代理

![img](https://note.youdao.com/yws/public/resource/e5b454028777eea520adb980ed82203e/xmlnote/WEB587ba75b57487019b6a002c90a46c3a8/WEBRESOURCE837cbd2d5c91df594666e5742ee056a2/1804)