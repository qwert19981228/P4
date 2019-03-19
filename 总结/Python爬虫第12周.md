# 爬虫

## 什么是爬虫

**抓取网络信息的应用程序**



## 数据来源

- 企业产生的用户数据
- 数据平台购买数据
- 政府/机构公开的数据
- 数据管理咨询公司
- 爬取网络数据



## 构建爬虫的步骤

1. 确定需求
2. 确定爬取目标   url地址
3. 构建http请求   发送请求
4. 处理响应结果  数据的格式化和存储



## 爬虫的难点 -- 反反爬

- 验证码
- 请求头
- 登录
- 代理
- 分布式爬取



## 遇到反爬机制怎么处理

1. 判断User-Agent
2. 判断Referer
3. 判断Cookie

如果以上操作还是没有成功爬取页面，就用将浏览器中的全部头信息放进来

注意:如果把全部headers拿过来的话记得把Accept-Encoding: gzip, deflate注释掉



## Http与Https的区别

- HTTP 的URL 以http:// 开头，而HTTPS 的URL 以https:// 开头
- HTTP 是不安全的，而 HTTPS 是安全的
- HTTP 标准端口是80 ，而 HTTPS 的标准端口是443
- 在OSI 网络模型中，HTTP工作于应用层，而HTTPS 的安全传输机制工作在传输层
- HTTP 无法加密，而HTTPS 对传输的数据进行加密
- HTTP无需证书，而HTTPS 需要CA机构颁发的SSL证书
- HTTP全称是Hyper  Text  Transfer Protocol,中文全称为超文本
- HTTPS全称是Hyper Text  Transfer Protocol over Secure Socket Layer,也就是说比HTTP多了安全层,通俗的讲来说就是HTTP的安全版



## urllib和urllib2的区别

- urllib 和urllib2都是接受URL请求的相关模块，但是urllib2可以接受一个Request类的实例来设置URL请求的headers，urllib仅可以接受URL。
- urllib不可以伪装你的User-Agent字符串。
- urllib提供urlencode()方法用来GET查询字符串的产生，而urllib2没有。这是为何urllib常和urllib2一起使用的原因。

Python3中 urllib2  变为urllib.request



## 常见的页面数据抽取方式

- xpath
- beautifulsoup4

- re

- jsonpath



## 反爬虫策略以及解决方法	

### 反爬虫策略

1. 通过headers反爬虫
2. 基于用户行为的反爬虫：(同一IP短时间内访问的频率)
3. 动态网页反爬虫(通过ajax请求数据，或者通过JavaScript生成)
4. 对部分数据进行加密处理的(数据是乱码)

### 解决方法

1. 对于基本网页的抓取可以自定义headers,添加headers的数据
2. 使用多个代理ip进行抓取或者设置抓取的频率降低一些，
3. 动态网页的可以使用selenium + phantomjs 进行抓取
4. 对部分数据进行加密的，可以使用selenium进行截图，使用python自带的pytesseract库进行识别，但是比较慢最直接的方法是找到加密的方法进行逆向推理。



## 常用的HTTP方法

- ★GET： 请求页面,并返回内容
- ★POST：大多用于提交表单或上传文件,数据包含在请求体中
- PUT： 传输文件，报文主体中包含文件内容，保存到对应URI位置。
- HEAD： 获得报文首部，与GET方法类似，只是不返回报文主体，一般用于验证URI是否有效。
- DELETE：请求服务器删除指定的页面,与PUT方法相反
- CONNECT:把服务器当做跳板,让服务器代替客户端访问其他网页
- OPTIONS：循序客户端查看服务器的性能
- TRACE:回显服务器收到的请求,主要用于测试或诊断



## re.match与re.search的区别  

- re.match:尝试从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话,match()就返回None
-  re.search:扫描整个字符串并返回第一个成功的匹配
-  match于search的区别:re.match只匹配字符串的开始,如果字符串开始不符合正则表达式,则匹配失败,函数返回None;而re.search匹配整个字符串,知道找到一个匹配

## findall与finditer的区别

- re.findall:在字符串中找到正则表达式所匹配的所有子串,并返回一个列表,如果没有找到匹配的,则返回空列表.
- 注意:match和search是匹配一次findall匹配所有
- re.finditer和findall类似,在字符串中找到正则表达式所匹配的所有子串,并把它们作为一个迭代器返回



# XPath

> XPath (XML Path Language) 是一门在 XML 文档中查找信息的语言，可用来在 XML 文档中对元素和属性进行遍历

#### 选取节点

| **表达式** | 描述                                                       |
| ---------: | :--------------------------------------------------------- |
|   Nodename | 选取此节点的所有子节点。                                   |
|          / | 从根节点选取。                                             |
|         // | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 |
|          . | 选取当前节点。                                             |
|         .. | 选取当前节点的父节点。                                     |
|          @ | 选取属性。                                                 |

#### 路径表达式

|       bookstore | 选取 bookstore 元素的所有子节点。                            |
| --------------: | :----------------------------------------------------------- |
|      /bookstore | 选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！ |
|  bookstore/book | 选取属于 bookstore 的子元素的所有   book 元素                |
|          //book | 选取所有 book 子元素，而不管它们在文档中的位置               |
| bookstore//book | 选择属于 bookstore 元素的后代的所有   book 元素，而不管它们位于 bookstore 之下的什么位置。 |
|         //@lang | 选取名为 lang 的所有属性。                                   |

#### 谓语

|                         路径表达式 | 结果                                                         |
| ---------------------------------: | :----------------------------------------------------------- |
|                 /bookstore/book[1] | 选取属于 bookstore 子元素的第一个   book 元素。              |
|            /bookstore/book[last()] | 选取属于 bookstore 子元素的最后一个   book 元素。            |
|          /bookstore/book[last()-1] | 选取属于 bookstore 子元素的倒数第二个   book 元素。          |
|      /bookstore/book[position()<3] | 选取最前面的两个属于 bookstore 元素的子元素的 book 元素。    |
|                     //title[@lang] | 选取所有拥有名为 lang 的属性的 title 元素。                  |
|               //title[@lang=’eng’] | 选取所有 title 元素，且这些元素拥有值为   eng 的 lang 属性。 |
|       /bookstore/book[price>35.00] | 选取 bookstore 元素的所有   book 元素，且其中的 price 元素的值须大于 35.00。 |
| /bookstore/book[price>35.00]/title | 选取 bookstore 元素中的   book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。 |

#### 选取未知节点

| 通配符 | 描述                 |
| -----: | :------------------- |
|      * | 匹配任何元素节点。   |
|     @* | 匹配任何属性节点。   |
| node() | 匹配任何类型的节点。 |

#### 选取若干路径

|                     **路径表达式** | 结果                                                         |
| ---------------------------------: | :----------------------------------------------------------- |
|       //book/title \| //book/price | 选取 book 元素的所有 title 和 price 元素。                   |
|                 //title \| //price | 选取文档中的所有 title 和 price 元素。                       |
| /bookstore/book/title   \| //price | 选取属于 bookstore 元素的   book 元素的所有 title 元素，以及文档中所有的   price 元素。 |



# BeautifulSoup

#### 元素选择器

```
对象.标签名 只获取第一个标签
print(html.p)
```

#### 获取文本

```
string  如果当前标签中只有字标签没有其他文本内容那么可以获取到子标签的内容
		如果当前标签有文本内容而且还有字标签 那么直接返回none
get_text() | text     
		结果相同 不管有没有字标签 获取当前标签和子标签的内容
print(html.title.string)
print(html.p.get_text())
print(html.p.text)
```

#### 获取属性

```
第一种只能获取指定属性的值 
第二种获取标签所有的属性 字典类型

print(html.a['href'])
print(html.a.attrs)
```

#### 筛选

```
print(html.find(class_="sister"))
print(html.find_all('p'))
```

#### 获取指定标签带有指定属性的值

```
els = html.find_all('a',attrs={'id':'link1'})
print(els)
```

#### 指定标签同时满足多个条件

```
els = html.find_all('a',attrs={'class':'sister','id':'link1'})
print(els)
```

#### 获取只要满足一个条件的

```
els = html.find_all(['p','a'])
print(els)
```

## 选择器

#### select

#### 类选择器

```
res= html.select('.sister')
print(res)
```

#### id选择器

```
res = html.select('#link1')
print(res)
```

#### 后代选择器

```
res = html.select('div p')
print(res,type(res[0]))

res = html.select('.item .inner1')
print(res)
```

#### 子元素选择器

```
res = html.select('.item > .inner1')
print(res)
```

#### 同时获取

```
res = html.select('.item,p[class=story]')
print(res)
```

#### 获取类名以指定字符开头的元素

```
res = html.select('p[class^=t]')
print(res)
```

#### 以指定字符结尾的

```
res = html.select('p[class$=y]')
print(res)
```

#### 包含指定字符

```
res = html.select('p[class*=t]')
print(res[0].get('class'))
```


