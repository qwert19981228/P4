'''
	操作类
	1. 类外
	2. 类内
'''


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

		self.age = 50 	# 类内修改属性
		print(self.age)
		self.desc = '666, 有钱自己造一个' 	# 类内新增属性
		print(self.desc)

	# 小结:
	# 	给属性赋值, 若属性已存在, 即为修改
	# 			   若属性不存在, 即为新增
	# 	
	# 	不推荐在类外 修改或新增属性
	# 	(原因: OOP有封装性, 如果在类外修改或新增, 就违反了OOP的特性)


# 1. 类外
a = Plane()

a.name = '中国歼击机' 		# 在类外, 修改属性
print(a.name)  				# 在类外, 新增属性
a.nickname = '最牛逼的战斗机'
print(a.nickname)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

a.test()


print(a.age)

