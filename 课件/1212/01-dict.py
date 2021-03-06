'''
	字典
	1. 定义
	2. 格式
	3. 基本操作
	4. 遍历字典
	5. 字典推导式
'''

# 1. 定义
# 	一堆由  键值对 组成的可变类型


# 2. 格式
# 	变量名 = {键:值, 键:值, ... }
# 	键:
# 		* 支持数字, 字母.  推荐用字母, 少用数字
# 		* 必须唯一,  如果不唯一, 后面的会覆盖前面的
# 		* 必须是不可变类型
# 		* 不能为空, 必须写
# 	
# 	值: 任意类型

a = {}
print(a, type(a)) 	# 空字典

a = {'关羽':'云长', '张飞':'翼德', '刘备':'玄德'}
print(a, type(a))

a = {1:2, 3:4, 5:6}
print(a, type(a))

a = {1.2:2, 3.3:4, 5.2:6}
print(a, type(a))

a = {True:2, False:4, True:6}
print(a, type(a))

# a = {.:1, !:2, $:3}
# print(a, type(a))

# a = {:2, False:4}
# print(a, type(a))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 3. 基本操作
# 	3.1 访问字典
# 	3.2 修改字典
# 	3.3 插入字典
# 	3.4 删除字典
#   3.5 成员检测

# 3.1 访问字典, 通过键 来访问
a = {'关羽':'云长', '张飞':'翼德', '刘备':'玄德'}
print(a['关羽'])
# print(a[0]) 		# 不再是值字典中的第一个值了,  而是键为0的值
# print(a['xxx']) 	# 键不存在时, 则报错

# 3.2 修改字典
# 	通过已有的键 来修改字典
a['关羽'] = '武圣'
print(a)

# 3.3 插入字典
# 	通过不存在的键, 来插入字典
a['曹操'] = '孟德'
print(a)


# 3.4 删除字典
# 	通过已有的键 来删除字典
#  	如果键 不存在, 则报错
del a['关羽']
print(a)

# del a['诸葛亮']


# 3.5 成员检测
print( '张飞' in a )
print( '关羽' in a )
print( '关羽' not in a )
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 4. 遍历
a = {'关羽':'云长', '张飞':'翼德', '刘备':'玄德'}

for i in a:	
	# i 	获取的键
	# a[i] 	获取的值	
	print(i, a[i])
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 直接获取键 和 值
for i,j in a.items():
	print(i, j)


# 单纯的遍历键
for i in a.keys():
	print(i)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 单纯的遍历值
for i in a.values():
	print(i)


def sushu(x):
	for i in range(2,x):
		if x%i == 0:
			return False
	return True
b = list(   filter(    sushu,range(2,101)     )   )
print(b)

from functools import reduce

a = [1,2,3,4,5]
b = reduce(lambda x,y:x+y,a)
print(b)



