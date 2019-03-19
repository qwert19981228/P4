'''
	内置函数
	1. 类型相关的
	2. 变量相关的
	3. 数学相关的
	4. 进制相关的
'''

# 1. 类型相关
#  	int()
#  	float()
#  	bool()
#  	complex()
#  	str()
#  	list()
#  	tuple()
#  	set()
#  	dict()


# 2. 变量相关
# 	id() 		获取变量的内存地址
# 	type() 		获取变量的数据类型
# 	print() 	输出变量
# 	locals() 	获取当前作用域中的所有变量

a = '女人最好什么?'
b = '最爱包, 因为包治百病'
print('作用域G: ', locals() )
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def A():
	x = 30
	y = 40
	print('作用域E :', locals())
	def B():
		m = 100
		n =200
		print('作用域L :', locals())

	B()
A()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 3. 数学相关
#  	abs()
#  	sum()
#  	max()
#  	min()
#  	pow()
#  	round()
#   range()
print( abs(-5) )
print( sum([1,2,3]))
print( max([1,2,3]))
print( min([1,2,3]))
print( pow(2,3) ) 	# 2的3次方  
print( round(0.12345678, 3)) 	# 保留指定小数位

for i in range(5):
	print(i, end="")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 进制相关
# hex() 	十六进制
# oct() 	八进制
# bin() 	二进制
# chr() 	ascii => 字符
# ord() 	字符 => ascii
# repr()  	原始字符串
# eval() 	解析字符串 (能够将字符串 当成公式执行. 例如含有变量, 那么就会解析变量)


print( hex(10)  )
print( oct(8)  )
print( bin(8)  )
print( chr(97) )
print( ord('a') )
print( ord('A') )
print( ord('0') )


string = '老\n母\n鸡'
print(string)
print(repr(string))

a = 10
print('a+1')
print(eval('a+1'))






