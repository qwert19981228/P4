'''
	循环结构
		for循环
'''

# 循环3
# 	for 变量 in 数字区间:
#  		代码块
#  	
#  	
#  	数字区间:
#  		range(start, stop, step)
#  			
#  		参数:
#  			start: 从start开始, 默认从0开始
#  			stop: 到stop结束, 不包括stop
#  			step: 步长, 默认为1

# 输出 0-9
for i in range(0,10):
	print(i, end=" ")

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for i in range(10):
	print(i, end=" ")

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for i in range(0,10,3):
	print(i, end=" ")

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 其余用法

a = ['貂蝉', '西施', '王昭君', '杨玉环']
a = '123456789';
a = 'abcdefg';
print(  len(a)  ) 	# len()  获取变量的总长度
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#    0  	 1 		 2 		   3
a = ['貂蝉', '西施', '王昭君', '杨玉环']
length = len(a)


for i in range( length ):
	print(i, a[i])

# 分析:
# 	通过range() 来实现遍历 list, tuple, set
# 	获取 索引 和 值
# 	
# 	如果单纯的直接遍历list, tuple ...
# 	只能获取到 值