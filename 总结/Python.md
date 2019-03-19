[TOC]

# Python基础语法

### 1.输出打印

> ##### 1.1   print('内容')
>

```python
print('亚洲四大邪术：')
```

> ##### 1.2   print('内容1','内容2','内容3',...)
>

```python
print('泰国的变性术','日本的化妆术','韩国的整容术','中国的PS术')
```

> ##### 1.3   print('内容1', '内容2', '内容3', ..., end='')
>

```python
print('救护车', '俺不能死', 'ambulance', end=' ----- ')
print('海关', '卡死他们', 'custom')
```

> ##### 1.4   
>

```python
print(
		'最近看的电影: ' \
		'"无双"' \
		'"邪不压正"' \
		'"毒液"' \
	 )
```



### 2.缩进排版

> #### python有非常严格的排版要求
>

#### 2.1默认顶格缩进

#### 2.2同级保持缩进一致 

> ##### 缩进：Tab 进行缩进，4个空格

#### 2.3一条命令 只占 一行

> 如果强行放在一行，每条命令需要用 ；隔开

```python
num = 100
if num < 500:
	print('100小于500')
	print('这里只有条件成立时, 才能进来')
		# print('这里只有条件成立时, 才能进来')
```

#### 2.4行宽

每条命令尽量不要超过80个字符，如有特殊情况，可略微超过，但最长不得超过120

原因：不方便在控制台查看         设计可能存在缺陷

### 3.注释

<u>功能：不会解析代码，做代码的描述，不写注释，后果自负</u>

格式：单行注释  #

​            多行注释  '''  内容 '''、""" 内容 """

> 注意点：多行注释 不要嵌套使用

### 4.编码

Python3    默认编码  utf-8  万国码

最早的编码  			ASCII      仅支持128个字符

支持多种语言的编码	unicode 支持英文, 韩文, 汉文, 日文 ... 缺点: 占空间

unicode进阶版 		utf-8       支持英文, 汉文, 韩文, 日文 ... 优点: 省空间

设置编码：`-*- coding: utf-8 -*-`

> ##### 注意：
>

设置是在注释里面设置的，所以#不要丢

一般编码 是写在程序的最前面

> ##### 小结：
>

若无特殊情况，文件一律使用 UTF-8 编码

若无特殊情况，文件开头必须加入 `# -*-coding：utf-8 -*-`



## 变量

### 1.定义

用于存储数据，相当于数学中学的“未知数”，并指向一个内存

### 2.格式

#### 2.1 变量名 ：值

```python
name = '红猫'
print( name )
print( id(name) ) 	# id() 	获取当前变量的内存地址
```

#### 2.2 变量名1 = 变量名2 = 变量名3 = . . .= 值

```python
a = b = c = d = 100 	# 多个变量 都指向一个内存地址
print(a)
print(b)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
```

#### 2.3未定义的变量：没有值的变量

```python
print(x) 	# 如果直接使用未定义变量, 则报错 (没有内存)
```

### 3.命名要求

#### 3.1 由数字，字母和下划线组成

```python
address = '召唤师峡谷'
name1 = '大小姐'
_desc = '喜欢一炮定江山'
print(address, name1, _desc)
```

#### 3.2 支持中文，但不推荐

```python
刘备 = '搞定了大小姐, 就搞定了江山'
print(刘备)
```

#### 3.3 不能以数字开头

```python
2B = '赵日天'
```

#### 3.4不能与关键字重名

（关键字：python系统自带的字母单词）

```python
#  查看有哪些关键字
import keyword
print(keyword.kwlist)
```

#### 3.5严格区分大小写

```python
a = 100
print(a)
# print(A)
```

### 4.变量操作

#### 4.1修改变量

- 变量名已存在，就是修改

- 变量名不存在，就是新增

```python
name = '苍老师'
name = '波老师'
print(name)

age = 18
print(age)
```

#### 4.2 删除变量

通过关键字 del 来删除

```python
a = b = c = d = 100
print(a,b,c,d)

del a
# print(a)

del b,c 
# 删除多个变量时, 每个变量之间用 , 隔开
# print(b,c,d)
print(d)
```





## Python3内存管理

### 1.引用

```python
a = 10 		
# a 就是引用, 10 就是对象
# a引用了 对象10
print(a)
b = 10
print(id(a))
print(id(b))
# 分析: b引用了 对象10, 那么此时a引用了 对象10
# 结果: a 和 b  引用了 同一个对象10
```

> #### 小结：当多个引用指向同一个对象时，即为指向同一个内存

```python
a = 20
print(a, b)
print(id(a))
print(id(b))
```

> 重点：当多个引用指向一个对象时，突然有一个引用改变了值，那么不会改变原有对象，只会产生一个新内存

### 2.垃圾回收机制

> 当对象没有人指向时，没有人引用时。一旦对象引用数量为0时，那么该对象就可以当垃圾回收，也就意味着没有内存





# 数据类型：变量值的类型

### Python3中 6个标准类型

- 1.数字             Number
- 2.字符串         String
- 3.列表             list
- 4.元组             tuple
- 5.集合             set
- 6.字典             dictionary（dict）

### 6个标准类型又分为两种：

> ##### 可变数据类型：变量值可以修改，但内存地址不会更改
>

列表，字典 ,	普通集合

> ##### 不可变数据类型：变量一旦修改，则重新指向一个新的内存地址
>

数字，字符串，元组，冰冻集合





## 数字    Number

### 1.整体

#### 1.1 整数 int

##### 1.1.1  值：正负整数值

##### 1.1.2  范围：

- 理论上 无限制   ；实际上 受限于内存

##### 1.1.3  进制：

|   进制   | 前缀 | 基数范围 |
| :------: | :--: | :------: |
|  二进制  |  0b  |   0~1    |
|  八进制  |  0o  |   0~7    |
|  十进制  |  无  |   0~9    |
| 十六进制 |  0x  | 0~9 a~f  |



- 任意进制 => 十进制

通用公式: 基数*进制^次方

次方从后向前看, 个位: 0次方  十位: 1次方  百位: 2次方



- 十进制 => 任意进制

想要转成什么进制,  十进制除以哪个进制.

每次求余数, 最终余数 倒取	

#### 1.2 布尔

##### 1.2.1 值：True / False (首字母必须大写)

##### 1.2.2 作用：

代表两种极端的状态, 常用于 判断, 比较
- True : 1, 真, 对, 开, 存在, 可以 ...
- False: 0, 假, 错, 关, 不存在, 不可以 ...



## 浮点（float）

### 1.值 

由整数 + 小数组成，中间以  .  作为分割

```python
num = 1
num = True
print(num,type(num))
```

### 2.科学计数法

nEm: n *  10的 m次方

一般情况下，科学计数法用于特别大的数字

```python
num = 2e3
print(num,type(num))
```

### 3.精度

#### 3.1 python3只有双精度,没有单精度

#### 3.2有效位数17位(从第一个非0数字开始,向后数17位)

#### 3.3控制小数

```python
a = 3.012456789112345
print(a)

a = 3.0123456789123456789
print(a)

a = 0.00123456789123456789
print(a)

a = 0.123456789
# round(变量,保留的小数位数)
b = round(a,2)      #保留两位小数
print(b)
```

> 原因:   计算机都是二进制计算机

> ​            浮点不适合做 进制运算



## complex（复数）

### 1.值：

格式：

​        实数 + 虚数j

### 2.复数操作

#### 2.1实数单独获取

#### 2.2虚数单独获取

```python
print('实数',a.real)
print('虚数',a.imag)
```

### 3.作用

复数在实际生活中，没啥用

但在后期的系统分析，数学中的平面几何，非常的有用



## string（字符串）

### 1.定义

可用于表达数字，字母，标点，汉字. . .汉字描述

### 2.格式

单引号：变量名 = ‘ 内容 ’

双引号：变量名 = “ 内容 ”

三引号：变量名 =""" 内容 """   ;    变量名 = ''' 内容 '''

```python
a1 = '不知道'
a2 = "不知道"
a3 = ''' 不知道 '''
a4 = """ 不知道 """
#分析：
#三引号：没有变量赋值，则为注释 ； 有变量赋值
print(a1)
print(a2)
print(a3)
print(a4)
```

### 3.特性

#### 3.1 单双引号可以互插,不能自插

```python
#a = 'I give you face,but you dont't want to face'
a = "I give you face,but you dont't want to face"
#a = "I give you face,but you dont"t want to face"
#a = 'I give you face,but you dont"t want to face'
```

#### 3.2 转义符号    \

​	作用:将普通符号转为特殊符号

​	例如:	\n  换行

​			 \r  回车

​			 \t  制表符   Tab

```python
a = '上面\n下面'
a = "上面\n下面"
print(a)
```

#### 3.3 原始字符串

​	在引号外面加 r 或 R,那么该字符串将会原样输出,不会解析任何字符

```python
a = r"上面\n下面"
a = R"上面\n下面"
print(a)
```

#### 3.4 字符串格式化

​	print( ' 格式化内容 ' % (内容1,内容2,...))

​		%s	字符串

​		%d   整数

​		%c   ascii

​		%o	八进制

​		%x	十六进制

​		%X	十六进制

​		%f	浮点

​		%e	科学计数法,小写

​		%E	科学计数法,大写

#### 3.5字符串操作

##### 3.5.1  拼接

​		用于变量与变量

​		用于变量与字符串

```python
a = '金庸小说:'
b = '飞雪连天射白鹿,笑书神侠以倚碧鸳'
c = a + b
print(c)
```

##### 3.5.2  复制 *

```python
a = '母鸡'
b = a * 3
print(b)
```

##### 3.5.3  索引 []

```python
a = '123456789'
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
```

##### 3.5.4  取片 [:]

```python
a = '123456789'
print(a[:])          # 从开头到末尾
print(a[2:])          # 从索引2到末尾
print(a[:2])          # 从开头到索引2,但不包括索引2
print(a[1:2])          # 从索引1到索引2,但不包括索引2
print(a[1:6:2])          # 从索引1到索引6,步长为2,但不包括索引6
```



## list (列表)

### 1.定义

由一堆数据组成的有序序列(容器)

### 2.格式

​	变量名 = [内容1,内容2,内容3,....]

```python
food = ['黄焖鸡','沙县小吃','兰州拉面']
print(food,type(food))
```

### 3.基本操作

#### 3.1访问列表:通过索引来访问

```python
print(food[0])
print(food[-3])
```

​	注意:访问不存在的索引,则报错

#### 3.2插入列表

##### 3.2.1 变量名.insert(索引,值)

​		分析:

​			如果索引不存在,按已有最大索引 +1 计算

​			如果索引已存在,插入指定索引,原有的索引依次向后推1

```python
food.insert(5,'四川麻辣烫')
print(food)
print(food[3])
```

##### 3.2.2 变量名.append(值)

​		分析:

​			append 只会插入最后面

```python
food.append('过桥米线')
print(food)
print(id(food))
```

#### 3.3修改列表

​		通过已有的索引,直接重新赋值

​		如果索引不存在,则报错

```python
food[1] = '扬州炒饭'
print(food)
print(id(food))
```

​	注意:

​		list 属于 可变类型:(只是值可变)

​		值一旦改变,但是内存不会变

#### 3.4 删除列表

​		通过已有的索引来删除

​		如果索引已存在,则会报错

```python
def food[1]
print(food)
```

## 元组、集合、字典

### 1.元组

​	变量名 = (值1,值2,值3,....)

```python
a = ('西游记', '三国演义', '红楼梦', '水浒传')
print(a, type(a))
```

### 2.集合

​	变量名 = {值1,值2,值3,....}

```python
a = {'西游记', '三国演义', '红楼梦', '水浒传'}
print(a, type(a))
```

### 3.字典

​	变量名 = {键1:值1,键2:值2,键3:值3,...}

```python
a = {'吴承恩':'西游记', '罗贯中':'三国演义', '曹雪芹':'红楼梦', '施耐庵':'水浒传'}
print(a, type(a))
```



## 类型转换

### 1.int(x)

​	注意:

​		x支持浮点,布尔,数字字符串

### 2.float(x)

​	注意:

​		x支持整数,布尔,数字字符串

### 3.bool(x)

​	注意:

​		false:0,0.0,0+0j,false,'',[],{},()         

​		除了以上,都是true

### 4.complex(x)

#### 4.1complex(real,imag=0)

​	虚数默认为0

#### 4.2实数

#### 4.3字符串复数

​		字符串不能有多余的空格

### 5.str(x)

​	支持任意类型

### 6.list(x)

​	不支持Number,其余都支持

### 7.tuple(x)

​	不支持Number,其余都支持

### 8.set(x)

​	不支持Number,其余都支持

### 9.dict(x)

​	以键值对的形式输出

# 运算符



## 算术运算符

### 1.基本运算 (+	-*/)

```python
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
```

### 2.取模,取余数(%)

```python
print(10%4)
print(4%10)
```

#### 2.1取模结果:正负取决于第二位数

```python
print(10%4)
print(10%-4)
print(-10%-4)
print(-10%4)
```

#### 2.2取模范围:

​	%x			结果:0~x-1

​	%(y-x+1)+x	结果:x~y

```python
#结果:0~2
print(0%3)
print(1%3)
print(2%3)
print(3%3)
print(4%3)
```

### 3.幂(**)

​	格式：x ** y     x的y次方

```python
print(2 ** 4)
print(2 ** 10)
print(2 ** 7)
print(2 ** 6)
```

### 4.整除(//)

​	格式: x // y       求除以y的整数,抛弃小数

```python
print(10 / 4)
print(10 // 4)
```



## 比较运算符

1. == 
2. !=
3. (>)
4. (<)
5. (>=)
6. (<=)

注意:比较结果只有 True 和 False

```python
print(10 == 10)
print(10 != 10)
print(10 >= 10)
print(10 <= 10)
print(10 > 10)
print(10 < 10)
```

​	等价值:

```python
print(0 == False)
print(0.0 == False)
print(0+0j == False)
```

​	不等价值:

```python
print('' == False)
print([] == False)
print(() == False)
print({} == False)
```





## 赋值运算符

1. = 
2. +=
3. -=
4. *=
5. /=
6. %=
7. **=
8. //=

### 1.赋值

#### 1.1单一赋值

​		先算=右边的,再算=左边的

#### 1.2连续赋值

```python
a = b = c = 20
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))
```

#### 1.3多段赋值

​	看上去从前向后,依次赋值,各自独占一个内存

```python
a,b,c = 1,2,3
print(a,b,c)
print(id(a))
print(id(c))
print(id(b))
```

​	底层:

​		a,b,c = 1,2,3

​		先是  x = 1   y = 2  z = 3         这里的xyz都是临时变量

​		最终  a = x   b = y  c = z

### 2.其他赋值

```python
a = 10
b = 5
a += b				#a = a + b
print(a,b)
```

```python
a = 10
b = 5
a -= b				#a = a - b
print(a,b)
```

```python
a = 10
b = 5
a *= b                #a = a ** b
print(a,b)
```





## 逻辑运算符

### 1.逻辑与

​	格式: x  and  y

如果x为真,那么结果就是y

如果x为假,那么结果就是x(与假前,与真后)

```python
x = 5
y = 10
print(x and y)
```

### 2.逻辑或

​	格式: x  or  y

如果x为真,那么结果就是x

如果x为假,那么结果就是y(或假后,与真前)

```python
x = 5
y = 10
print(x or y)
```

### 3.逻辑非

​	格式:not x

如果x为真,那么就是假

如果x为假,那么就是真(真即是假,假即是真)

```python
x = 5
print( not x )

x = 0
print( not x )
```

### 4.混合运算

```python
a = 5
b = 0
print( a and b or b) # 0
print( b and b or a) # 5
print( b or a and b) # 0
```



## 位运算

### 1.按位与(&)

​	两个为1即为1,否则就是0

```python
a = 5 	# 0101
b = 12  # 1100
print( a & b )

a = 4
b = 10
print( a & b )

print( 12 & 100 )
```

### 2.按位或(|)

​	一个为1即为1,否则就是0

```python
a = 5
b = 12
print( a | b )
```

### 3.按位异或(^)

​	两个不同即为1, 否则就是0

```python
a = 5
b = 12
print( a ^ b )
```

### 4.按位取反(~)

​	-x-1

```python
a = 5
print( ~a )

a = 6
print( ~a )

a = -5 
print( ~a )
```

### 5.左移(<<)  

​	低位补0, 高位抛弃

```python
a = 5
print( a << 1) 	# a 左移1位,  先将a 转为二进制
```

### 6.右移(>>)  

​	低位抛弃, 高位补0

```python
a = 5
print( a >> 2 )
```





## 成员运算符

### 1.in	

​	判断是否在	指定成员容器中

### 2.not in

​	判断是否不在		指定成员容器中

```python
name = ['迪丽热巴', '古力娜扎', '马尔扎哈', '真皮沙发']

a = '古力娜扎'
print( a in name )

a = '德玛西亚'
print( a in name )
print( a not in name )           #以list为例
```





## 身份运算符

### 1.is

判断两个变量是否来自一个内存

### 2.is not

判断两个变量是否来自不同的内存

```python
a = 10
b = 20
print(id(a))
print(id(b))
print( a is b )
print( a is not b )
```





# 流程控制



## 顺序结构

代码从上往下依次执行



## 分支结构

### 1.分支(1)

​	格式:

​		if 条件:true环境

​	规则:条件为真,则执行true环境

​		条件为假,则跳过true环境

​	分析:

​		条件就是一个表达式,例如:比较,赋值,逻辑

​		最终条件只有两个结果:true和false

```python
lv = 4
lv = 40
if lv < 6: print('青铜狗')
```

### 2.分支(2)

​	if 条件:

​		true环境(代码块)

​	代码块: 一行或者多行代码,但不能不写

```python
lv = 4
if lv < 6:
	print('青铜')
	print('菜鸟级别')
	print('还需要多锻炼锻炼')
```

### 3.分支(3)

   	if 条件:
​     		true环境
  	else: 
​     		false环境

​	规则:条件为真,则执行true环境

​		条件为假,则执行false环境

```python
lv = 4
lv = 2
if lv < 6:
	print('青铜狗')
else:
	print('大神')
```

### 4.分支(4)

​	if 条件1:

​		true1环境 (代码块)

  	elif 条件2:

​		true2环境 (代码块)

​	elif 条件3:

​		true3环境 (代码块)
  	...

​	多个条件满足一个即可进入代码块

```python
lv = 5
lv = 6
lv = 6.8
lv = 9.5
if lv <= 6:
	print('青铜')
elif lv <= 7:
	print('白银')
elif lv <= 8:
	print('黄金')
elif lv <= 9:
	print(' 铂金')
else:
	print('钻石王者')
```

### 5.分支(5)

​	if 条件1:

​		true环境1

​		if 条件2:

​			true 环境2

​			if 条件3:

​				true环境3

​				...

​				else:

​					false环境3

​			else:

​				false环境2

​	else:

​		false环境1

​	要同时满足多个条件时,才能进入相应的代码块

```python
sex = '女'
age = 20

if sex == '男':
	if age < 30:
		print('帅哥')
	else:
		print('大叔')
else:
	if age < 30:
		print('小姐')
	else:
		print('大姐')
```





## 循环结构

> 作用:将某一部分的代码,重复的执行,知道不满足某些条件时,终止循环
>
> 好处:偷懒,减少代码量

### while循环

#### 1.while(1)

​	格式:

​		while  1. 条件:

​			2.  true环境(代码块) 

​	3.循环外的代码

​		条件成立,则进入true环境

​		条件不成立,则结束循环,准备执行while外面的代码

​	执行顺序:

​			12 12 12 12 12 12 12

​			条件1成立,则进入2

​			直到1不成立,则进入3

```python
num = 1
while num < 7:
	print('老王和老李 么么哒 %d 次' % num )
	num += 1
```

#### 2.while(2)

​	while 条件:true环境		仅适合简单功能	

​	一条命令独占一行,一般不允许同在一行

​	若强制同在一行,每条命令之间用 分号 隔开

```python
num = 1
while num < 10: print(num); num += 1
```

#### 3.while(3)

​	死循环,无限循环:	条件永远成立		例如True,1...

​	在未来实时请求时,非常有用

```python
while True:
	print('123')
```

#### 4.while(4)

​	while  条件:

​		true环境(代码块)

​	else:

​		false环境(代码块)

```python
age = 10
while age < 18:
	print('现在才 %d 岁, 还不能谈恋爱' % age )
	age += 1
else:
	print('终于 %d 岁, 可以开始浪了' % age )
```





### for循环

#### 1.for(1)

​	for  变量  in  容器:

​		代码块

​	容器: list,tuple,set,dict

​	这里也可以填string

​	变量   会一次获取容器中一个值

```python
# 字符串
a = '貂蝉王昭君西施杨玉环'
for i in a:
	print(i) 	# string中, 每一次的循环, 能获取其中一个字
```

```python
# 列表
a = ['貂蝉', '王昭君', '西施', '杨玉环']
for i in a:
	print(i)
```

```python
# 字典
a = {'貂蝉':'吕布', '王昭君':'蓝猫', '西施':'范蠡', '杨玉环':'李隆基'}
for i in a:
   print(' 今天 %s 由 %s 来侍寝  ' % ( a[i]  ,i  ) )

#键	通过i来获取
#值	通过字典名 [键] 来获取值
```

#### 2.for(2)

​	for  变量  in 容器:

​		代码块

​	else:

​		进阶体

​	这里的else是值:  但循环完了就立马进入else

```python
a = ['貂蝉', '西施', '王昭君', '杨玉环']

for i in a:
	print(" %s 有空" % i )
else:
	print('今天来点刺激的, 个位爱妃先回去吧, 我要壮汉来侍寝')
```

#### 3.for(3)

​	for  变量  in  数字区间:

​			代码块 

​	数字区间:

​		range(start,stop,step)

​		参数:

​			start:从start开始,默认从0开始

​			stop:到step结束,不包括stop

​			step:步长,默认为1

```python
# 输出 0-9
for i in range(0,10):
	print(i, end=" ")
```

#### 4.其余用法

```python
a = ['貂蝉', '西施', '王昭君', '杨玉环']
a = '123456789';
a = 'abcdefg';
print(len(a)) 	# len()  获取变量的总长度

#    0  	 1 		 2 		   3
a = ['貂蝉', '西施', '王昭君', '杨玉环']
length = len(a)


for i in range(length):
	print(i, a[i])
```

分析:

​	通过range() 来实现遍历 list,tuple,set

​	获取索引和值

​	

​	如果单纯的直接遍历list,tuple....

​	只能获取到值





## 流程控制符

### 1.continue

​	立马结束当前一轮循环,直接准备下一轮循环

```python
# 输出0-9,  当碰到5, 则跳过
for i in range(10):
	if i == 5:
		continue
		print('xxxxx') 	# 该行代码也不会执行  
	print(i, end=" ")
```

### 2.break

​	立马结束当前所在的循环,准备执行循环外的代码

```python
for i in range(10):
	if i == 5:
		break
	print(i, end=' ')
```

### 3.pass

​	为了防止报错而占个位置,留待将来使用,本身无意义

```python
if True:
	pass

for i in range(10):
	pass
```





# 函数



## 概念

### 1.定义

> 将代码组织在一起,从而实现一个完整的功能

### 2.作用

​	1.可重复利用

​	2.提高开发效率

​	3.便于代码维护

### 3.分类

​	内置函数: 内建函数,系统函数,编程语言自带的,可以直接使用

​	自定义函数:根据实际需求而创造的函数

### 4.自定义

​	格式:

​		def 函数名(参数1,参数2,...):

​			函数体,代码块

​	注意:

​		函数体一定要缩进

​	组成:

​		关键字:def

​		函数名

​		参数

​		函数体

​		返回值

### 5.特性

​	不调用不执行

​	函数可以互相调用,却互不影响

​	调用函数的位置,必须在,定义函数位置的后面(有顺序要求)

​	执行原理:

​		先调用函数

​		再调用函数体,代码块

​		当代码块全部执行完毕后,回到调用函数的地方

### 6.调用函数

​	函数名()

```python
def sayStr():
	print('每次别人说我丑的时候, 我都很伤心, 年纪轻轻, 眼睛就瞎了')
	getName()


def getName():
	print('草原三兄弟: xxx,xxx,xxx ')

sayStr()
```





## 函数名

### 1.命名规范

​	由数字,字母和下划线组成

​	但不能以数字开头

```python
def a1():
	print('多年之前, 你若主动, 我们就会有故事')
a1()

def _a2():
	print('多年之后, 你若嫁了, 我若没娶, 叫你儿子放学路上小心点')
_a2()

# def 2B():
# 	pass

# def 中文():
# 	print('看看中文能不能用, 看看绿不绿, 不推荐, 因为会变绿')
# 中文()
```

### 2.大小写

严格区分大小写

严格区分大小写

严格区分大小写

```python
def a():
	print('我的这个有点小')

a()
# A()
```

### 3.命名形式

​	参考:PEP8

#### 3.1小写单词

```python
def getmessage():
	print('苍老师发来的邀约信息')
getmessage()
```

#### 3.2下划线

```python
def get_message():
	print('波老师发来的邀约信息')
get_message()
```

### 4.注意点

#### 4.1函数重名

​		调用函数,会调用前面最近的一个指定函数

​		函数可以覆盖,后面的覆盖前面的

​		尽量别重名

```python
def get_message():
	print('波老师发来的邀约信息')
def get_message():
	print('波老师昨天带学员喝酒去了')

get_message()
```

#### 4.2 函数名意义

​		为了后期的维护,提高的代码的可读性,函数名最好通俗易懂

​		看到名字就大致知道什么功能

​		惯性:

​			函数名习惯以  动词 + 名词   形式出现





## 返回值

### 1.关键字

​	return

### 2.作用

#### 2.1将函数中的值,返回到调用

#### 2.2提前结束函数,并返回,return后面的代码将不再执行

```python
def test():
	x = 100
	y = 200
	sum = x + y
	return sum

a = test()
print(a)
```

### 3.返回类型

#### 3.1值的类型

​		return可以返回任意类型

```python
def test():
	return '张全蛋'
	return {1:2,3:4}
	return {1,2,3}
	return (1,2,3)
	return [1,2,3]
	return 1+2j
	return True
	return 100.5
	return 100

print(test())
```

#### 3.2多返回值

​		return 值1,值2,...

​		return [值1,值2,...]

​		return {值1,值2,...}

​	需要一次性返回多个值:

​		1)将多个值 以逗号隔开

​		2)将值包装到list,tuple,set中

```python
def test():
	x,y,z = 100, 5.5, 'abc'
	return x,y,z 	# 一次性返回多个值, 以元组的形式返回
	return [x,y,z]
	return {x,y,z}
a = test()
print(a, type(a))
```

#### 3.3无返回值

​		如果函数没有return,默认返回None





## 参数

### 1.定义

​	参数:能用将函数功能进行微弱的变化,从而达到通用的效果

​	形参:在定义函数时给的参数(parameter)

​	实参:在调用函数时给的参数(argument)

```python
def add(a, b):
	print('a + b = %d ' % (a+b)  )

add(10, 20)
add(5, 999)
```

### 2.参数传递

#### 2.1传值和传址

​		传值:仅仅是将值传递过去

​		传址:不仅将值传递过去,而且将内存地址传递过去

#### 2.2	区分:

​		传值:不可变数据类型

​		传址:可变数据类型

```python
def test(a, b):
	a += 200 		# 传值
	b[0] *= 10 		# 传址
	print('a 的值: ', a)
	print('b 的值: ', b)
x = 10
y = [5,6,7]
test(x, y)
print('x 的值: ', x)
print('y 的值: ', y)
```

### 3.参数类型

#### 3.1必须参数

​		实参个数 = 形参个数(参数个数必须一致)

​		先到先得

```python
def test(name, age, sex):
	print('名字: %s' % name)
	print('年龄: %s' % age)
	print('性别: %s' % sex)
test('史珍香', 18, '男')
# test(18, '史珍香', '男')
```

#### 3.2关键字参数

​		实数指定参数名来传入

​		好处:不用按照顺序来传入

```python
def test(name, age, sex):
	print('名字: %s' % name)
	print('年龄: %s' % age)
	print('性别: %s' % sex)

test(age=20, sex='人妖', name='杜子腾')
```

#### 3.3默认参数

​		即便实参没有传值,形参可以采用默认值

```python
def test(name, age = 18, sex = '人妖'):
	print('名字: %s' % name)
	print('年龄: %s' % age)
	print('性别: %s' % sex)
test('二狗', 800)
```

#### 3.4不定长参数

​		在形参前面加  *,以元组形式接收没人要的实参

​		在形参前面加  **,以字典形式接收没人要的关键字实参

​		单独出现           *,在* *后面的参数必须以关键字实参进行传入

​					   且关键字必须以形参名一致

```python
def test(*a):
	print(a, type(a))

def test(x, y, *a):
	print(x, type(x))
	print(y, type(y))
	print(a, type(a))

def test(x, **a):
	print(a, type(a))

test(10,n1=20, n2=30, n3=40)
```

```python
def test(x, *, y, z):
		print(x)
		print(y)
		print(z)

# test(10,n1=20,n2=30)
test(10,z=30,y=20)
```

### 4.匿名函数

​	没有名字的函数

​	场景:功能太简单,又不想写def,不用去函数名

​	**lambda**    **形参:返回值**

​	冒号左边:想要传递的参数

​	冒号右边:需要return的结果

​	注意:lambda是一个表达式,并非语句,用在的话不能用的地方

> 小结:

​		lambda用于简单功能

​		def	     用于复杂功能

```python
# 匿名写法
test = lambda x,y: x+y
print(test(10,20))


# 原生写法
def xxx(x, y):
	sum = x + y
	return sum
```



# 变量



## 变量的作用域

### 1.全局变量

在函数外部定义的变量

### 局部变量

在函数内部定义的变量

```python
a = 10 		# 全局变量
def test():
	b = 20  # 局部变量
```

### 2.作用域

|       作用域       |   英文   | 缩写 |
| :----------------: | :------: | :--: |
|     局部作用域     |  local   |  L   |
| 闭包函数外的函数中 | enlosing |  E   |
|     全局作用域     |  global  |  G   |
|     内置作用域     | built-in |  B   |

**查询规则:	L -> E -> G -> B**

​			仅仅是访问,不代表修改或删除

```python
x = int(10.5)		#内置作用域	B
a = 0				#全局作用域	G
def outher():
	b = 1			#闭包函数外的函数中	E
	print('b的变量: %d' % b)
	def inner():
		c = b		#局部作用域	L
		c = a
		print('c的变量: %d' % c)
```

### 3.改变作用域

在作用域E中,不能直接改变全局变量,要通过global声明一下,就可以改变全局变量

注意点:

​	global a 之后,全局a 和 global a 公用一个内存

​	而在E区间中,单独写a ,仅仅是给E区间中声明一个新的变量a,该变量a 与全局a 内存 不一样

​	如果仅仅是访问全局a ,不需要global声明

```python
a = 10
def outher():
	b = 5
	global a
	a += b
	print(a)
outher()
print(a)
```

​	L区间可以访问E区间的变量,不能直接改变E区间的变量,通过nonlocal来声明一下就可以改变E区间的变量

```python
a = 10
def outher():
	b = 55
	def inner():
		nonlocal b
		b += 5
	inner()
outher()
```

> 小结:

​	**需要改变作用G中的变量,则通过global**

​	**需要改变作用E中的变量,则通过nonlocal**





## 闭包函数

### 1.定义

​	函数A里面定义了一个新的函数B

​	函数B使用函数A的变量

​	只要满足以上两个条件,函数B就是一个闭包函数

```python
def A():
	a = 10
	def B():
		print(a)
```

### 2.闭包的两种使用方式

#### 2.1直接调用	

```python
def A():
	a = 10
	def B():
		b = 20
		b += a
		print(b)
	B()
A()
```

#### 2.2返回函数名

```python
def A():
	a = 10
	def B():
		b = 20
		b += a
		print(b)
	return B
result = A()
```

### 3.作用

​	优点:数据的持久化

​	缺点:因为持久化,没有及时释放内存,所以一直占用内存,浪费了性能

### 4.注意点

​	闭包函数不能直接修改外部函数的变量





## 内置函数

### 1.类型相关的

​	int()			整型

​	float()		浮点数

​	bool()		布尔值

​	complex()	复数

​	str()			字符串

​	list()			列表

​	tuple()		元组

​	set()		集合

​	dict()		字典

### 2.变量相关的

​	id()			获取变量的内存地址

​	type()		获取变量的数据类型

​	print()		输出变量

​	locals()		获取当前作用域中的所有变量

```python
a = '女人最好什么?'
b = '最爱包,因为包治百病'
print('作用域G: ', locals())

def A():
    x = 30
    y = 40
    print('作用域E: ',locals())
    def B():
        m = 100
        n = 200
        print('作用域L: ',locals())
       B()
 A()
```

### 3.数学相关的

​	abs()		取绝对值

​	sum()		求和

​	max()		求最大值

​	min()		求最小值

​	pow()		求次方

​	round()		保留小数位

​	range()		数字区间

```python
print(abs(-5))
print(sum[1,2,3])
print(max[1,2,3])
print(min[1,2,3])
print(pow(2,3))
print(round(0.123456789,3))

for i in range(5):
    print(i)
```

### 4.进制相关的

​	hex()		十六进制

​	oct()		八进制

​	bin()		二进制

​	chr()		ascii ==> 字符

​	ord()		字符 ==> ascii

​	repr()		原始字符串

​	eval()		解析字符串(能够将字符串当成公式执行)

```python
print(hex(10))
print(oct(8))
print(bin(8))
print(chr(97))
print(ord('a'))
print(ord('A'))
print(ord('0'))

string ='老\n母\n鸡'
print(string)
print(repr(string))

a = 10
print('a+1')
print(eval('a+1'))
```





## 字符串方法

​	对象.方法名()

​	方法就是函数

​	对象:一切皆对象​	

```python
.upper()        #全部转为大写
.lower()        #全部转为小写
.capitalize()   #首字母大写
.title()        #每个单词的首字母大写
.isalnum()      #只能有数字, 字母 , 中文
.isalpha()      #只能有字母, 中文
.isdigit()      #只能有数字
.isupper()      #检测是否为大写
.islower()      #检测是否为小写
```





## 格式化字符串

### 1.基础用法

​	{}从前向后依次对应参数

```python
a = '{},{},{}高高兴兴牵着手,一起冲向女厕所'
print(a.format('熊大','熊二','光头强'))
```

### 2.索引格式化

​	{0}			只接受索引为0的参数

​	{1}			只接受索引为0的参数

​	. . .

​	{n}			只接受索引为0的参数

```python
a = '{0},{1},{2}高高兴兴牵着手, 一起冲向女厕所'
a = '{2},{1},{0}高高兴兴牵着手, 一起冲向女厕所'
a = '{1},{2},{0}高高兴兴牵着手, 一起冲向女厕所'
print(a.format('熊大','熊二','光头强'))
```

### 3.关键字格式化

```python
a = '{name}头顶{pro1}, 身披{pro2}, 脚踩{pro3}, 吾称屌丝二代'
print(a.format(name='狗蛋',pro1='锅盖',pro2='麻袋',pro3='白菜'))
print(a.format(pro1='锅盖',pro2='麻袋',pro3='白菜',name='狗蛋'))
```

### 4.索引,关键字混合

​	索引位置,必须对应好

​	关键字位置随意,但不能影响索引

```python
a = '{0}头顶{1}, 身披{pro2}, 脚踩{pro3}, 吾称屌丝二代'
print( a.format('二狗','锅盖',pro2='麻袋',pro3='白菜'))
print( a.format('二狗','锅盖',pro3='白菜',pro2='麻袋'))
```

### 5.格式限定符

​	{a:bcd}

​	a:索引/关键字

​	b:填充符号			默认空字符串

​	c:对齐符号			左< 右> 居中^

​	d:总长度

```python
a = '吕布带了很大很大的{color:"^2}{thing:>10}'
print(a.format(color='红色的',thing='帽子'))
```

### 6.进制限定

​	b:二进制			格式:{:b}

​	o:八进制			格式:{:o}

​	d:十进制			格式:{:d}

​	x:十六进制		格式:{:x}

```python
a ='八戒大约体重{:d}斤' 	#将200转成十进制
a ='八戒大约体重{:b}斤' 	#将200转成二进制
a ='八戒大约体重{:o}斤' 	#将200转成八进制
a ='八戒大约体重{:x}斤' 	#将200转成十六进制
print(a.format(200))
```

### 7.精度限定

​	格式:{:.num}		整数+小数	一共num位

​	格式:{:.numf}		小数		一共num位

​	注意点:

​		冒号后面有一个小数点

```python
a = '圆周率: {:.5}'
a = '圆周率: {:.5f}'
print(a.format(3.141592652))
```

### 8.千分位

逗号,每隔3位加一个逗号

```python
a = '马云身价${:,}'
print(a.format(10000000000000000000))
```





## 列表 list

### 1.定义

​	由一堆数据组成的有序序列

### 2.格式

​	变量名 = [值1,值2,值3,...]

​	值:可以为任意类型

```python
a = []	#空列表
print(a,type(a))
```

```python
a = ['王宝强','陈羽凡','贾乃亮']
print(a,type(a))
```

```python
a = [10,10,5,True,'小杨']
print(a)
```

### 3.基本操作

#### 3.1访问列表

​	格式:

​		变量名[索引]

```python
a = ['狗不理','叉烧包','汤包','流沙包']
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])
```

#### 3.2修改列表

​	索引存在时, 才能修改

​	索引不存在时, 则报错

```python
a[2] ='生煎包' 		
print(a)
```

#### 3.3删除列表

```python
del a[2]
print(a) 		
print(a[2])
```

#### 3.4插入列表

##### 	3.4.1插入已有的索引

​		变量名.insert(索引,值)

```python
a.insert(2,'鲜肉包')
print(a)
print(a[2],a[3])
```

##### 	3.4.2插入不存在的索引

```python
a.insert(99, '灌汤包')
print(a)
print(a[4])
```

##### 	3.4.3插入最大的索引 或 在最后面加一个索引

​		变量名.append(值)

```python
a.append('蟹黄包')
print(a)
```

​		小结:

​			如果知道索引,用insert

​			如果只是想追加一个索引,用append

### 4.高级操作

#### 4.1列表合并	+

```python
a = ['刘德华','张学友']
b = ['郭富城','黎明']
c = a + b
print(c)
```

#### 4.2列表重复	*

```python
a = ['甄姬','曹丕']
b = a*3
print(b)
```

#### 4.3列表分片	[start:stop:step]

```python
a = ['刘备','关羽','张飞','赵云','马超','黄忠','诸葛亮']
print(a[:]) 		# 从开头 ~ 末尾
print(a[2:]) 		# 从索引2 ~ 末尾
print(a[:2]) 		# 从开头 ~ 索引2 (不包含索引2)
print(a[2:5]) 		# 从索引2 ~ 索引5 (不包含索引5)
print(a[0:6:2]) 	# 从索引0 ~ 索引6, 步长为2 (不包含索引6)
```

#### 4.4成员检测 in \not in

```python
a = ['刘备','关羽','张飞','赵云','马超','黄忠','诸葛亮']
b = '曹操' in a
b = '张飞' in a
b = '曹操' not in a
print(b)
```

### 5.遍历列表

#### 5.1遍历1

```python
a = ['刘备','关羽','张飞','赵云','马超','黄忠','诸葛亮']
i = 0
while i < 6:
	print(i,a[i]) 
	i += 1

for i in range(6):
	print(i,a[i])

length = len(a)
print(length)
for i in range(len(a)):
	print(i,a[i])
```

#### 5.2遍历2

```python
a = ['刘备','关羽','张飞','赵云','马超','黄忠','诸葛亮']
for i in a:
	print(i,a.index(i))
```

### 6.嵌套列表

```python
a = [[],[],[],[]]
print(a,type(a))

a = [['貂蝉','西施'],['熊大','熊二']]
print(a[0])
print(a[1])
print(a[0][0])
print(a[1][1])
print(a[1][0])
```

#### 修改嵌套列表

```python
a[0][1] = '杨玉环'
print(a)
```

### 7.推导式

#### 7.1基本推导式

​		格式:[变量操作 for 变量 in 列表]

```python
# 需求: 将列表中的每个值+5
a = [10,20,30,40]

# 原生写法
for i in range(len(a)):
	a[i] += 5
print(a)

# 推导式
a = [10,20,30,40]
a = [i+5 for i in a] 
print(a)
```

#### 7.2条件推导式

​		格式:[变量操作 for 变量 in 列表 if 条件表达式]

​		格式:[变量操作  if 条件表达式 else for 变量 in 列表]

```python
# 需求:获取列表中的所有偶数
a = [10,11,12,13]
a = [i + 5 for i in a if i % 2 == 0]
print(a)
```

```python
# 需求:将列表中所有的偶数+5, 其他值不变
a = [10,11,12,13]
a = [i+5 if i%2 == 0 else i for i in a]
print(a)
```

#### 7.3多循环推导式

​		格式:[变量操作 for 变量1 in 列表1 for 变量2in 列表2]

```python
# 需求:给下列人物配以称号, 写出所有的可能
a = ['屌丝','菜鸟']
b = ['狗蛋','全蛋']
c = [i+'===>'+j for i in a for j in b]
print(c)

# 原生写法:
a = ['屌丝','菜鸟']
b = ['狗蛋','全蛋']
c = []
for i in a:
	for j in b:
		c.append(i+'===>'+j)
print(c)
```

#### 7.4多循环条件推导式

​		格式:[变量操作 for 变量1 in 列表1 for 变量2in 列表2 if 条件]

​		格式:[变量操作 if 条件 else for 变量1 in 列表1 for 变量2in 列表2]

```python
# 需求: 获取索引相同的对应值
a = ['屌丝','菜鸟']
b = ['狗蛋','全蛋']
c = [ i+'==>'+j for i in a for j in b if a.index(i) == b.index(j)]
print(c)


# 需求: 获取索引相同的对应值, 索引不同的用 xx==>xx 代替
a = ['屌丝','菜鸟']
b = ['狗蛋','全蛋']
c = [i+'==>'+j  if a.index(i) == b.index(j) else 'xx===>xx' for i in a for j in b]
print(c)

```





## 元组 tuple

### 1.定义

​	一组有序的数据组合,但不能修改数据,元组属于不可变类型

### 2.格式

​	变量名 = (值1,值2,值3,...)

```python
a = () 		# 空元组
print(a,type(a))

# 真正只有一个值的写法
a = (10,)
print(a,type(a))
```

### 3.基本操作

#### 3.1访问元组

```python
a = ('大圣','天蓬','卷帘','金蝉子')
print(a[0])
print(a[-1])
```

#### 3.2修改元组

​		因为元组是不可变类型, 所以无法修改元组

#### 3.3删除元组

​		因为元组是 不可变类型, 所以无法删除元组

#### 3.4插入元组

​		因为元组是 不可变类型, 所以无法插入元组

### 4.高级操作

#### 4.1合并

```python
a = ('佛祖','普度众生')
b = ('达摩','易筋经')
c = a+b
print(c)
```

#### 4.2重复

#### 4.3分片

#### 4.4成员检测

### 5.遍历

```python
a = ('易筋经', '洗髓经', '金钟罩', '童子功')
i = 0
while i < len(a):
	print(i, a[i])
	i += 1

for i in range(len(a)):
	print(i, a[i])

for i in a:
	print(a.index(i), i)
```





## 字典 dict

### 1.定义

​	一堆由键值对组成的可变类型

### 2.格式

​	变量名 = {键:值,键:值,...}

​	键:

- 支持数字,字母,推荐用字母,少用数字

- 必须唯一,如果不唯一,后面的会覆盖前面的

- 必须是不可变类型

- 不能为空,必须写

  值:任意类型

```python
a = {}
print(a,type(a)) 	# 空字典

a = {'关羽':'云长','张飞':'翼德','刘备':'玄德'}
print(a,type(a))

a = {1:2,3:4,5:6}
print(a,type(a))

a = {1.2:2,3.3:4,5.2:6}
print(a,type(a))

a = {True:2,False:4,True:6}
print(a,type(a))
```

### 3.基本操作

#### 3.1访问字典

```python
a = {'关羽':'云长','张飞':'翼德','刘备':'玄德'}
print(a['关羽'])
```

#### 3.2修改字典

​		通过已有的键来修改字典

```python
a['关羽'] = '武圣'
print(a)
```

#### 3.3插入字典

​		通过不存在的键来修改字典

```python
a['曹操'] = '孟德'
print(a)
```

#### 3.4删除字典

​		通过已有的键来删除字典

​		如果键不存在,则报错

```python
del a['关羽']
print(a)
```

#### 3.5成员检测

```python
print('张飞' in a )
print('关羽' in a )
print('关羽' not in a )
```

### 4.遍历

```python
a = {'关羽':'云长','张飞':'翼德','刘备':'玄德'}
for i in a:		
	print(i,a[i])

# 直接获取键 和 值
for i,j in a.items():
	print(i,j)

# 单纯的遍历键
for i in a.keys():
	print(i)

# 单纯的遍历值
for i in a.values():
	print(i)
```

### 5.字典推导式

​	以列表推导式相似

#### 5.1基本推导式

​		格式:{键:值 for 键,值 in 字典.items()}

```python
# 需求:以下列格式进行是输出    绰号=xxx  大名=xxx
a = {'赵小刀':'赵丽颖','小笼包':'陈妍希','胖迪':'迪丽热巴'}
b = {'绰号='+k:'大名='+v for k,v in a.items()}
print(b)
```

#### 5.2条件推导式

​		格式:{键:值 for 键,值 in 字典.items() if 条件}

```python
# 需求:只显示名字长度为4位的人 
a = {'赵小刀':'赵丽颖','小笼包':'陈妍希','胖迪':'迪丽热巴'}
b = {k:v for k,v in a.items() if len(v) == 4}
print(b)
```

#### 5.3多循环推导式

​		格式:{键:值 for 键1,值1 in 字典1.items() for 键2,值2 in 字典2.items()}

```python
# 需求: 凑CP
a = {'赵小刀':'赵丽颖','小笼包':'陈妍希'}
b = {'小旋风':'林志颖','黑旋风':'李逵'}
c = {v1:v2 for k1,v1 in a.items() for k2,v2 in b.items()}
print(c)
```

#### 5.4多循环条件推导式

​		格式:{键:值 for 键1,值1 in 字典1.items() for 键2,值2 in 字典2.items() if 条件}

```python
a = {'赵小刀':'赵丽颖','胖迪':'迪丽热巴'}
b = {'小旋风':'林志颖','黑旋风':'李逵'}
c = {v1:v2 for k1,v1 in a.items() for k2,v2 in b.items() if len(v1)!=4 and len(v2)!=4}
print(c)
```

​	



## 集合 set

### 1.定义

​	一个值不会重复的无序序列

​	主要作用:

​		去重:将一个列表转为集合,就会自动去重

​		关系测试:测试两个集合交集,差集等

### 2.格式

​	变量名 = {值1,值2,值3,...}

​	变量名 = set((值1,值2,...))

```python
a = set() 	# 空集合
print(a,type(a))

a = {} 		# 空字典
print(a,type(a))

a = {'安其拉','王昭君','妲己'}
print(a,type(a))

a = set(('史珍香')) 
a = set(('史珍香',))
a = set(['史珍香'])
```

### 3.基本操作

#### 3.1交集	&

```python
a = set('abcd')
b = set('cdxy')
c = a & b
print(c)
```

#### 3.2并集	|

```python
a = set('abcd')
b = set('cdxy')
c = a | b
print(c)
```

#### 3.3差集	-

```python
a = set('abcd')
b = set('cdxy')
c = a - b 	#a相对于b的差集
c = b - a 	#b相对于a的差集
print(c)
```

#### 3.4对称差集	^

```python
a = set('abcd')
b = set('cdxy')
c = a ^ b 	#除了交集不要, 其余都要
print(c)
```

#### 3.5成员检测  in\not in

```python
a = set('abcd')
b = 'a' in a
b = 'x' in a
b = 'x' not in a
print(b)
```

### 4.高级操作

#### 4.1添加一个值

​		格式:集合.add(值)

```python
a = set('abcd')
a.add('x')
print(a)
```

​		格式:集合update(容器)

```python
a.update({'m','n'})
a.update(('i','j'))
a.update(['x','y'])
print(a)
```

#### 4.2删除一个值

​		格式:集合.remove(值)

```python
a.remove('a')
#a.remove('p') 	# 移除一个不存在的值, 则报错
print(a)
```

​		格式:集合.discard(值)

```python
a.discard('b')
a.discard('p') 		# 移除一个不存在的值, 不会报错
print(a)
```

### 5.遍历

```python
a = {'马克思','马云','马化腾','马加爵','马蓉','马航','马冬梅'}
for i in a:
	print(i)
```

```python
a = {
		('A1','A2','A3'),
		('B1','B2','B3'),
		('C1','C2','C3'),
	}
print(a)

for i,j,k in a:
	print(i, j, k)
```

### 6.推导式

#### 6.1基本推导式

​		格式:{变量操作 for 变量 in 集合}

```python
# 需求: 给每一个值 都加 "小"字
a = {'马克思','马云','马化腾','马加爵','马蓉','马航','马冬梅'}
a = { '小'+i for i in a }
print(a)
```

#### 6.2条件推导式

​		格式:{变量操作 for 变量 in 集合 if 条件}

#### 6.3多循环推导式

​		格式:{变量操作 for 变量1 in 集合1 for 变量2 in 集合2}

#### 6.4多循环条件推导式

​		格式:{变量操作 for 变量1 in 集合1 for 变量2 in 集合1 if 条件}



## 冰冻集合

### 1.定义

​	一旦创建就无法再进行添加或删除功能

### 2.格式

​	变量名 = frozenset(可迭代对象)

​	可迭代对象:暂时理解为 字符串,列表,元组 ...

```python
a = frozenset() 	# 空冰冻集合, 一般情况下, 也不会干这种事
print(a, type(a))

a = frozenset(['正太','孟祥云','萝莉','小娜'])
print(a)
```

### 3.遍历

```python
a = frozenset(['正太','孟祥云','萝莉','小娜'])
for i in a:
	print(i)
```

### 4.推导式

​	格式:

​		frozenset(变量操作 for 变量 in 集合)

​		frozenset(变量操作 for 变量 in 集合 if 条件)

​		.   .   .

```python
a = frozenset(['正太','孟祥云','萝莉','小娜'])
print(id(a))
b = frozenset('小'+i for i in a)
a = frozenset('小'+i for i in a)
print(b)
print(a)
print(id(a))
```

### 5.注意点

​	普通集合:可变类型

​	冰冻集合:不可变类型





## 迭代器

### 1.定义

​	可迭代对象(iterable):能够使用iter()的都属于可迭代对象

​	迭代器(iterator):将可迭代对象一个一个进行获取

​		以下是常用的可迭代对象:

​				list

​				tuple		

​				set

​				dict

​				string

​				range()

### 2.使用

​	通过iter()和next()

​	iter()创建迭代器

​	next()通过迭代器获取一个值

```python
a = iter( [1,2,3] ) # 将列表送入iter(),得到"列表迭代器对象"
print(next(a)) 		# 通过next() 获取列表迭代器中的一个值
x = next(a) 		# 其中,可以将得到的值存入别的变量,做任意操作
# print(next(a))
# print(next(a)) 	# 迭代器中已经没有值,再次迭代,就会报错
```

​	小结:

​		迭代器与循环功能相似,却有些不一样

​			迭代器是需要用的时候,才去拿一个值,俗称:懒加载

​			循环是一旦开始,就必须全部拿完





## 高阶函数

### 1.定义

​	1)参数为函数

​	2)返回值为函数

​	满足以上任意条件,即可成为高阶函数

### 2.作用

​	1)易于可读性

​	2)方便代码维护

​	3)隔离作用域

### 3.使用

#### map

​		map(func,iterable,iterable,.  .  .)

​		**功能:对迭代器中每一个对象,都使用一次函数**

```python
# 需求:对 1~10 每一个值都开平方

def power(x):
	print('%d 的平方: ' % x, end='')
	return x**2

for i in map(power, range(1,11)):
	print(i)
```

#### sorted

​		sorted(iterable,key=func,reverse=Bool)

​		**功能:将可迭代对象进行排序,生成排好的序列**

​		**参数:**

​			iterable:可迭代对象

​			key:排序依据,常用函数

​			       如果没有key,默认使用iterable的值进行排序

​			       key默认为None

​		**返回值:排好序的可迭代对象**

```python
# 需求1:按照 值的大小 排序
a = set('12345678')
print(a)
b = sorted(a) 	# key,reverse 都是采用的默认值
print(b)

# 需求2:将值取绝对值 并排序
a = [8,1,3,-4,6,7,2,5]
print(a)

b = sorted(a, key=abs)
print(b)
```

#### filter

​		filter(func,iterable)

​		**功能:过滤迭代器中的数据,返回符合条件的可迭代对象**

​		        函数将可迭代对象中的数据进行判断,True则保留,否则抛弃

​				**注意点:**

​					func 需要返回bool,外部fillter才能知道是否保留

​		**参数:**

​			func:内置或自定义

​			iterable:可迭代对象

​		**返回值:对象**

```python
# 需求:以列表形式输出 1~10 之间的偶数

# 原版
def iseven(x):
	return x%2==0
b = list(filter(iseven,range(1,11)))
print(b)

# 优化版
b = list(filter(lambda x:x%2==0,range(1,11)))
print(b)
```

#### reduce

​		reduce(func,iterable)

​		**功能:对iterable的每一个对象进行累计操作**

​		**参数:**

​			func:内置或自定义

​				要求:每次必须送入两人进函数,形参必须设置两个

​			iterable:可迭代对象

​		**返回值:计算之后的值**

​		***注意:***

​			reduce不是内置函数,所以不能直接调用

​			必须提前引入模块functools

```python
from functools import reduce

a = [1,2,3,4,5]
def add(x,y):
	return x+y

b = reduce(add,a)
print(b)
```





# 文件操作

### 1.打开文件

​	open(文件路径,打开模式)

​	返回值:io对象

```python
a = open('a1.txt','r')
print(a)
```

​	打开模式

​		r	只读,指针指向开头,文件不存在,则报错

​		w	只写,指针指向开头,文件不存在,则自动创建

​		a	追加,指针指向末尾,文件不存在,则自动创建

​		+	增强,将具备读和写能力

​		b	二进制

### 2.读取文件

​	io对象.read(位数)

​	文件读取,都是通过指针来读取

​	指针一般情况下,都是指向开头

```python
a = open('a1.txt','r')
print(a.read(2)) #从当前指针向后读取2位
print(a.read(2)) #从当前指针向后读取2位
print(a.read(5)) #从当前指针向后读取5位
print(a.read())  #从当前指针向后读取到末尾
```

### 3.写入文件

​	io对象.write(内容)

​	注意:

​		w 模式,会将原有内容先全部删除,再写入内容

​		w 模式,如果文件不存在,则自动创建

```python
a = open('a2.txt','w') 	# 打开模式为w,可以写入内容
a.write('hello')
```

### 4.追加模式

​	io对象.open(文件路径,a)

​	注意:

​		a模式,会在原有内容的最后面,进行添加内容,不会影响原来的内容

```python
a = open('a2.txt','a')
a.write('Tmail')
```

### 5.增强模式

​	在原有的模式上,加强功能,符号: +

​	在一般情况下,带有+的模式,同时具备读和写的功能

​		例如:

​			r+

​			w+

​			a+

```python
a = open('a4.txt','r+')
a.write('123') 	# 因为是r+ 模式, 内容会从开头, 依次进行覆盖, 没有碰到的内容, 不受影响
```

```python
a = open('a4.txt','w+')
a.write('abcdef') 	#此时全部写完后,指针已经到了最后

a.seek(0) 			#seek(0)将指针指向开头
print(a.read()) 
```

### 6.二进制模式

​	通常读取,写入文件时,通过以string的类型进行操作

​	byte:以二进制进行存储,以十六进制展示(格式:\x十六进制)

​	如果以b模式打开,那么在写入内容之前,必须先转为二进制

​	str==>byte	需要encode()

​	byte==>str	需要decode()	

​		为什么需要byte转换?

​			1)正常人看不懂,得到保护数据的作用

​			2)抓取的文件,有的就是二进制

​			3)速度快

```python
a = open('a5.txt','wb+')
a.write('老母鸡'.encode())#在写入之前, 将老母鸡  转为二进制再存入
a.seek(0) 				 #因为写完之后, 指针已经指向末尾
print(a.read()) 		 #读取时, 默认以二进制方式读取
a.seek(0) 		
print(a.read().decode()) #二进制正常情况下看不懂,所以需要decode()转为string再输出
```

### 7.关闭文件

​	io对象.close()

​	所有文件一旦打开,就会占据内存,一天不关闭,一天就占内存,所以用的越久,打开的越多,内存就浪费的越多

​	close()方法主要是释放内存

```python
a = open('a5.txt','r')
a.close()
```



## 文件指针

### 1.当前指针

​	io对象.tell()

```python
a = open('a1.txt','r')
print(a.tell()) 	#当前指针为0
print(a.read(2)) 	#读取2位,指针向后移2位
print(a.tell()) 	#当前指针为2
print(a.read()) 	#读取到最后
print(a.tell()) 	#当前指针是几,该文件就有多大字节
a.close()
```

### 2.移动指针

​	io对象.seek()

```python
a = open('a1.txt','r')
print(a.tell())
print(a.read(2))
print(a.tell())
a.seek(0) 			#将指针移到 最前面
print(a.tell())
a.seek(3)
print(a.tell())
a.read()			#也可以利用 read读完, 将指针移到最后
```



## 文件内容

### 1.写入文件到内容

​	io对象.write('内容')

​	返回值:写入内容的长度

​	注意:

​		会清除原有的内容,再写入新的内容

```python
a = open('a2.txt','w+')
b = a.write('how are you')
print(b)
a.seek(0)
```

### 2.写入文件序列

​	io对象.writelines(容器)

​	返回值:无

```python
li = ('床前明月光\n','地上鞋两双\n','床上狗男女\n','其中就有你\n')
li = {'床前明月光\n','地上鞋两双\n','床上狗男女\n','其中就有你\n'}
li = {'床前明月光\n':'地上鞋两双\n','床上狗男女\n':'其中就有你\n'}
li = ['床前明月光\n','地上鞋两双\n','床上狗男女\n','其中就有你\n']
b = a.writelines(li)
a.close()
print(b)
```

### 3.读取内容

​	io对象.read(n)

​	参数:

​		n如果不填,默认从当前指针开始,读取到末尾

​		n = 1,从当前指针开始,向后读取1位

​		n = 2,从当前指针开始,向后读取2位

​		.  .  .

​	返回值:读取的内容

```python
a = open('a3.txt','r')
b = a.read()
print(b)
```

### 4.读取一行内容

​	io对象.readline(n)

​	参数:

​		n如果不填,从当前指针开始,向后读取一行(不会到下一行)

​		n = 1,从当前指针开始,向后读取1位

​		n = 2,从当前指针开始,向后读取2位

​		如果当前行没有读取完毕,下一次的readline会接着上一次继续读

​		如果指定n时,已经超过当前行,那么不会读取下一行的内容,只会读取当前一行

​	返回值:一行内容

```python
a = open('a2.txt','r')
# 不指定n时
b = a.readline()
print(b)
# 指定n时
b = a.readline(2)
print(b)
```

### 5.读取所有内容到列表中

​	io对象.readlines()

​	每一行分配一个索引,存入列表中

​	第一行为索引0

​	第二行为索引1

​	.   .   .

```python
a = open('a3.txt','r')
b = a.readlines()
print(b)
```

### 6.截取文件内容

​	io对象.truncate(n)

​	功能:从开头向后截取n个字节,剩余没有被截取的将全部删除

​	返回值:返回截取的长度

```python
a = open('a3.txt','a')
b = a.truncate(2)
print(b)
```

### 7.刷新文件缓冲

​	io对象.flush()

​	功能:立马将缓冲区的内容存入文件中

​	返回值:无

​	平时文件的写操作,其他不会立马把内容写入文件,只是把内容存入缓冲区

**当满足以下任意条件时,即可将缓冲区内容存入文件中**

- 当整个程序自然结束时

- 当运行到flush时

- 当文件关闭时

- 当缓冲区填满了,将内容存入文件中,再刷新刷新缓冲

  利用Pycharm,通过断点调试来查看

### 8.浅谈with

​	在以上的操作,经常忘记close操作,导致内存在不断的浪费

​	with会在文件操作完之后,自动帮你关闭文件

```python
a = open('a4.txt','r')
print(a.read())
# 上面的a 没有关闭文件

with open('a4.txt','r') as file:
	print(file.read())
	pass
```





# 模块

### 1.定义

​	模块是一个包含所有自定义的函数,类和变量的文件

​	当模块被别的程序引入时,便可以使用该模块的任意函数和变量

​	Python系统标准库,也是这么引用的

### 2.格式

#### 2.1引用模块

​		import	模块名

​		模块名.方法名()

​		模块名.变量名

```python
import demo
print(demo.name)
print(demo.money)
demo.skill()
```

#### 2.2引用模块中的方法/变量

​		from 模块名 import 方法名

​		from 模块名 import 方法名1,方法名2, . . .

​		from 模块名 import 变量名

​		from 模块名 import 变量名1,变量名2, .  .  .

```python
from demo import skill
skill()

from demo import skill, skill2
skill()
skill2()

from demo import name
print(name)

from demo import name, money
print(name)
print(money)
```

### 3.路径

​	可以看到有以下几个目录:
​		有Python\     安装的根目录
​		有Python\DLLs 
​		有Python\lib
​		有Python\lib\site-packages\
​		当前目录下            (该运行文件的目录下)

### 4.`__name__`属性

​	作用:自动获取当前模块/引用模块的名字

​	如果是自身文件被运行, `__name__` 返回`__main__` 代表正在运行的是当前主程序

​	如果是被别的模块引入,`__name__`返回引入模块的名字





## 字符串模块 string

​	**简述:字符串相关的功能**

```python
import string
```

##### a = string.ascii_letters 	   #获取所有的字母(包含大小写)

##### a = string.ascii_uppercase   #获取所有的大写字母

##### a = string.ascii_lowercase  #获取所有的小写字母

##### a = string.digits 	                  #获取所有的数字(十进制)

##### a = string.octdigits 		  #获取所有的数字(八进制)

##### a = string.hexdigits 		  #获取所有的数字(十六进制)

##### a = string.punctuation 	  #获取ascii码中所有符号, 标点

##### a = string.whitespace 	  #获取所有的空白,空格,制表符,换行等

##### a = string.printable 		  #获取所有的字符



## random模块

```python
import random
#获取0~1之间的随机数 
a = random.random() 		#(0,1)含有小数
print(a) 

#获取0~1之间的随机数
a = random.randrange(0,2) 	#[0,2)
print(a)

#获取0~10之间的随机数  
a = random.randrange(0,11) 	#[0,10]
print(a)

#获取1~10 之间的随机整数
a = random.randint(1,10) 	#[1,10]
print(a)

# 获取1~10 之间的随机小数
a = random.uniform(1,10) 	#[1,10]
print(a)

# 从下列x中, 获取一个字符
# 	仅支持list, tuple, string
x = [1,2,3,4,'a','b','c','d']
x = (1,2,3,4,'a','b','c','d')
x = '1234abcd'
a = random.choice(x)

# 将列表a的值随机排序
a = [1,2,3,4,'a','b','c','d']
random.shuffle(a)
print(a)
```



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

#### time.process_time()

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

#### datetime.datetime.datetime.strftime(格式)

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

**super**( )**调用父级的方法**

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

##### 通过类来修改:

​		将会把类中的属性给修改掉

​		这会影响"所有"从 类实例化出去的对象 (拥有专属的除外)

##### 通过对象来修改:

​		一旦将类实例化, 生成一个对象,对象会拥有"独立的内存", 拥有类的所有属性和方法

- 只要不修改属性, 就会受到类的影响
- 一旦对象自己修改了属性, 那么这个属性是专属于对象,将不再受到类的影响

```python
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



## 类方法和实例方法

### 定义

​	**类方法**:通过**类名**来访问的方法

​	**实例方法**:通过**对象**来访问的方法

### 格式

#### 类方法格式

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



## 异常

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



## 单例模式

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



## 装饰器

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

