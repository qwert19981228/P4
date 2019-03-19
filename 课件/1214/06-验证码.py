'''
	设计验证码
'''
import string
import random


# 数字验证码
def yzm():
	# 1. 存储验证码
	code = ''

	# 2. 随机4位数字
	for i in range(4):
		a = random.randrange(0,10)
		code += str(a)

	# 3. 返回验证码
	return code
print(  yzm() )


# 字母验证码
def yzm():
	# 1. 存储验证码
	code = ''

	# 2. 准备 大小写字母
	a = string.ascii_letters

	# 3. 随机获取一个字母
	for i in range(4):
		code += random.choice(a)

	# 4. 返回验证码
	return code

print( yzm() )



# 字母验证码
def yzm():
	# 1. 存储验证码
	code = ''

	# 2. 准备 大小写字母
	a = string.ascii_letters + string.digits

	# 3. 随机获取一个字母
	for i in range(4):
		code += random.choice(a)

	# 4. 返回验证码
	return code

print( yzm() )


# 汉字验证码
def yzm():
	# 1. 存储验证码
	code = ''

	# 2. 准备汉字
	a = '阿什顿发的发生的发生的反撒地方阿萨德发起翁二群翁热群翁二群持续表现出'

	# 3. 随机获取一个汉字
	for i in range(4):
		code += random.choice(a)

	# 4. 返回验证码
	return code

print( yzm() )




# 成语验证码
def yzm():
	# 1. 存储验证码
	code = ''

	# 2. 准备汉字
	a = ['一丝不苟', '一干二净', '魑魅魍魉', '三心二意', '五湖四海', '六亲不认', '七嘴八舌', '九牛一毛', '八仙过海', '二二得四', '四面八方', '十全十美']

	# 3. 随机获取一个成语
	code = random.choice(a)

	# 4. 返回验证码
	return code

print( yzm() )


