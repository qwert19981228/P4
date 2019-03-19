'''
	异常
	1. 定义
	2. 格式
'''

# 1. 定义
# 	在程序执行过程中, 如果发生了错误, 那么程序会立马终止, 并提示一些错误信息, 这就是"异常"
# 	
# 	其中, 这些错误信息, 这种行为"抛出异常"
# 	
# 	我们程序员需要做的, 就是让产品不会抛出异常, 尽量给用户比较好的体验感



# 2. 格式
# 
# 写法1: 基本用法
# 
#  	try:
#  		正在执行代码的区域a  (捕获异常)
#  	except:
#  		处理异常的区域b 		(处理异常)
#
#   区域c
#
#
#   分析:
#		区域a  如果发生错误, 则立马进入区域b
#  		区域a  如果没发生错误, 则等区域a 执行完, 然后进入区域c
#  		
#   	在trye中, python一直在捕获 区域a 的异常, 一旦捕获成功, 则会执行区域b		
#   
#   注意:
#   	无论上面是否有异常, 区域c 都会执行
#  

# try:
# 	num = int( input('请输入数字: ') )
# 	print('您输入的是: %d' % num)
# except:
# 	print('您输入的不是数字')

# print('--'*30)
# --------------------------------------------------


# 格式2:
# 	不同的错误, 报不同的信息
# 	try:
# 		代码块a
# 	except 错误类型1:
# 		代码块b
# 	except 错误类型2:
# 		代码块c
# 	...
# 		

# try:
# 	num = int(input('请输入数字: '))
# 	result = 100 / num
# 	print('100 / %d = %f ' % (num, result))
# except ZeroDivisionError:
# 	print('不能输入数字0')
# except ValueError:
# 	print('请输入数字')

# --------------------------------------------------



# 格式3:
# 	不同的错误信息, 报相同的提示信息
# 	
# 	try:
# 		代码块a
# 	except (错误类型1, 错误类型2, ...):
# 		代码块b
# 	except (错误类型3, 错误类型4, ...):
# 		代码块c

# try:
# 	num = int(input('请输入数字: '))
# 	result = 100 / num
# 	print('100 / %d = %f ' % (num, result))
# except (ZeroDivisionError, ValueError):
# 	print('请输入正确的数字')
# --------------------------------------------------




# 格式4:
# 	未知错误
#   
#   try:
#   	代码块a
#   except Exception as 变量:
#   	代码块b

# 作用:
# 	在实际开始种, 想要把所有可能发生的错误全部预测出来, 挺难的
# 	此时,通过Exception 异常类 统一抛出异常. 例如: 404, 服务器繁忙...

# try:
# 	num = int(input('请输入数字: '))
# 	result = 100 / num
# 	print('100 / %d = %f ' % (num, result))

# except Exception as e:
# 	print('未知错误: %s' % e)

# print('--'*50)



# 格式5:
# 	完整写法
# 
# 	try:
# 		代码块a
# 	
# 	except 错误类型1:
# 		...
# 	except 错误类型2:
# 		...
# 	except (错误类型3,错误类型4):
# 		... 
# 	except (错误类型5,错误类型6):
# 		... 
# 	except Exception as e:
# 		...
# 	else:
# 		代码块b  没有异常时才会执行
# 	finally:
# 		代码块c  无论是否有异常, 都会执行
# 	

try:
	num = int(input('请输入数字: '))
	res = 100 / num
except ValueError:
	print('请输入正确的数字')
except (ZeroDivisionError):
	print('请输入非0数字')
except Exception as e:
	print('未知错误: %s' % e)
else:
	print('100 / %d = %f ' % (num, res))
finally:
	print('*'*30)



















