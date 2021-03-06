'''
	多重循环
		定义: 在循环中, 嵌套循环
'''

# 星阵图设计: 先看行, 再看列
# 
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********



# while 版
# 
# 		y=0, 增量1
# x=0 	y<1
# x=1 	y<2
# x=2 	y<3
# ...
# x=9 	y<10
# 
# 		y<x+1


x = 0
while x < 10:

	y = 0
	while y < x+1 :
		print('*', end="")
		y += 1

	print() 	# 在换行之前, 根据 行数决定输出几颗*  
	x += 1

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# for 版
for x in range(10):
	for y in range(x+1):
		print('*', end="")
	print()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *


#  			y=0, 增量1
# x=0 		y<10
# x=1 		y<9
# x=2 		y<8   10-x
# ...       ...
# x=9 		y<1   10-x


for x in range(10):
	for y in range(10-x):
		print('*', end="")
	print()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')




#          *
#         **
#        ***
#       ****
#      *****
#     ******
#    *******
#   ********
#  *********
# **********


for x in range(10):

	# 控制 空格
	for y in range(10-x):
		print(' ', end="")


	# 控制 *
	for y in range(x+1):
		print('*', end="")

	# 换行
	print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# **********
#  *********
#   ********
#    *******
#     ******
#      *****
#       ****
#        ***
#         **
#          *

for x in range(10):
	# 控制 空格
	for y in range(x+1):
		print(' ', end="")

	# 控制 *
	for y in range(10-x):
		print('*', end="")

	# 换行
	print()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# *
# **
# ***
# ****
# ***
# **
# *
# 
# abs(变量) 		给变量取 绝对值

# 
#  			y=0, 增量1
# x=-3 		y<1   4-3 	4-abs(x)
# x=-2 		y<2   4-2 	4-abs(x)
# x=-1 		y<3   4-1 	4-abs(x)
# x=0 		y<4   4-0 	4-abs(x)
# x=1 		y<3   4-1 	4-abs(x)
# x=2 		y<2   4-2 	4-abs(x)
# x=3 		y<1   4-3 	4-abs(x)

for x in range(-3,4):
	for y in range(4-abs(x)):
		print('*', end='')
	print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# *
# ***
# *****
# *******
# *****
# ***
# *
#  		
# 			y=0, 增量1 							
# x=-3 		y<1 	7-6 	7-2*abs(x)
# x=-2 		y<3 	7-4 	7-2*abs(x)
# x=-1 		y<5 	7-2 	7-2*abs(x)
# x=0 		y<7 	7-0 	7-2*abs(x)
# x=1 		y<5 	7-2 	7-2*abs(x)
# x=2 		y<3 	7-4 	7-2*abs(x)
# x=3 		y<1 	7-6 	7-2*abs(x)

for x in range(-3,4):
	for y in range(7-2*abs(x)):
		print('*', end='')
	print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 扩展题:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

for i in range(-4,0):
    if i<0:       #if..else..条件可以写成三木运算符形式
        j=-i      #  j=-i if i<0 else j=i
    else:
        j=i
    #先是j个空格，然后打印（9-2j）个* ，后面的都是空格，在屏幕上不显示，可以不打印#
    print(' '*j+'*'*(9-2*j))  













'''
def set_abs(n):
	if n >= 0:
		return n
	else:
		n = -n
		return n
print(set_abs(-5))	
	



def startu(n):
	for i in range(n):
		
		
print(startu(5))


'''
