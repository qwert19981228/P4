'''
	类的专属方法 (魔术方法)
	1. 构造方法
	2. 析构方法
'''

# 类的专属方法:
# 	普通方法, 不调用不会主动执行
# 	专属方法, 触发指定条件, 就会自动执行


# 2. 析构方法
# 	触发条件: 当对象被销毁的时候
# 			  有以下几种销毁场景:
# 			  1) 当程序自然结束时
# 			  2) 当对象被删除时
# 			  3) 当对象被覆盖时
# 	
# 	
# 	主要作用: 在销毁之前, 做一些遗嘱


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

# del a
a = '光头强'


print('-'*50)