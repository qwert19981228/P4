# 练习:
# 
# 输出 0-9
# --------------------

num = 0
while num < 10:
	print(num, end=" ")
	num += 1
else:
	print('')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 计算 0-9 的和
num = 0
sum = 0

while num < 10:
	sum += num 	# sum = sum + num
	num += 1
else:
	print(sum)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 输出 0-9 中所有的偶数 (2的倍数)

num = 0

while num < 10:

	# 判断当前的num 是否为偶数
	if num % 2 == 0:
		print(num)

	num += 1

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 计算 0-9 中所有的偶数和

num = 0 	
sum = 0 	# sum 存储总和

while num < 10:
	if num % 2 == 0:
		sum += num

	num += 1
else:
	print(sum)