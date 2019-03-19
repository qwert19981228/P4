'''
	装饰器
'''

# 1. 什么是装饰器
# 	本质是一个函数
# 	
# 	作用: 在不影响原有函数的基础上, 给函数扩展功能, 使用起来更强大
# 	(俗称: 装饰,  跟装饰品一样, 人配以一些装饰器, 看起来人更加好看一些)



# 案例1:
# 	有一只 东北虎, 现在要装一对翅膀, 来装饰自己
# --------------------------------------------------


# 原始写法 (回顾知识: 闭包)
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
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 分析:
# 	执行顺序:
# 		1) 先调用 wing(tiger)   将tiger作为参数传给wing
# 		2) 进入wing, 直接返回函数angel  (此时没有调用angel)
# 		3) 回到调用函数的地方, a = angel
# 		4) a()  ==>  angel()  调用angel
# 		5) 生成变量 things = 天使翅膀
# 		6) name = func() ==> name = tiger()  调用tiger函数
# 		7) 在tiger中, 生成变量name = 东北虎
# 		8) 返回name 到angle中的 name=func()
# 		9) name = func() => tiger() => 东北虎
# 		10) 执行print, 执行输出
# 
#  综上所述: 高阶函数 + 闭包函数 = 装饰器


# 装饰器写法
# --------------------------------------------------
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

# 分析:
# 	仅仅是将 wing(tiger) 写在定义函数 tiger的上方.  代表用wing 来装饰tiger

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')




# 扩展:
# 	想加个皇冠, 能更好的体现东北虎  高大的形象

def hat(func):
	def crown():
		things = '黄金镶钻王冠'
		name = func()
		print('一个拥有 %s 的 %s ' % (things, name))
	return crown

@hat
def tiger():
	name = '东北虎'
	return name

tiger()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 一次性加多个装饰器

def wing(func):
	def angel():
		things = '天使翅膀'
		name = func() 		 # name = crown()  ==> name = None
		print('一个拥有 %s 的 %s ' % (things, name))
	return angel

def hat(func):
	def crown():
		things = '黄金镶钻王冠'
		name = func()
		print('一个拥有 %s 的 %s ' % (things, name))
		return name
	return crown

@wing
@hat
def tiger():
	name = '东北虎'
	return name

tiger()

# 分析
# 	
# 	在tiger上面, 有多个装饰器, 那么离tiger越近, 就优先执行哪个装饰器
# 	
# 	执行顺序:
# 		1) xxx = hat(tiger) 	==>  xxx = crown
# 		2) yyy = wing(xxx) 		==>  yyy = wing(crown)
# 		3) yyy()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 装饰器 (带参数)
# --------------------------------------------------

# 案例2: 
# 	有很多品种的老虎, 都想用些东西来装饰自己


def wing(func):
	def angel(x):
		things = '天使翅膀'
		name = func(x) 		 # name = tiger()
		print('一个拥有 %s 的 %s ' % (things, name))
	return angel

@wing
def tiger(name):
	return name

tiger('西伯利亚虎')
tiger('华南虎')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def wing(func):
	def angel(x):
		things = '天使翅膀'
		name = func(x) 		 # name = tiger()
		print('一个拥有 %s 的 %s ' % (things, name))
	return angel


def hat(func):
	def crown(x):
		things = '黄金镶钻王冠'
		name = func(x)
		print('一个拥有 %s 的 %s ' % (things, name))
		return name
	return crown

@wing
@hat
def tiger(name):
	return name


tiger('西伯利亚虎')
tiger('华南虎')
