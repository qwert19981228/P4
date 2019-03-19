'''
	列表 list
	1. 定义
	2. 格式
	3. 基本操作
	4. 高级操作
	5. 遍历
	6. 嵌套列表
	7. 推导式
'''

# 4. 高级操作
# 	4.1 列表合并
# 	4.2 列表重复
# 	4.3 列表分片
# 	4.4 成员检测 

# 4.1 列表合并 +
a = ['刘德华', '张学友']
b = ['郭富城', '黎明']
c = a + b
print(c)

# 4.2 列表重复 * 
a = ['甄姬', '曹丕']
b = a*3
print(b)

# 4.3 列表分片 [start:stop:step]
#    0       1 		 2 		 3 		 4 		5 		6
a = ['刘备', '关羽', '张飞', '赵云', '马超', '黄忠', '诸葛亮']
print(a[:]) 		# 从开头 ~ 末尾
print(a[2:]) 		# 从索引2 ~ 末尾
print(a[:2]) 		# 从开头 ~ 索引2 (不包含索引2)
print(a[2:5]) 		# 从索引2 ~ 索引5 (不包含索引5)
print(a[0:6:2]) 	# 从索引0 ~ 索引6, 步长为2 (不包含索引6)

# 4.4 成员检测 
# 	in
# 	not in
a = ['刘备', '关羽', '张飞', '赵云', '马超', '黄忠', '诸葛亮']
b = '曹操' in a 	# x
b = '张飞' in a # √
b = '曹操' not in a 	# √
print(b)









