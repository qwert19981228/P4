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

``` linux
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