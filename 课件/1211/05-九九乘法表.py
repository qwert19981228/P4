'''
	99乘法表[1*1=1, 1*2=2, 1*3=3, 1*4=4, ...]
'''


# 基础写法
i = [1,2,3,4,5,6,7,8,9]
j = [1,2,3,4,5,6,7,8,9]
res = [ '%d * %d = %d' % (x, y, x*y) for x in i for y in j if y >= x]
print(res)
print(len(res))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 简化一点
res = [ '%d * %d = %d' % (x, y, x*y) for x in range(1,10) for y in range(1,10) if y >= x]
print(res)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 最优的写法
res = [ '%d * %d = %d' % (x, y, x*y) for x in range(1,10) for y in range(x,10) ]
print(res)


