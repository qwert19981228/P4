'''
	OOP三大特性:
	1. 封装性
	2. 继承性
	3. 多态性
'''


# 2. 继承性
# 	2.1 定义
# 	2.2 格式
# 	2.3 特性


# 2.1 定义
# 	子类继承父类的一些东西
# 	
# 	子类: 派生类, 扩展类
# 	父类: 基类
#  	
#  	优点: 	
#  		提高代码的重用性, 降低冗余率


# 2.2 格式
# 	class 子类(父类):
# 		代码块


class Gumu():
	name = '古墓派'

	def skill1(self):
		print('玉女心经')

	def skill2(self):
		print('御蜂之术')



class Man(Gumu):
	name = '杨过'

	def skill3(self):
		print('蛤蟆功')

class Woman(Gumu):
	name = '小龙女'

	def skill3(self):
		print('左右互搏术')

a = Man()
b = Woman()

a.skill1()
a.skill2()
a.skill3()

b.skill1()
b.skill2()
b.skill3()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 2.3 特性
# 	1) 可以继承属性和方法 (不能继承私有属性和方法)
# 	2) 可以重写属性和方法
# 	3) 支持单继承, 连续继承, 多继承




# 1) 继承
# 	小技巧:
# 		对于man类,  不能直接访问Gumu的私有属性和方法
# 		对于Gumu类, 直接访问Gumu自己id私有属性和方法
# 		
# 		技巧:
# 			man调用Gumu的公有方法, 在公有方法中调用私有属性和方法(间接调用)

class Gumu():
	name = '古墓派'
	__age = 100

	def skill1(self):
		print('玉女心经')
		print(self.__age)


class Man(Gumu):
	
	def skill9(self):
		print(self.name)
		# print(self.__age)


a = Man()
print(a.name)
a.skill1()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
a.skill9()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 2) 重写
# 	可以重写属性 和 方法
# 	
# 	若果已经重写了父级方法, 在后期发现还需要用到父级的方法. 
# 	那么通过 super().父级方法名() 来调用
# 	
# 	super() 可以调用父级的属性和方法

class Gumu():
	name = '古墓派'

	def skill1(self):
		print('玉女心经')

	def skill2(self):
		print('御蜂之术')


class Man(Gumu):
	name = '杨过' 	# 重写父级同名属性

	# 可以重写方法
	def skill1(self): 	# 这里仅仅是在Man类中 覆盖Gumu的skill1方法. (Gumu类的skill1本身不受影响)
		super().skill1() 
		super().skill2()
		print('黯然销魂掌')

		print(super().name)
		print(super()) 	# super() 既代表Man类, 也代表Man对象


a = Man()
print(a.name)
a.skill1()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 3) 单继承


class Father():
	name = '老王'

	def skill1(self):
		print('穿墙')



class Son(Father):
	name = '小宋'


a = Son()
print(a.name)
a.skill1()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 3) 连续继承
# 	儿子继承老子,  孙子继承儿子,  曾孙子继承孙子,  重孙子继承曾孙子 ...
class Father():
	name = '老王'

	def skill1(self):
		print('穿墙')

class Son(Father):
	money = 50000000

	def skill2(self):
		print('造钱')	

# 孙子 可以使用Son 和 Father的属性和方法
class Grandson(Son):
	pass
	# name = '小宋'
	# money = 5
	# def skill1(self):
	# 	print('透视')

	# def skill2(self):
	# 	print('花钱')

a = Grandson()
print(a.name)
print(a.money)
a.skill1()
a.skill2()
# 
# 注意:
# 	
# 	 		/-- 大儿子  <--  孙子
# 	老子 <-- 
# 	 		\-- 小儿子
# 	
# 	孙子可以使用 大儿子和老子的属性和方法
# 	孙子不能使用 小儿子的属性和方法
# 	
# 	孙子 和 小儿子没有继承关系


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# 3) 多继承
# 
# 	格式: 
# 	class 类名(父类1, 父类2, 父类3, ...)
# 		代码块

class 小龙女():
	name = '小龙女'

	def skill1(self):
		print('玉女剑法')

	def skill9(self):
		print('九阴真经-正版')


class 欧阳锋():
	name = '欧阳锋'

	def skill2(self):
		print('蛤蟆功')


	def skill9(self):
		print('九阴真经-盗版')


class 大雕():
	name = '神雕'
	def skill3(self):
		print('玄铁剑法')

class 杨过(小龙女, 欧阳锋, 大雕):
	name = '杨过'

# 杨过 继承了 小龙女, 欧阳锋和大雕的属性和方法
a = 杨过()
a.skill1()
a.skill2()
a.skill3()
print(a.name)

a.skill9() # 当继承多个父类时, 有重名方法, 按照先继承的为准
# 杨过在继承时, 按照从左向右的顺序依次继承
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 继承顺序
# 	查看多继承时, 是按照什么样的顺序来找属性和方法的
# 	
# 	内置方法: __mro__ 		方法搜索顺序
# 	使用格式:
# 		类名.__mro__
# 
# 
# 
# 分析:
# 	结果: 元组类型
# 	元组第一个是 杨过类, 第二个是小龙女类, 第三个是欧阳锋类, 第四个是大雕类, 第五个是 object类
# 	
# 	(从左向右 搜索法)
# 	可以理解为, 在使用杨过类时, 在第一个类找不到 需要的属性和方法时, 就去第二个, 后面就以此类推
# 							  在第一个类找到了, 就不去第二个类找
# 							  如果到了最后都找不到, 则 报错
# 
# 问题:
# 	杨过在多继承时, 根本没写 object, 但是在mro中, 最后一个多了个object类
# 	在Python3, 所有类的最终基类, 都是object. 只是python3 默认最终基类为object, 在语法给省略了
# 	
#  	哪怕类名() 的小括号中, 没有写东西, 也继承了 object类
# 
# 

print(杨过.__mro__)
# print(杨过.xxx)

