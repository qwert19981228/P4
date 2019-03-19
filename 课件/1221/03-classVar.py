'''
	类属性 和 实例属性
	1. 定义
	2. 访问
	3. 修改
'''


# 1. 定义
# 	通过类   来访问的属性, 都叫做"类属性",  别称"类变量"
# 	通过对象 来访问的属性, 都叫做"实例属性", 别称"实例变量"

# 	作用
# 		类属性: 资源共享
#  		实例属性: 资源独享

class Person():
	name = '小龙'


# 2. 访问
print(Person.name) 	# 类属性
a = Person()
b = Person()
print(a.name) 		# 实例属性
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 3. 修改
Person.name = '神龙'
print(Person.name)
print(a.name)
print(b.name)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


a.name = '大龙'
print(Person.name)
print(a.name)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


Person.name = '火龙'
print(Person.name)
print(a.name)
print(b.name)



# 分析:
# 	通过类 来修改:
# 		将会把Person类中的name 给修改掉.
# 		这会影响"所有"从 Person 实例化出去的对象 (拥有 专属的除外)

# 	通过对象 来修改:
# 		一旦将Person 实例化, 生成一个对象a. 对象a 会拥有"独立的内存", 拥有Person类的所有属性和方法
# 		1) 只要不修改属性, 就会受到 Person的影响
# 		2) 一旦对象a 自己修改了属性, 那么这个属性是 专属于对象a. 将不再受到Person 的影响
# 		
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 案例:
# 	统计 徐烈强 一共和几个人几个吃过饭?

class 徐烈强():
	count = 0

	def __init__(self, name):
		self.name = name 	 # self是对象.   对象.name ==> 实例属性
		徐烈强.count += 1 	 # 徐烈强是类.    类名.name  ==> 类属性
		#self.count += 1



objA = 徐烈强('龚顺义')
objB = 徐烈强('杨加旺')
objC = 徐烈强('孟祥云')

print(objA.name)
print(objB.name)
print(objC.name)
# print(徐烈强.name)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print(徐烈强.count)
print(objA.count)
print(objB.count)
print(objC.count)











