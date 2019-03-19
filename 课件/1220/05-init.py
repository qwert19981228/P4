'''
	类的专属方法 (魔术方法)
	1. 构造方法
	2. 析构方法
'''

# 类的专属方法:
# 	普通方法, 不调用不会主动执行
# 	专属方法, 触发指定条件, 就会自动执行



# 1. 构造方法
# 	1.1 触发条件: 实例化类时
# 	1.2 主要作用:
# 		1) 设置初始化属性
# 		2) 改变初始化属性
# 	
# 	小结:
# 		有了 __init__,  类才能变得更加通用




class Book():
	def __init__(self):
		print('准备要初始化Book类')

a = Book()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



class Book():
	def __init__(self, name, author, price):
		self.name = name 		# 新增属性 name (书名)
		self.author = author 	# 新增属性 auther (作者)
		self.price = price 		# 新增属性 price (单价)



a = Book('金瓶梅', '黄龙', 188)
b = Book('金瓶梅2', '杨加旺', 68)
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


print('%s 由 %s 精心编写, 零售价 %d 元' % (a.name, a.author, a.price))
print('%s 由 %s 精心编写, 零售价 %d 元' % (b.name, b.author, b.price))




a.price *= 0.1
print('%s 由 %s 精心编写, 零售价 %d 元' % (a.name, a.author, a.price))











