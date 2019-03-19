'''
	综合验证码
'''


# parameter 形参
# argument  实参

# 验证码
# @param Length 	验证码长度
# @param type 		验证码类型 	1:数字  2:字母  3:数字+字母  4:汉字
#  					
import random
import string
def yzm(Length=4, Type=1):
	# 1. 存储验证码
	code = ''

	# 2. 生成验证码
	if Type==1:
		# 数字验证码
		for i in range(Length):
			a = random.randrange(0,10)
			code += str(a)

	elif Type==2:
		# 字母验证码
		a = string.ascii_letters
		for i in range(Length):
			code += random.choice(a)

	elif Type==3:
		# 数字+字母验证码
		a = string.ascii_letters + string.digits
		for i in range(Length):
			code += random.choice(a)

	elif Type==4:
		# 汉字验证码
		a = '阿什顿发的发生的发生的反撒地方阿萨德发起翁二群翁热群翁二群持续表现出'
		for i in range(Length):
			code += random.choice(a)

	# 返回验证码
	return code


print( yzm() )
print( yzm(2) )
print( yzm(6, 2) )
print( yzm(3, 3) )
print( yzm(4, 4) )
