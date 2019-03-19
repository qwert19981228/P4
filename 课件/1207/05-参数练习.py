# 
# 题1:
# 	自定义函数 abs().  功能需要一致	
def set_abs(n):

	# 原始版本
	# if n < 0:
	# 	n = -n
	# 	return n
	# else:
	# 	return n

	# 优化版
	if n < 0:
		n = -n
	return n

print( set_abs(-5) )
print( set_abs(5) )
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 题2:
# 	输出多行星阵图

# *
# **
# ***

def star(n, bz=1):

	if bz == 1:
		for x in range(n):
			for y in range(x+1):
				print('*', end='')
			print()
	elif bz == 2:
		for x in range(n):
			for y in range(n-x):
				print('*', end='')
			print()
	elif bz == 3:
	elif bz == 4:



star(5)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
star(3)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
star(10,2)











