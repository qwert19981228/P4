'''
	OOP的三大特性:
	1. 封装性
	2. 继承性
	3. 多态性
'''

# 1. 封装性
# 	1.1 定义
# 		将属性和方法集中到一个类中, 形成一个不可分割的类
# 		封装后, 类内的属性和方法, 有的公开, 有的私有


#  	1.2 格式
#  		私有属性
#  		__属性名 = 值
#  		
#  		私有方法
#  		def __方法名(self):
#  			pass


#  	1.3 使用
#  		self.__属性名
#  		self.__方法名()
#  		
#  		限制: 只能在类内使用


#  	小结:
#  		默认属性和方法, 都是公开, 类内类外都可以访问
#  		私有属性和方法, 只能在类内使用
#  		
#  		定义一个类时, 如果不想让外边的人使用这个属性/方法, 就设置为私有的
#  		私有的常用于 内部的事情


class Person():
	name = '小宋'   # 公有属性
	__size = '3cm' 	# 私有属性, 在类外是无法访问


	def getname(self):  # 公有方法
		print('大家好, 我是 %s' % self.name)


	def __skill(self): 	# 私有方法
		print('%s 会偷电瓶车 ' % self.name)

	def test(self):
		print('在类内访问  : %s' % self.__size)
		self.__skill()


a = Person()
print(a.name)
#print(a.__size)


a.getname()
# a.__skill()


a.test()




