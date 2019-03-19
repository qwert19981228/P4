'''
	集合
	1. 定义
	2. 格式
	3. 基本操作
	4. 高级操作
	5. 遍历
	6. 推导式
'''

# 1. 定义
# 	一个值不会重复的无序序列
#  	
#  	主要作用:
#  		去重, 		将一个列表转为集合, 就会自动去重
#  		关系测试 	测试两个集合交集, 差集等


# 2. 格式
#  	变量名 = {值1, 值2, ...}
#   变量名 = set( (值1, 值2, ...)  )

a = set() 	# 空集合
print(a, type(a))

a = {} 		# 空字典
print(a, type(a))

a = {'安其拉', '王昭君', '妲己'}
print(a, type(a))

# set()  强制转为集合类型
a = set(  ('史珍香') ) 	# 当做一个字符串, 会将字符串的值一个一个拆分到集合中
a = set(  ('史珍香',) )  # 当做一个元组, 将值当成一个整体 送进集合中
a = set(  ['史珍香'] ) 	# 当做一个列表, 同上
print(a)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 小练习
# 	创建 a-f 的集合
a = 'abcdef' 		# 利用字符串一个一个拆分的特性来操作
b = set(a)
print(b)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 3. 基本操作
# 	3.1 交集 	& 	
# 	3.2 并集 	|
# 	3.3 差集     -
# 	3.4 成员检测  in


# 交集
a = set('abcd')
b = set('cdxy')
c = a & b
print(c)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 并集
a = set('abcd')
b = set('cdxy')
c = a | b
print(c)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 差集
a = set('abcd')
b = set('cdxy')
c = a - b 	# a 相对于b 的差集
c = b - a 	# b 相对于a 的差集
print(c)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 对称差集
a = set('abcd')
b = set('cdxy')
c = a ^ b 	# 除了交集不要, 其余都要
print(c)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



a = set('abcd')
b = 'a' in a
b = 'x' in a
b = 'x' not in a
print(b)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 4. 高级操作
# 	4.1 添加一个值
# 	4.2 删除一个值
# 	4.3 成员检测

a = set('abcd')
# 4.1 添加一个值
# 格式1:  集合.add(值)
a.add('x')
print(a)

# 格式2: 集合.update( 容器 )
a.update( {'m','n'} )
a.update( ('i','j') )
a.update( ['x','y'] )
print(a)

print(id(a))



# 4.2 删除一个值
# 格式: 集合.remove(值)
a.remove('a')
# a.remove('p') 	# 移除一个不存在的值, 则报错
print(a)

print(id(a))


# 格式: 集合.discard(值)
a.discard('b')
a.discard('p') 		# 移除一个不存在的值, 不会报错
print(a)


print(id(a))
# 集合 不能通过索引来访问
# 	集合 根本没有索引, 所以无法单独的访问
# 	可以通过遍历来一个一个的访问







