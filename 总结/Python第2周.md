# 数据类型



## 浮点（float）

### 1.值 

由整数 + 小数组成，中间以  .  作为分割

```python
num = 1
num = True
print(num,type(num))
```

## 2.科学计数法

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
>

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

可用于表达数字，字母，标点，汉字。。。汉字描述

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

#### 	3.1 单双引号可以互插,不能自插

```python
#a = 'I give you face,but you dont't want to face'
a = "I give you face,but you dont't want to face"
#a = "I give you face,but you dont"t want to face"
#a = 'I give you face,but you dont"t want to face'
```

#### 	3.2 转义符号    \

​	作用:将普通符号转为特殊符号

​	例如:	\n  换行

​			 \r  回车

​			 \t  制表符   Tab

```python
a = '上面\n下面'
a = "上面\n下面"
print(a)
```

#### 	3.3 原始字符串

​	在引号外面加 r 或 R,那么该字符串将会原样输出,不会解析任何字符

```python
a = r"上面\n下面"
a = R"上面\n下面"
print(a)
```

#### 	3.4 字符串格式化

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

#### 	3.5字符串操作

##### 		3.5.1  拼接

​		用于变量与变量

​		用于变量与字符串

```python
a = '金庸小说:'
b = '飞雪连天射白鹿,笑书神侠以倚碧鸳'
c = a + b
print(c)
```

##### 		3.5.2  复制 *

```python
a = '母鸡'
b = a * 3
print(b)
```

##### 		3.5.3  索引 []

```python
a = '123456789'
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
```

##### 		3.5.4  取片 [:]

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

#### 	3.1访问列表:通过索引来访问

```python
print(food[0])
print(food[-3])
```

​	注意:访问不存在的索引,则报错

#### 	3.2插入列表

##### 		3.2.1 变量名.insert(索引,值)

​		分析:

​			如果索引不存在,按已有最大索引 +1 计算

​			如果索引已存在,插入指定索引,原有的索引依次向后推1

```python
food.insert(5,'四川麻辣烫')
print(food)
print(food[3])
```

##### 		3.2.2 变量名.append(值)

​		分析:

​			append 只会插入最后面

```python
food.append('过桥米线')
print(food)
print(id(food))
```

#### 	3.3修改列表

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

#### 	3.4 删除列表

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

#### 	4.1complex(real,imag=0)

​	虚数默认为0

#### 	4.2实数

#### 	4.3字符串复数

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

#### 	2.1取模结果:正负取决于第二位数

```python
print(10%4)
print(10%-4)
print(-10%-4)
print(-10%4)
```

#### 	2.2取模范围:

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

#### 	1.1单一赋值

​		先算=右边的,再算=左边的

#### 	1.2连续赋值

```python
a = b = c = 20
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))
```

#### 	1.3多段赋值

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

​	条件成立,则进入true环境

​	条件不成立,则结束循环,准备执行while外面的代码

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

#### 	3.1小写单词

```python
def getmessage():
	print('苍老师发来的邀约信息')
getmessage()
```

#### 	3.2下划线

```python
def get_message():
	print('波老师发来的邀约信息')
get_message()
```

### 4.注意点

#### 	4.1函数重名

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

#### 	4.2 函数名意义

​		为了后期的维护,提高的代码的可读性,函数名最好通俗易懂

​		看到名字就大致知道什么功能

​		惯性:

​			函数名习惯以  动词 + 名词   形式出现





## 返回值

### 1.关键字

​	return

### 2.作用

#### 	2.1将函数中的值,返回到调用

#### 	2.2提前结束函数,并返回,return后面的代码将不再执行

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

#### 	3.1值的类型

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

#### 	3.2多返回值

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

#### 	3.3无返回值

​			如果函数没有return,默认返回None





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

#### 	2.1传值和传址

​		传值:仅仅是将值传递过去

​		传址:不仅将值传递过去,而且将内存地址传递过去

#### 	2.2	区分:

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

#### 	3.1必须参数

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

#### 	3.2关键字参数

​		实数指定参数名来传入

​		好处:不用按照顺序来传入

```python
def test(name, age, sex):
	print('名字: %s' % name)
	print('年龄: %s' % age)
	print('性别: %s' % sex)

test(age=20, sex='人妖', name='杜子腾')
```

#### 	3.3默认参数

​		即便实参没有传值,形参可以采用默认值

```python
def test(name, age = 18, sex = '人妖'):
	print('名字: %s' % name)
	print('年龄: %s' % age)
	print('性别: %s' % sex)
test('二狗', 800)
```

#### 	3.4不定长参数

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

​	lambda    形参:返回值

​	冒号左边:想要传递的参数

​	冒号右边:需要return的结果

​	注意:lambda是一个表达式,并非语句,用在的话不能用的地方

> ​	小结:
>

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

