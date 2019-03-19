# 变量



## 变量的作用域

### 1.全局变量

在函数外部定义的变量

###    局部变量

在函数内部定义的变量

```python
a = 10 		# 全局变量
def test():
	b = 20  # 局部变量
```

### 2.作用域

#### 2.1局部作用域		local	L

#### 2.2闭包函数外的函数中enlosing E

#### 2.3全局作用域		global	G

#### 2.4内置作用域		built-in	B

查询规则:	L -> E -> G -> B

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

​	而在E区间中,单独写a = 15 ,仅仅是给E区间中声明一个新的变量a,该变量a 与全局a 内存 不一样

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
>

​	需要改变作用G中的变量,则通过global

​	需要改变作用E中的变量,则通过nonlocal





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

#### 	2.1直接调用	

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

#### 	2.2返回函数名

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





## 格式化函数

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

#### 	3.1访问列表

​	格式:

​		变量名[索引]

```python
a = ['狗不理','叉烧包','汤包','流沙包']
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])
```

#### 	3.2修改列表

​	索引存在时, 才能修改

​	索引不存在时, 则报错

```python
a[2] ='生煎包' 		
print(a)
```

#### 	3.3删除列表

```python
del a[2]
print(a) 		
print(a[2])
```

#### 	3.4插入列表

##### ​		3.4.1插入已有的索引

​		变量名.insert(索引,值)

```python
a.insert(2,'鲜肉包')
print(a)
print(a[2],a[3])
```

##### 				3.4.2插入不存在的索引

```python
a.insert(99, '灌汤包')
print(a)
print(a[4])
```

##### 				3.4.3插入最大的索引 或 在最后面加一个索引

​		变量名.append(值)

```python
a.append('蟹黄包')
print(a)
```

​		小结:

​			如果知道索引,用insert

​			如果只是想追加一个索引,用append

### 4.高级操作

#### 	4.1列表合并	+

```python
a = ['刘德华','张学友']
b = ['郭富城','黎明']
c = a + b
print(c)
```

#### 	4.2列表重复	*

```python
a = ['甄姬','曹丕']
b = a*3
print(b)
```

#### 	4.3列表分片	[start:stop:step]

```python
a = ['刘备','关羽','张飞','赵云','马超','黄忠','诸葛亮']
print(a[:]) 		# 从开头 ~ 末尾
print(a[2:]) 		# 从索引2 ~ 末尾
print(a[:2]) 		# 从开头 ~ 索引2 (不包含索引2)
print(a[2:5]) 		# 从索引2 ~ 索引5 (不包含索引5)
print(a[0:6:2]) 	# 从索引0 ~ 索引6, 步长为2 (不包含索引6)
```

#### 	4.4成员检测 in \not in

```python
a = ['刘备','关羽','张飞','赵云','马超','黄忠','诸葛亮']
b = '曹操' in a
b = '张飞' in a
b = '曹操' not in a
print(b)
```

### 5.遍历列表

#### 	5.1遍历1

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

#### 	5.2遍历2

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

#### 	修改嵌套列表

```python
a[0][1] = '杨玉环'
print(a)
```

### 7.推导式

#### 	7.1基本推导式

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

#### 	7.2条件推导式

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

#### 	7.3多循环推导式

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

#### 	7.4多循环条件推导式

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

#### 	3.1访问元组

```python
a = ('大圣','天蓬','卷帘','金蝉子')
print(a[0])
print(a[-1])
```

#### 	3.2修改元组

​		因为元组是不可变类型, 所以无法修改元组

#### 	3.3删除元组

​		因为元组是 不可变类型, 所以无法删除元组

#### 	3.4插入元组

​		因为元组是 不可变类型, 所以无法插入元组

### 4.高级操作

#### 	4.1合并

```python
a = ('佛祖','普度众生')
b = ('达摩','易筋经')
c = a+b
print(c)
```

#### 	4.2重复

#### 	4.3分片

#### 	4.4成员检测

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

#### 	3.1访问字典

```python
a = {'关羽':'云长','张飞':'翼德','刘备':'玄德'}
print(a['关羽'])
```

#### 	3.2修改字典

​		通过已有的键来修改字典

```python
a['关羽'] = '武圣'
print(a)
```

#### 	3.3插入字典

​		通过不存在的键来修改字典

```python
a['曹操'] = '孟德'
print(a)
```

#### 	3.4删除字典

​		通过已有的键来删除字典

​		如果键不存在,则报错

```python
del a['关羽']
print(a)
```

#### 	3.5成员检测

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

#### 	5.1基本推导式

​		格式:{键:值 for 键,值 in 字典.items()}

```python
# 需求:以下列格式进行是输出    绰号=xxx  大名=xxx
a = {'赵小刀':'赵丽颖','小笼包':'陈妍希','胖迪':'迪丽热巴'}
b = {'绰号='+k:'大名='+v for k,v in a.items()}
print(b)
```

#### 	5.2条件推导式

​		格式:{键:值 for 键,值 in 字典.items() if 条件}

```python
# 需求:只显示名字长度为4位的人 
a = {'赵小刀':'赵丽颖','小笼包':'陈妍希','胖迪':'迪丽热巴'}
b = {k:v for k,v in a.items() if len(v) == 4}
print(b)
```

#### 	5.3多循环推导式

​		格式:{键:值 for 键1,值1 in 字典1.items() for 键2,值2 in 字典2.items()}

```python
# 需求: 凑CP
a = {'赵小刀':'赵丽颖','小笼包':'陈妍希'}
b = {'小旋风':'林志颖','黑旋风':'李逵'}
c = {v1:v2 for k1,v1 in a.items() for k2,v2 in b.items()}
print(c)
```

#### 	5.4多循环条件推导式

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

#### 	3.1交集	&

```python
a = set('abcd')
b = set('cdxy')
c = a & b
print(c)
```

#### 	3.2并集	|

```python
a = set('abcd')
b = set('cdxy')
c = a | b
print(c)
```

#### 	3.3差集	-

```python
a = set('abcd')
b = set('cdxy')
c = a - b 	#a相对于b的差集
c = b - a 	#b相对于a的差集
print(c)
```

#### 	3.4对称差集	^

```python
a = set('abcd')
b = set('cdxy')
c = a ^ b 	#除了交集不要, 其余都要
print(c)
```

#### 	3.5成员检测  in\not in

```python
a = set('abcd')
b = 'a' in a
b = 'x' in a
b = 'x' not in a
print(b)
```

### 4.高级操作

#### 	4.1添加一个值

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

#### 	4.2删除一个值

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

#### 	6.1基本推导式

​		格式:{变量操作 for 变量 in 集合}

```python
# 需求: 给每一个值 都加 "小"字
a = {'马克思','马云','马化腾','马加爵','马蓉','马航','马冬梅'}
a = { '小'+i for i in a }
print(a)
```

#### 	6.2条件推导式

​		格式:{变量操作 for 变量 in 集合 if 条件}

#### 	6.3多循环推导式

​		格式:{变量操作 for 变量1 in 集合1 for 变量2 in 集合2}

#### 	6.4多循环条件推导式

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

#### 	3.1map

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

#### 	3.2sorted

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

#### 	3.3filter

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

#### 	3.4reduce

​		reduce(func,iterable)

​		**功能:对iterable的每一个对象进行累计操作****

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

#### 	2.1引用模块

​		import	模块名

​		模块名.方法名()

​		模块名.变量名

```python
import demo
print(demo.name)
print(demo.money)
demo.skill()
```

#### 	2.2引用模块中的方法/变量

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

### 4.__name__属性

​	作用:自动获取当前模块/引用模块的名字

​	如果是自身文件被运行, __name__ 返回 __main__ 代表正在运行的是当前主程序

​	如果是被别的模块引入,__name__返回引入模块的名字





## String模块

​	**简述:字符串相关的功能**

```python
import string
a = string.ascii_letters 	#获取所有的字母(包含大小写)
a = string.ascii_uppercase  #获取所有的大写字母
a = string.ascii_lowercase  #获取所有的小写字母
a = string.digits 			#获取所有的数字(十进制)
a = string.octdigits 		#获取所有的数字(八进制)
a = string.hexdigits 		#获取所有的数字(十六进制)
a = string.punctuation 		#获取ascii码中所有符号, 标点
a = string.whitespace 		#获取所有的空白,空格,制表符,换行等
a = string.printable 		#获取所有的字符
```



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

