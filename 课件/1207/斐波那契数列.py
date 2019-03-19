'''
	斐波那契数列
		0 1 1 2 3 5 8 13 21 34 ...
		

'''

n = 3

a1 = 0 	# 第一个数
a2 = 1 	# 第二个数
count = 2  # 计数

print('斐波那契数列: %d %d ' % (a1, a2), end='')
for i in range(3, n+1):
	tmp = a1 + a2 			# tmp 临时变量
	print(tmp, end=' ')
	a1 = a2
	a2 = tmp
	count += 1
print()

strvar = "123"
res = strvar.zfill(10)
print(res)
a = {'赵小刀':'赵丽颖','小笼包':'陈妍希','胖迪':'迪丽热巴'}
b = {k:v for k,v in a.items() if len(v)==4}
print(b)
