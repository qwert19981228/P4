# 模块



## 数学模块 math

### 导入模块

```python
import math
```

### 具体方法

#### math.ceil( )

​	**功能**:进一取整, 小数位只要不是0, 都会进1

#### math.floor( )

​	**功能**:舍一取整, 无论小数是几, 都直接抛弃, 只留下整数

```python
a = 3.5
a = 3.2
a = 3.0
b = math.ceil(a)
b = math.floor(a)
```

#### math.pow( )

​	**功能**:开次方, 开2的3次方

#### math.sqrt( )

​	**功能**:开平方根

#### math.fabs( )

​	**功能**:获取绝对值

#### math.modf( )

​	**功能**:以元组形式存储小数位和整数位 

```python 
a = math.pow(2,3) 
a = math.sqrt(9) 
a = math.fabs(-3.5)
a = math.modf(5.87)
```

#### math.fsum( )

​	**功能:**计算序列值和

```python
a = [1,2,3]
a = (1,2,3)
a = {1,2,3}
a = {1:2,3:4}
b = math.fsum(a) 
```

#### math.copysign( )

​	**功能:**将第二个值的符号拷贝给第一个值

```python
a = -5
b = 3
c = math.copysign(a,b)
c = math.copysign(b,a)
```

#### math.pi

​	**功能:**圆周率

#### math.e 

​	**功能:**自然底数

```python
a = math.pi
a = math.e
```



## 时间模块 time

### 导入模块

```python
import time
```

### 具体方法

#### time.time( )

​	**功能:**时间戳,从1970-现在的秒数,格林威治时间

```python
a = time.time()
```

#### time.ctime(时间戳)

​	**功能:**格式化时间戳

​	**返回值:** 周 月  日  时 分  秒 年

```python
a = time.ctime() 	
```

#### time.gmtime( )

​	**功能:**世界时间元组

```python
a = time.gmtime()
```

#### time.localtime( )

​	**功能:**本地时间元组

​	**返回值:** 格式化之后的时间字符串

```python
a = time.asctime()
a = time.asctime(time.localtime())
```

#### time.strftime(格式, 时间元组)

​	**功能**:格式化时间元组

​	**返回值**:格式化后的时间字符串

```python
a = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
a = time.strftime('%Y/%m/%d %I:%M:%S %p', time.localtime())
a = time.strftime('%U',time.localtime())
a = time.strftime('%x',time.localtime())
a = time.strftime('%X',time.localtime())
# a = time.strftime('%Z',time.localtime())
a = time.strftime('%Y %% %m %% %d %I:%M:%S %p', time.localtime())
```

#### time.strptime(时间字符串, 格式)

​	**功能**:格式化时间字符串

​	**返回值:**时间元组

```python
a = time.strptime('2018-12-17 10:12:30','%Y-%m-%d %H:%M:%S')
```

#### time.mktime(时间元组)

​	**功能**:格式化时间元组

​	**返回值:**时间戳

```python
a = time.mktime(time.localtime())
a = time.mktime((2018,12,17,10,15,30,0,0,0))
```

#### time.sleep(秒数)

​	**功能**:睡眠

```python
time.sleep()
```

#### time.perf_counter()

​	**功能**:系统运行的时间, 包含睡眠时间

####  time.process_time()

​	**功能:**消耗cpu的时间, 不包含睡眠时间



## 日历模块 calendar

### 导入模块

```python
import calendar
```

### 具体方法

#### calendar.calendar( )

​	**功能**:一年的日历

​	**参数**:年份  w 默认2,日期间隔  l 默认1,上下行间距  c 默认6,月份间隔

```python
a = calendar.calendar(2018)
a = calendar.calendar(2018,2,1,20)
```

#### calendar.month( )

​	**功能**:某一月的日历

```python
a = calendar.month(2018,12)
a = calendar.month(2020,12)
a = calendar.month(8000,12)
print(a)
```

#### calendar.isleap(年份)

​	**功能:**判断是否是闰年

```python
a = calendar.isleap(2000)
```



## 日期模块 datetime

### 导入模块

```python
import datetime
```

### 具体方法

#### datetime.datetime.now()

**功能**:当前时间

```python
a = datetime.datetime.now()
```

#### datetime.datetime.from time stamp(时间戳)

**功能:**格式化时间戳

```python
a = datetime.datetime.fromtimestamp( 1566666666 )
```

####  datetime.datetime.datetime.strftime(格式)

**功能:**格式化时间戳

```python
a = datetime.datetime.now().strftime('%Y-%m-%d')
```

#### datetime.datetime.datetime.strptime('时间字符串', '格式')

**功能:**格式化时间字符串

```python
a = datetime.datetime.strptime('2018-12-17', '%Y-%m-%d')
```

#### datetime.timedelta( 时间间隔 )

**功能:**计算时间间隔

> 默认参数days=?.  如果是按天算, 可省略days

```python
a = datetime.datetime.now() - datetime.timedelta(days=1) 	# 昨天
a = datetime.datetime.now() + datetime.timedelta(days=1) 	# 明天
a = datetime.datetime.now() + datetime.timedelta(2) 		# 后天
```



## 系统模块 os

### 导入模块

```python
import os
```

### 具体方法

#### os.name属性/变量

​	**功能:**获取当前是什么系统

​		nt		=>	windowns/winNT

​		posix	=>	linux

```python
a = os.name 
```

#### os.sep属性

​	**功能**:获取当前系统支持的路径分隔符

​		windows:  \ 

​		linux:    / 

```python
print(os.sep)
```

#### os.getcwd()

​	**功能**:获取当前工作路径

```python
print(os.getcwd())
```

#### os.mkdir()

​	**功能:**创建目录

​	**注意**:./当前目录

​		../上一级目录

​		../../上上级目录

​		依次类推

```python
os.mkdir('a')
os.mkdir('./a')
os.mkdir('../a')
os.mkdir('../../b')
```

#### os.makedirs(目录路径)

​	**功能**: 创建多级目录

​	**注意:**如果该目录已存在, 则报错

```python
os.makedirs('./x/y/z')
```

#### os.rmdir(目录路径)

​	**功能**: 删除空目录

​	**注意:**只能删除 空目录 (里面不能含有任何文件或目录)

```python
os.rmdir('./a')
```

#### os.chdir(目录)

​	**功能**: 修改当前工作路径

```python
os.chdir('./a') 	#切换当前目录到a里面
os.mkdir('./z') 	#此时创建目录,是在a目录里面创建
```

#### os.system( 系统命令 )

​	**功能**: 运行系统命令

​		**windows**命令:

​			创建文件: type null>文件名

​			删除文件: del 文件名

​			创建目录: mkdir 目录名

​			删除目录: rmdir 目录名

​		**Linux**命令:

​			创建文件: touch 文件名

​			删除文件: unlink 文件名

​			创建目录: mkdir 目录名

​			删除目录: rmdir 目录名

​		**在哪个系统下**, **就用哪个命令**

```python
os.system('type null > a.txt')
os.system('del a.txt')

os.system('mkdir aaa')
os.system('rmdir aaa')
```

#### os.remove(文件路径)

​	    **功能**: 删除一个文件

​	    **注意**: 若文件不存在, 则报错

```python
os.remove('./a/b/c/d.txt')
```

#### os.listdir(目录路径)

​	    **功能**: 获取指定目录下的所有文件 和文件夹

```python
result = os.listdir('./a')
```

#### os.path.exists(路径)

​	**功能**: 判断一个文件 或 目录是否存在

```python
print( os.path.exists('./a/a (1).txt'))
print( os.path.exists('./a/a (999).txt'))
print( os.path.exists('./a/b'))
```

#### os.path.isfile(文件路径)

​	**功能**: 判断是否为文件

```python
print( os.path.isfile('./a/a (1).txt'))
print( os.path.isfile('./a/b'))
```

#### os.path.isdir(目录路径)

​	**功能**: 判断是否为目录

```python
print( os.path.isdir('./a/a (1).txt'))
print( os.path.isdir('./a/b'))
```

#### os.path.abspath(路径)

​	**功能**: 获取绝对路径

​	**注意**:windows: 指的就是某个盘符

​		linux: 指的是根目录

```python
print( os.path.abspath('./a'))
print( os.path.abspath('./a/a (1).txt'))
```

#### os.path.join(路径1, 路径2)

​	**功能**: 拼接目录和文件名

​	**注意**:中间的分隔符, 会自动采用当前系统的默认分隔符

```python
print(os.path.join('./a','a (1).txt'))
```

#### os.path.split(路径)

​	**功能**: 拆分路径

```python
url = 'C:/Python3/P4/1218/a/a (1).txt'
print(os.path.split(url))
```

#### os.path.dirname(路径)

​	**功能**: 只获取目录

```python
url = 'C:/Python3/P4/1218/a/a(1).txt'
print( os.path.dirname(url))
```

#### os.path.basename(路径)

​	**功能**: 只获取文件名

```python
url = 'C:/Python3/P4/1218/a/a (1).txt'
print(os.path.basename(url))

```

#### os.path.getsize(文件路径)

​	**功能**: 获取文件的大小

​	**注意**:仅支持文件大小, 不支持目录大小

```python
print(os.path.getsize('./a/a (1).txt'))
print(os.path.getsize('./a')) 	 		
```



## 高阶文件模块 shutil

### 导入模块

```python
import shutil
```

### 具体方法

> src: 源文件
>
> dst: 目标文件

#### shutil.copyfile(src, dst)

​	**功能**: 将文件src 的内容复制给 dst

​	**注意**:仅仅将内存复制过给dst

​		dst 若不存在, 则自动创建

​		dst 若存在, 则删除原有内容, 重新写入

```python
 shutil.copyfile('./a.txt', './b.txt')
```

#### shutil.copymode(src, dst)

​	**功能**: 将src 的文件权限复制给了 dst

​	**注意**:dst若不存在, 则报错

​		dst若存在, 只把src的权限给了dst,不会复制内容

```python
shutil.copymode('./c.txt', './d.txt')
```

#### shutil.copystat(src, dst)

​	**功能**:将src文件的权限和时间复制给了dst

​	**注意**:dst 若不存在, 则报错

​		dst 若存在,仅仅复制权限和时间,不包括内容

```python
hutil.copystat('./e.txt', './f.txt')
```

#### shutil.copy(src, dst)

​	**功能**: 将src文件的权限和内容复制给了dst

​	**注意**:dst 若不存在, 则自动创建

​		dst 若存在,仅仅复制权限和内容,不包括时间

```python
shutil.copy('./e.txt', './g.txt')
```

#### shutil.copy2(src, dst)

​	**功能**: 将 src文件的 权限, 内容 和 时间 复制给了dst

​	**注意**:dst 若不存在, 则自动创建

​		dst 若存在, 那都复制, 内容会重写

```python
shutil.copy2('./e.txt', './h.txt')
```

#### shutil.copytree(src, dst)

​	**功能**: 将 src目录 递归复制给 dst

​	**注意**:src 和 dst 都是目录

​		在复制src 时, 会递归复制所有的子文件 和 子目录

​		dst若不存在, 则自动创建

```python
shutil.copytree('./a', './b')
```

#### shutil.rmtree(src)

​	**功能**:递归删除目录 src 

​	**注意**:src 不存在, 则报错

​		src 存在, 则删除里面所有的文件和目录, 包括自己

```python
shutil.rmtree('./b')
```

#### shutil.move(src, dst)

​	**功能**: 剪切文件 或 重命名文件

​	**注意**:适用于 文件 或 目录

​		重命名: 只要目录没变即可

​		剪切:  必须要换一个目录

​		剪切目录时, 拒绝访问的文件不能被剪切

```python
shutil.move('./h.txt', './hhh.txt') 	# 重命名
shutil.move('./hhh.txt', './a/h.txt') # 剪切
shutil.move('./a', './b')
shutil.move('./b', './c/b')
```



## 压缩包模块 zipfile

### 导入模块

```python
import zipfile
```

### 具体方法

#### 压缩

##### zip包.ZipFile( )

​	**filename**: 给zip包 取个名字

​	**mode**:打开方式

​		r 读取zip包里面的文件

​		w 往zip包里面写入文件 (会清除原有的内容)

​		a 往zip包里面写入文件 (不会清除原有的内容)

​	**compression**:压缩方法

​		ZIP_STORED      仅仅将文件存入zip, 不会真正的压缩, 默认

​		ZIP_DEfLATED     通过zip压缩算法, 再将文件存入zip

​	**allowZip64**: 是否允许创建 >= 2G的zip包

​		True: 允许, 默认

​		False: 不允许

##### zip包.write( )

​	**filename**: 将哪个文件/目录 写入zip包

​	**arcname**: 给写入zip包里的文件/目录 取个别名 (防止出现重名)

​	**compression**: 压缩方式

​		ZIP_STORED     仅仅将文件存入zip包, 并非真正的压缩, 默认

​		ZIP_DEFLATED   将文件 压缩到zip包, 提前通过zip压缩算法处理一次

#### 解压

##### zip包.extract(文件名, 指定目录)

​	**功能**: 解压一个文件 到 指定目录

##### zip包.extractall(指定目录)

​	**功能**: 解压所有文件 到 指定目录 

​	**注意**:如果指定目录不存在, 则自动创建





# 面向对象



## 概念

> OOP只是一种编程思想  

​	**类**:就是一个**抽象,虚拟**的事物

​	**对象**:就是真实的,**实例化**的事物

​		**类**就是**对象**的**抽象化**

​		**对象**就是**类**的**实例化**



## 类

#### 格式

`class  类名( ):`

​	`代码块`

#### 命名规范

##### 类名

1. 类名采用大驼峰命名法(每个单词的首字母大写)
2. 类名一般都是名词
3. 严格区分大小写

##### 属性名

1. 由数字,字母和下划线组成
2. 不能以数字开头

##### 方法名

- 以动词开头

##### 属性名和方法名

1. 一律小写,多个单词用下划线隔开
2. 严格区分大小写

**注意**:

​	类一旦实例化,就会占据一个内存

​	类不实例化,就不能正常使用



## 对象

#### 定义

​	单独的类只是抽象的, 只有实例化之后, 才能真正的使用

#### 创建一个对象(实例化)

​	对象名 = 类名()

#### 使用属性

​	对象名.属性名

#### 使用方法

​	对象名.方法名()

#### self

- self : 当前对象
- 别名 : 伪对象
- 限制 : 只能在类内使用
- 注意 : self不是关键字, self用其他单词来代替, 并非固定词 ( 用self来表达, 习惯, 不成文的规定)
- 普通方法中, 必须带有self参数, 必须是第一个

> 小结:在类内, 靠 self 使用属性/方法
>
> ​	在类外, 靠 对象 使用属性/方法 
>
> ​	属性和方法 都是依托对象而存在的

```python
class Plane():
	name = '波音777'
	age = 18
	def fly(self):
		print('I can fly')
	def test(self):
		print(self) 	# 就是 plane object,   就是对象 a
		print(self.name)
		print(self.age)
		self.fly()
a = Plane() 	
print(a)		
print(id(a)) 
```



## 操作类

### 类内

1. 类内修改属性
2. 类内新增属性

### 类外

1. 在类外, 修改属性
2. 在类外, 新增属性

### 注意

- 给属性赋值, 若属性已存在, 即为修改
- 若属性不存在, 即为新增
- 不推荐在类外 修改或新增属性
- (原因: OOP有封装性, 如果在类外修改或新增, 就违反了OOP的特性)

```python
class Plane():
	name = '波音777'
	age = 18
	def fly(self):
		print('I can Fly')
	def biu(self):
		print('射两下')
	def test(self):
		print(self.name)
		print(self.nickname)
		self.age = 50 					# 类内修改属性
		print(self.age)
		self.desc = '666, 有钱自己造一个' # 类内新增属性
		print(self.desc)
a = Plane()
a.name = '中国歼击机' 		# 在类外, 修改属性
print(a.name)  			    # 在类外, 新增属性
a.nickname = '最牛逼的战斗机'
print(a.nickname)
a.test()
print(a.age)
```



## 类的专属方法(魔术方法)

### 构造方法

#### 触发条件

​	实例化类时

#### 主要作用

1. 设置初始化属性
2. 改变初始化属性

> 小结: 有了 `__init__`,  类才能变得更加通用

```python
class Book():
	def __init__(self, name, author, price):
		self.name = name 		# 新增属性 name (书名)
		self.author = author 	# 新增属性 auther (作者)
		self.price = price 		# 新增属性 price (单价)
a = Book('金瓶梅', 'xx', 188)
b = Book('金瓶梅2', 'yy', 68)
print(a)
```



### 析构方法

#### 触发条件

​	当对象被销毁的时候

**有以下几种销毁场景**

- 当程序自然结束时
- 当对象被删除时
- 当对象被覆盖时

#### 主要作用

​	在销毁之前, 做一些遗嘱

```python
class Book():
	def __init__(self, name, author, price):
		self.name = name 		# 新增属性 name (书名)
		self.author = author 	# 新增属性 auther (作者)
		self.price = price 		# 新增属性 price (单价)
	def __del__(self):
		print('书快要被扔了, 当草纸擦擦屁股')
a = Book('熊出没', '熊大', 20)
print(a.name)
print(a.author)
print(a.price)
# del a   	#当对象被删除时
a = '光头强' #当对象被覆盖时
```



## OOP的三大特性

### 封装性

#### 定义

​	将属性和方法集中到一个类中, 形成一个不可分割的类

​	封装后, 类内的属性和方法, 有的公开, 有的私有

#### 格式

​	私有属性

​		`__属性名 = 值`

​	私有方法

​		`def __方法名(self): `

​			`pass`

#### 使用

​	self.__属性名

​	self.__方法名()

​	限制: 只能在类内使用

#### 注意

- 默认属性和方法, 都是公开, 类内类外都可以访问
- 私有属性和方法, 只能在类内使用
- 定义一个类时, 如果不想让外边的人使用这个属性/方法, 就设置为私有的
- 私有的常用于 内部的事情

```python
class Person():
	name = '小宋'   							# 公有属性
	__size = '3cm' 							 # 私有属性, 在类外是无法访问
	def getname(self):  					# 公有方法
		print('大家好, 我是 %s' % self.name)
	def __skill(self): 						# 私有方法
		print('%s 会偷电瓶车 ' % self.name)
	def test(self):
		print('在类内访问 __size : %s' % self.__size)
		self.__skill()
a = Person()
print(a.name)
# print(a.__size)
a.getname()
# a.__skill()
a.test()
```



### 继承性

#### 定义

​	子类继承父类的一些东西

​		子类: 派生类, 扩展类 

​		父类: 基类

​	优点: 提高代码的重用性, 降低冗余率

#### 格式

​	class 子类(父类):

​		代码块

#### 特性

- 可以继承属性和方法 (不能继承私有属性和方法)

- 可以重写属性和方法

- 支持单继承, 连续继承, 多继承

  **super( )调用父类的方法**

### 多态性

#### 定义

​	通过一个类, 传入不同的对象, 从而实现不同的效果

#### 优点

​	 提高代码的灵活度

```python
class usb():
	def run(self): 			# run 方法代表运行接入的设备
		pass
class mouse(usb):
	def run(self):
		print('已连接鼠标')
class keyboard(usb):
	def run(self):
		print('已连接键盘')
class udisk(usb):
	def run(self):
		print('已连接U盘')
# 准备在电脑上实现效果
class computer():
	def start(self, usb):
		usb.run() 			# 一开机, 就通过usb来调用run() 方法
c = computer()
m = mouse()
k = keyboard()
u = udisk()
c.start(m) 	# 电脑开机, 运行usb上的鼠标
c.start(k)  # 电脑开机, 运行usb上的键盘
c.start(u) 
```



## 类属性和实例属性

### 定义

​	通过类     来访问的属性, 都叫做"类属性",  别称"类变量"

​	通过对象 来访问的属性, 都叫做"实例属性", 别称"实例变量"

​	**作用**

​		类属性: 资源共享

​		实例属性: 资源独享

### 访问

```python
class Person():
	name = '小龙'
print(Person.name) 	# 类属性
a = Person()
b = Person()
print(a.name) 		# 实例属性
```

### 修改

##### 	通过类来修改:

​		将会把类中的属性给修改掉

​		这会影响"所有"从 类实例化出去的对象 (拥有专属的除外)

##### 	通过对象来修改:

​		一旦将类实例化, 生成一个对象,对象会拥有"独立的内存", 拥有类的所有属性和方法

- 只要不修改属性, 就会受到类的影响
- 一旦对象自己修改了属性, 那么这个属性是专属于对象,将不再受到类的影响

``` python
Person.name = '神龙'
print(Person.name)
print(a.name)
print(b.name)

a.name = '大龙'		#实例修改
print(Person.name)
print(a.name)

Person.name = '火龙'	#类修改
print(Person.name)
print(a.name)
print(b.name)
```

