'''
	类方法 和 实例方法

'''

# 1. 定义
# 	类方法: 通过"类名"来访问的方法
# 	实例方法: 通过"对象" 来访问的方法


# 2. 格式
# 	
# 	类方法格式:
# 		@classmethod
# 		def 方法名(cls):
# 			代码块
# 			
# 			
# 	注意:
# 		1. 在方法名上一行必须添加 @classmethod
# 		2. 第一个参数必须设为cls.  功能类似于self.
# 			cls也不是关键字, 名字可以改
# 			
# 			cls 代表当前类名
# 			self 代表当前对象



class Doll():
	count = 0

	def __init__(self, name):
		self.name = name
		Doll.count += 1

	@classmethod 		# 类方法 装饰器
	def show_count(cls):
		print('已经有 %d 个人使用了该娃娃' % cls.count)
		print(cls)


	def test(self):
		print('我是实例方法')
		print(self) 
		# print(cls.count)
		print(Doll.count)
		Doll.show_count()

objA = Doll('小强')
objB = Doll('小龚')
objC = Doll('小杨')

Doll.show_count()
objA.show_count()
objB.show_count()
objC.show_count()

# Doll.test()
objA.test()


# 小结:
# 	类方法: 属于类
# 		可以通过类 	访问
# 		可以通过对象 访问
# 		只可以访问类属性
# 		一个类占一个内存
# 	
# 	实例方法: 属于对象
# 		可以通过对象 方位
# 		可以直接访问 实例属性
# 		可以间接访问 类属性 和 类方法
# 		一个对象占一个内存












