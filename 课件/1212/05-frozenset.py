'''
	冰冻集合
	1. 定义
	2. 格式
	3. 遍历
	4. 推导式
	5. 注意点
'''

# 1. 定义
#	一旦创建就无法再进行添加或删除的操作

# 2. 格式	
# 	变量名 = frozenset( 可迭代的对象 )
# 	
#  	可迭代对象: 暂时理解为 字符串, 列表, 元组 ...

a = frozenset() 	# 空冰冻集合, 一般情况下, 也不会干这种事
print(a, type(a))

a = frozenset( ['正太', '孟祥云', '萝莉', '小娜'] )
print(a)

# 尝试添加, 删除
# a.add('老不死', '宋捷文')
# a.remove('正太')


# 3. 遍历
a = frozenset( ['正太', '孟祥云', '萝莉', '小娜'] )
for i in a:
	print(i)


# 4. 推导式
#  	格式: 
# 		fronzenset( 变量操作 for 变量 in 集合  )   		
# 		fronzenset( 变量操作 for 变量 in 集合 if 条件)   		
#  		...
a = frozenset( ['正太', '孟祥云', '萝莉', '小娜'] )
print(id(a))
b = frozenset( '小'+i for i in a)
a = frozenset( '小'+i for i in a)
print(b)
print(a)
print(id(a))


# 5. 注意点
# 	普通集合: 可变类型
# 	冰冻集合: 不可变类型




