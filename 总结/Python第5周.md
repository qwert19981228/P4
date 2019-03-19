## 类方法和实例方法

### 定义

​	**类方法**:通过**类名**来访问的方法

​	**实例方法**:通过**对象**来访问的方法

### 格式

#### 	类方法格式

​		@classmethod

​		def  方法名(cls):

​			代码块

### 注意

1. 在方法名上一行必须添加@classmethod

2. 第一个参数必须设为cls,功能类似于self

   cls也不是关键字,名字可以改

   - cls代表当前类名
   - self代表当前对象

### 小结

1. 类方法:属于类
   - 可以通过类访问
   - 可以通过对象访问
   - 只可以访问类属性
   - 一个类占一个内存
2. 实例方法:属于对象
   - 可以通过对象访问
   - 可以直接访问实例属性
   - 可以间接访问类属性和类方法
   - 一个对象占一个内存



## 静态方法

### 定义

不需要使用类属性,也不需要使用实例属性,即可定义为静态方法

**作用:**说明书,更新内容,协议展示,....

### 格式

​	@staticmethod

​	def 静态方法名( ):

​		代码块

> 注意:不需要强制传入,self或cls



# 异常

### 定义

​	在程序执行过程中, 如果发生了错误, 那么程序会立马终止, 并提示一些错误信息, 这就是"异常"

​	其中, 这些错误信息, 这种行为"抛出异常"

​	我们程序员需要做的, 就是让产品不会抛出异常, 尽量给用户比较好的体验感

### 格式

#### 写法1

​	**基本用法**

​	**try:**

​		**正在执行代码的区域a  (捕获异常)**

​	**except:**

​		**处理异常的区域b       (处理异常)**

​	**区域c**

​	

​	**分析:**

​		区域a  如果发生错误, 则立马进入区域b			

​		区域a  如果没发生错误, 则等区域a 执行完, 然后进入区域c

​		在try中, python一直在捕获 区域a 的异常, 一旦捕获成功, 则会执行区域b       

​	**注意**:无论上面是否有异常, 区域c 都会执行

```python
try:
	num = int( input('请输入数字: ') )
	print('您输入的是: %d' % num)
except:
	print('您输入的不是数字')

print('--'*30)
```

#### 写法2

​	**不同的错误, 报不同的信息**

​	**try:**

​		**代码块a**

​	**except 错误类型1:**

​		**代码块b**

​	**except 错误类型2:**

​		**代码块c**

​	**. . .**

```python
try:
	num = int(input('请输入数字: '))
	result = 100 / num
	print('100 / %d = %f ' % (num, result))
except ZeroDivisionError:
	print('不能输入数字0')
except ValueError:
	print('请输入数字')

```

#### 写法3

​	**不同的错误信息, 报相同的提示信息**

​	**try:**

​		**代码块a**

​	**except (错误类型1, 错误类型2, ...):**

​		**代码块b**

​	**except (错误类型3, 错误类型4, ...):**

​		**代码块c**

```python
try:
    num = int(input('请输入数字: '))
	result = 100 / num
	print('100 / %d = %f ' % (num, result))
except (ZeroDivisionError, ValueError):
	print('请输入正确的数字')
```

#### 写法4

​	**未知错误**

​	**try:** 

​		**代码块a**

​	**except Exception as 变量:** 

​		**代码块b**

​	**作用**:

​		在实际开始种, 想要把所有可能发生的错误全部预测出来, 挺难的

​		此时,通过Exception 异常类 统一抛出异常. 例如: 404, 服务器繁忙...

```python
try:
	num = int(input('请输入数字: '))
	result = 100 / num
	print('100 / %d = %f ' % (num, result))
except Exception as e:
	print('未知错误: %s' % e)
```

#### 写法5

​	完整写法

​	**try:**

​		**代码块a **

​	**except 错误类型1: **

​		**. . .**

​	**except 错误类型2:**

​		**. . . **

​	**except (错误类型3,错误类型4):   **

​		**. . .  **

​	**except (错误类型5,错误类型6):   **

​		**. . .  **

​	**except Exception as e:**

​		**. . .**

​	**else:**

​		**代码块b  没有异常时才会执行**

​	**finally:**

​		**代码块c  无论是否有异常, 都会执行**

```python
try:
	num = int(input('请输入数字: '))
	res = 100 / num
except ValueError:
	print('请输入正确的数字')
except (ZeroDivisionError):
	print('请输入非0数字')
except Exception as e:
	print('未知错误: %s' % e)
else:
	print('100 / %d = %f ' % (num, res))
finally:
	print('*'*30)
```



## 异常传递

### 场景:

​	在实际开发中, 都是模块式开发, 每一个功能都是独立的

​	最终会在一个主程序中 集中进行调试.

​	如果在调用模块时, 其中一个模块发生了错误, 那么try应该写哪里

### 解决方案:  

​	把try写在主程序里面

```python
def demo1():
	return int(input('请输入数字:'))
def demo2():
	return demo1()
try:
	demo2()
except Exception as e:
	pass
```



## 主动抛出异常

### 场景

​	在之前学的Python中, 都是自动捕获异常, 也会自动报错.

​	在实际开发中, 有很多业务不满足条件时, 也会做异常处理, 此时需要主动抛出异常来处理

### 使用

能够进入处理异常区域的方式:

1. 自动捕获异常
2. 主动抛出异常
   - 准备异常
   - 抛出异常



## `__new__`

### 触发条件

​	创建实例时, 自动触发

### 功能

​	创建一个对象



# 单例模式

### 定义

​	第一次通过类实例化时,产生一个对象

​	第二次及以后再次通过类实例化时,会直接获取第一次实例化得到的对象,不会再创建新的对象

### 优势

​	由于只会产生一个对象,所以内存得到节省(内存是同一个)

```python
class Music(object):
	# 用于记录 第一个对象
	first = None
	is_init = False
	def __new__(cls): # 重写object里面的new
        # 若first为空, 则证明从未实例化过, 那么允许创建一个对象
		# 若first非空, 则证明已经实例化过, 那么不允许创建对象
		if cls.first is None:
			cls.first = super().__new__(cls)
		return cls.first
	def __init__(self):
		if Music.is_init == True:
			return None
		print('hello, 酷狗')
		Music.is_init = True
a = Music()
b = Music()
c = Music()
print(a)
print(b)
print(c)
```

**总结**

​	只有一个对象,只执行一次初始化



# 装饰器

### 定义

​	**本质**是一个**函数**

### 作用

​	在不影响原有函数的基础上,给函数扩展功能,使用起来更加强大

​	如果有多个装饰器,离的越近,就优先执行哪个装饰器

​	**装饰器 = 高阶函数 + 闭包函数**

```python
#原生写法
def wing(func):
	def angel():
		things = '天使翅膀'
		name = func() 		 # name = 东北虎
		print('一个拥有 %s 的 %s ' % (things, name))
	return angel
def tiger():
	name = '东北虎'
	return name
a = wing(tiger) 	# a 接收的就是 angel 函数
a()
```

```python
# 装饰器写法
def wing(func):
	def angel():
		things = '天使翅膀'
		name = func() 		 # name = 东北虎
		print('一个拥有 %s 的 %s ' % (things, name))
	return angel
@wing
def tiger():
	name = '东北虎'
	return name
tiger()
```



# 前端



## 网页基础布局

### HTML5 声明头

​	!DOCTYPE html

### 开始结束标记

​	<html> / </html>

### 头标签

​	<head>设置标题/引入脚本/加载样式表css/提供元信息

### 元信息标签

​	设置网页字符集为utf-8

​	`<meta charset='utf-8'>`

### 网站标题

​	<title>/

### 页面主体

​	<body>/

### 注释

​	HTML注释的内容，注释不能嵌套使用

​	<!-- -->



## HTML语法

1. 
   HTML 不区分大小写，**推荐小写**

2. HTML**标签及标签中的内容**组成一个**HTML元素**
3. HTML属性写在标签里面，用来**描述**该**元素的特征或特点**
4. 属性名 = "属性值"，不区分大小写，**建议双引号，且小写**
5. 多个属性之间用空格隔开，多个属性值之间也使用空格隔开
6. 标签之间的多个空格 或 换行，都**会被解析为一个空格**



## 功能标签

### p段落标签

​	每个段落标签之间都会有一个空行

### br换行标签

​	就是换行的

### hr水平分割线标签

- **[size]** 粗细 **单位 px** 像素(pixel)
- **[width]** **宽度 px/%**
- **[align]** **水平位置** left/center/right
- **[color]** 颜色 

​		英文 blue red green yellow 

​		RGB #000 #fff

​		rgb(255,255,255)

### center居中标签

​	居中的

### pre格式化输出标签

​	原样输出

### 列表标签

#### 	ol有序列表

​		[type] 1 a A i I

​		[start] 列表起始数字

​		[reversed] 升序/降序

#### 	ul无序列表

​		[type] circle disc square

#### 	li列表项

​		[value] 值

### 定义列表

#### 	dl 

​	定义列表标签

#### 	dt

​	定义列表标题

#### 	dd 

​	定义列表详情

### 标题标签

#### 	h1~h6

​		文字大小随数字大小递减，所有标签都有加粗功能

### biu标签

#### 	b加粗

#### 	i倾斜

#### 	u下划线  

### 标记

#### 	sup上标

#### 	sub下标

### font字体标签

​	定义字体用的

### image图片标签

- [src] source 指定图片资源的地址(url)
- [alt] 图片加载失败时显示的问题
- [width] 宽度
- [height] 高度
- [title] 鼠标悬停时显示的提示文字