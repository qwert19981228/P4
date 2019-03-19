'''
	流程控制符
	1. continue 	立马结束当前一轮循环, 直接准备下一轮循环
	2. break 		立马结束当前所在的循环, 准备执行循环外的代码
							   所在的最近的循环
	3. pass 		为了防止报错而占个位置, 留待将来使用, 本身无意义
'''

# 1. 输出0-9,  当碰到5, 则跳过
for i in range(10):
	if i == 5:
		continue
		print('xxxxx') 	# 该行代码也不会执行  
	print(i, end=" ")

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 2. 输出0-9, 当碰到5, 不循环, 则跳出循环

for i in range(10):
	if i == 5:
		break
	print(i, end=' ')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


for i in range(10):
	for j in range(i+1):
		if j == 5:
			break
		print('*', end='')
	print()


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 3. pass占位
if True:
	pass

for i in range(10):
	pass


a = 0.008
i = 0
while (2**i)*a:
	i+=1
	if (2**i)*a > 8848:
		break
print(i)






