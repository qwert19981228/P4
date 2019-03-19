'''
	主动抛出异常
'''


# 1. 场景
# 	在之前学的Python中, 都是自动捕获异常, 也会自动报错.
# 	在实际开发中, 有很多业务不满足条件时, 也会做异常处理, 此时需要主动抛出异常来处理


# 小结:
# 	能够进入 处理异常区域的方式:
# 	1. 自动捕获异常
# 	2. 主动抛出异常 	
# 		2.1 准备异常
# 		2.2 抛出异常


def get_num():
	
	# 1) 提示用户 输入数字
	num = input('请输入数字: ')

	# 2) 判断是否为 数字
	if num.isdigit() == True:
		print('您输入的数字为: %s' % num)
	else:
		print('准备主动抛出异常')
		e = Exception('您输入的不是数字') # 准备异常
		raise e  						# 抛出异常

try:
	get_num()	
except Exception as e:
	print(e)













