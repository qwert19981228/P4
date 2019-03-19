'''
	高阶函数
	1. 定义
	2. 作用
	3. 使用
'''


# 注意点:
# 	高阶函数, 以函数作为参数时, 千万不要给函数加(),  一旦加(), 就不是送函数参数, 而是调用函数


# 3. 使用
# 	3.1 map()
# 	3.2 sorted()
# 	3.3 filter()
# 	3.4 reduce()


# 3.2 
# 	sorted(iterable, key=func, reverse=Bool )
# 	功能: 将可迭代对象进行排序, 生成排好的序列
# 	
# 	参数:
# 		iterable: 可迭代对象
# 		key: 排序依据, 常用函数
# 			 如果没有key, 默认使用iterable的值 进行排序
# 			 key默认为 None
# 			 
# 		reverse: 升序/降序
# 				升序: False 默认
# 				降序: True
# 	返回值: 排好序的可迭代对象


# 需求1:
# 	按照 值的大小 排序
a = set('12345678')
print(a)
b = sorted(a) 	# key, reverse 都是采用的默认值
print(b)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 需求2:
# 	将值取绝对值 并排序
a = [8,1,3,-4,6,7,2,5]
print(a)

b = sorted(a, key=abs)
print(b)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 需求3:
#  	按照名字的长短 排序

# 原版
a = ['范冰冰', '迪丽热巴', '杨幂']
def getlen(x):
	return len(x)

b = sorted(a, key = getlen)  
print(b)


# 优化版
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
a = ['范冰冰', '迪丽热巴', '杨幂']

b = sorted(a, key = lambda x: len(x))
print(b)
# 分析:
# 	key = lambda x: len(x)
# 	主要是将 可迭代对象中的值, 一个一个送进lambda, 并返回函数处理后的结果, 且作为此次排序的依据
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 需求4:
# 	按照 值的大小来排序
a = set('12345768')
print(a)

b = sorted(a, reverse=False)
b = sorted(a, reverse=True)
print(b)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 需求5:
# 	将值取反 再排序
# a = [5,2,4,1,8]
a = {1,2,3,4,5,6,7,8}
print(a)

def myreverse(x):
	return x*-1

# b = sorted(a, key=myreverse)
b = sorted(a, key= lambda x:x*-1, reverse=True)
print(b)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')





# 3.3 
# 	filter(func, iterable)
# 	
# 	功能: 过滤迭代器中的数据, 返回符合条件的可迭代对象
# 		  函数将可迭代对象中的数据进行判断, True 则保留, 否则抛弃
# 		  注意点:
# 		  	func 需要返回bool, 外部filter才能知道是否保留
# 	
# 	参数:
# 		func: 内置 或 自定义
# 		iterable: 可迭代对象
# 	
# 	返回值:
# 		对象
# 	

# 需求1:
# 	以列表形式输出 1~10 之间的偶数

# 原版
def iseven(x):
	return x%2==0
b = list( filter(iseven, range(1,11)) )
print(b)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 优化版
b = list( filter(lambda x:x%2==0, range(1,11)) )
print(b)


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 需求2:
# 	以列表形式输出 2~100 之间所有的素数(质数)
def isprime(x):
	for i in range(2,x):
		if x%i == 0:
			return False
	return True

b = list( filter(isprime, range(2,101)  ) )
print(b)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 3.4
# 	reduce(func, iterable)
#  	功能: 对iterable的每一个对象进行累计操作
#  	参数:
#  		func: 内置 或 自定义
#  			  要求: 每次必须送两人进函数, 形参必须设置两个
#  		
#  		iterable: 可迭代对象
#  	返回值: 计算之后的值
#  	
#  	
#  	注意:
#  		reduce 不是内置函数, 所以不能直接调用
#  		 	   必须提前引入模块 functools   
from functools import reduce

a = [1,2,3,4,5]
def add(x,y):
	return x+y

b = reduce(add, a)
print(b)






