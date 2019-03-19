# 
# 身份运算符
# 	is 		判断两个变量是否来自一个内存
# 	is not 	判断两个变量是否来自不同的内存
# 	
# 	注意点:
# 		is 	判断的是内存地址
# 		==  判断的是值


a = b = 10
print(id(a))
print(id(b))
print( a is b )
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

a = 10
b = 20
print(id(a))
print(id(b))
print( a is b )
print( a is not b )
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



a = 0
b = False
print( a == b )
print( a is b )







