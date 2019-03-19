'''
	返回值
	1. 关键字
	2. 作用
	3. 返回类型
'''

# 1. 关键字: return 


# 2. 作用
# 	2.1 将函数中的值  返回到调用函数的地方
# 	2.2 提前结束函数, 并返回, return 后面的代码将不再执行

def test():
	x = 100
	y = 200
	sum = x + y

a = test()
print(a) 	# None  什么都没有, 空


def test():
	x = 100
	y = 200
	sum = x + y
	return sum

a = test()   	#  a = 300
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def test():
	x = 100
	y = 200
	sum = x + y
	return sum
	print(x)

a = test()   	#  a = 300
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 3. 返回类型
# 	3.1 值的类型
# 	3.2 多返回值
# 	3.3 无返回值

# 3.1 
# 	return 可以返回任意类型
def test():
	return '张全蛋'
	return {1:2,3:4}
	return {1,2,3}
	return (1,2,3)
	return [1,2,3]
	return 1+2j
	return True
	return 100.5
	return 100

print( test() )
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 3.2 多返回值
# 	return 值1, 值2, ... 	
# 	return [值1, 值2, ...]	
# 	return {值1, 值2, ...}	
# 	
# 	需要一次性返回多个值:
# 		1) 将多个值 以逗号隔开
# 		2) 将值 包装到list, tuple, set 中

def test():
	x,y,z = 100, 5.5, 'abc'
	# return x,y,z 	# 一次性返回多个值, 以元组的形式返回
	# return [x,y,z]
	# return {x,y,z}
a = test()
print(a, type(a))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 3.3
# 	如果函数 没有return, 默认返回None




