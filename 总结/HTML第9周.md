## DOM

定义HTML 和 XML的访问标准

​	xml?

​		html 就是 标签属性, 显示数据

​			预定义好的

​		xml  就是 描述数据, 存储数据

​			自定义, 可以扩展



### DOM 节点

在html中所有的东西 都是节点

- 整个文档节点: document

- html元素节点: element

- html属性节点: attr

- html内容节点: text   (包含 空格)

- 注释节点: comment




### 节点关系

- 父节点

- 子节点

- 祖辈节点

- 后辈节点

- 同辈节点




### 节点访问

#### 方法

- getElementById( )

- getElementsByTagName( )

- getElementsByClassName( )

- getAttributeNode( )    获取属性节点

- getAttribute( )       获取属性值


#### 属性

- attributes    获取属性节点

- parentNode     获取父级节点

- childNodes     获取子级节点

- parentElement  获取父级元素

- children      获取子级元素




### 节点属性

#### nodeName

- 文档节点的 nodeName 始终都是 #document

- 元素节点的 nodeName 始终都是 标签名

- 属性节点的 nodeName 始终都是 属性名

- 内容节点的 nodeName 始终都是 #text


#### nodeValue

- 元素节点的 nodeValue 始终都是 null 就是 undefined

- 属性节点的 nodeValue 始终都是 属性值

- 内容节点的 nodeValue 始终都是 正文内容


#### nodeType

- document   	 9

- element          1

- attr                  2  

- text                  3

- comment        8




### 节点操作

#### 修改属性值

​	元素节点.setAttribute(属性名, 属性值)

​	元素节点.属性名 = '值'

#### 创建节点

​	属性: document.createAttribute('属性名');

​	元素: document.createElement('标签名');

#### 删除节点

​	属性:  removeAttribute() 

​		  或者 把值设置为null

​	元素:  removeChild(节点)   删除父节点的一个子节点

#### 替换节点

​	属性:  setAttribute(属性名, 属性值)

​	元素:  replaceChild(新节点,旧节点);

#### 插入节点

​	属性: setAttribute(属性名, 属性值)

​	元素: appendChild(node)            插入子节点

​		 insertBefore(新节点, 旧节点)   指定位置插入节点

#### 克隆节点

​	cloneNode()    

​		false(默认值)

​		true(全部复制)





## jQuery 框架

jQuery 只是JavaScript的一个轻量级框架

​	写得少, 干得多

优势:

- 开源
- 便捷的选择器
- 方便的DOM操作
- 动画操作
- 简化ajax
- 兼容性



### jQuery 安装

一般jq就两个版本

​	一个测试版, 用于测试, 有良好的代码排版

​	一个迷你版, 用于实际项目中, 已被精简和压缩

经典版本: jquery-1.8.3

最新版本: jquery-3.3.1 (至今 2019年1月)



### jQuery 基本语法

```
$(对象).操作(function(){
	代码块
})
```

### 简化写法

```
$(function(){
	代码块
});
```



## Ajax

> 简介:asyn javascript and xml   异步的 js 和 xml

同步: 发出一条指令后,在没得到结果前,就不能做其他事情 (事情一个一个做)

异步: 发出一条指令后,在没得到结果前,可以选做其他事     (事情分布式完成)

#### HTTP基本原理

##### ​	请求

​		客户端向服务器请求一个文件

##### ​	响应

​		服务器将文件内容返回给客户端,文件有了输出才算真正的响应

传统的请求 通过url地址栏 刷新请求

Ajax	    通过技术 偷偷的请求	

主要用于 在无刷新的情况下,局部改变数据

```html
$.ajax({
	url: 'py地址',
	type: '传输方式',
	data: {参数名1:参数值1,参数名2:参数值2,...},
	success:function(){
		响应成功后,功能代码块
	},
	error:function(){
		响应失败后,功能代码块
	}
})
```

#### 注意

​	url:ajax要传输的地址

​	type:默认get

​	data:常用json格式

​		也可以用"参数名1=参数值1&参数名2=参数值2& ..."

​	success:请求成功后的回调函数

​	error:请求失败后的回调函数

​	datatype:预期服务器返回的数据类型

#### 服务器

​	Apache

​	Nginx

​	IIS

​	Tomact

​	. . .

#### 常见状态码

​	200		成功响应

​	304		文件来自于缓存

​	404		文件不存在

​	500		服务器未知错误

​	503		服务器宕机(死机)或服务器不可用

​	2xx		成功...

​	4xx		客户端的问题

​	5xx		服务器的问题



## Bootstrap

1. 简介

   ​是一个前端框架

2. 作用

   常用于响应式布局,移动设备

3. 官方地址

   http://www.bootcss.com/

4. 下载安装

   https://v3.bootcss.com/getting-started/#download

5. BootStrap的结构

   css

   ​	bootstrap.css		学习版(良好的代码排版)

   ​	bootstrap.min.css	实际开发使用的版本,被压缩过的

   ​	bootstrap-theme.css	主题

   js	

   ​	基于jQ的js

   fonts 

   ​	字体图标

   免费主题模版

   ​	http://www.bootswatch.com

   

   


# 数据库


   1. 定义

       是按照数据结构来组织, 存储 和 管理数据的 仓库

       组成: 

       ​	库  database

       ​	表  table

       库中包含了 表

       表中包含了 数据

   2. 分类

      关系型数据库

      MySQL, SQLServer, Oracle ...

      优点:

      ​	保持数据的一致性

      ​	擅长做复杂数据查询

      ​	支持事务

      缺点:

      ​	读写性能比 非关系的差一点.  尤其是 海量数据的高效率读写

      ​	表结构固定, 不灵活

      非关系型数据库

      Redis, MongoDB, ...

      优点:

      ​	读写速度快

      ​	格式灵活

      ​	开源

      缺点:

      ​	表结构复杂, 导致复杂查询能力较弱

      ​	不支持事务


   3. 注释

       /* 多行注释 * /

        -- 单行

       #单行

        注意:

       ​	 单行注释符  与  注释内容 之间至少保留一个空格
   4. 基本语法

       命令大写, 自定义名字小写

       自定义名字 不能使用关键字

       每条命令 均已 分号结尾.




## 常见命令

1. 设置密码

   set password = password('密码')

2. 查看数据库

   show databases;    复数

3. 创建数据库

   create database ` 库名 `;

   create database if not exists ` 库名 `;

   create database if not exists ` 库名 ` default charset=编码;

   ​	注意:

   ​		1) 编码不要写成utf-8,  写成 utf8, 中间没有 "-".

   ​		2) if not exists 判断库若存在 , 则不创建

   ​						库若不存在, 则创建

   ​		3) 反引号 具有屏蔽关键字的作用. 

   ​		推荐:  库名, 表名, 字段名 最好都加上反引号

4. 删除数据库

   drop database `库名`;

5. 使用数据库

   use `库名`;

6. 查看数据表

   show tables;

7. 创建数据表

   create table if not exists `表名`(
        `字段名`  字段类型   字段属性,
        `字段名`  字段类型   字段属性,
       ...
        `字段名`  字段类型   字段属性    (最后一个字段的分号, 不能写)

   )engine=引擎 default charset=编码;

8. 删除数据表

   drop table `表名`;

9. 查看表结构

   desc `表名`;

10. 查看建表语句

    show create  table `表名`;