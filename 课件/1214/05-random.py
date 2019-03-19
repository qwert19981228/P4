'''
	随机模块
'''

# 1. random 模块
# 	简述: 随机数模块

import random

# 获取0~1之间的随机数 
a = random.random() 		# (0,1) 	含有小数
print(a) 

# 获取0~1之间的随机数
a = random.randrange(0,2) 	# [0,2)
print(a)


# 获取0~10之间的随机数  
a = random.randrange(0,11) 	# [0,10]
print(a)

# 获取1~10 之间的随机 整数
a = random.randint(1,10) 	# [1,10]
print(a)

# 获取1~10 之间的随机 小数
a = random.uniform(1,10) 	# [1,10]
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 从下列x中, 获取一个字符
# 	仅支持list, tuple, string
x = [1,2,3,4,'a','b','c','d']
x = (1,2,3,4,'a','b','c','d')
# x = {1,2,3,4,'a','b','c','d'}
x = '1234abcd'
a = random.choice(x)
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 将列表a 的值随机排序
a = [1,2,3,4,'a','b','c','d']
random.shuffle(a)
print(a)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


import string
import random
# 练习题:
# 	1. 随机获取一个小写字母
a = string.ascii_lowercase
print( random.choice(a) )

# 2. 随机获取一个大写字母
a = string.ascii_uppercase
print( random.choice(a) )


# 3. 随机获取一个数字 0-9
a = string.digits
print( random.choice(a) )

# 4. 随机获取一个数字 或 字母
a = string.ascii_letters + string.digits
print( random.choice(a) )

