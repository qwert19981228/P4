'''
	常见标准模块:
	1. string模块
'''

# 1. string模块
# 	简述: 字符串 相关的功能
import string

a = string.ascii_letters 	# 获取所有的字母 (包含大小写)
a = string.ascii_uppercase  # 获取所有的大写字母
a = string.ascii_lowercase  # 获取所有的小写字母
a = string.digits 			# 获取所有的数字(十进制)
a = string.octdigits 		# 获取所有的数字(八进制)
a = string.hexdigits 		# 获取所有的数字(十六进制)
a = string.punctuation 		# 获取ascii码中所有符号, 标点
a = string.whitespace 		# 获取所有的空白  空格, 制表符, 换行等
a = string.printable 		# 获取所有的字符
print(a, type(a))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 练习:
# 	获取所有的字母 和 数字
a = string.ascii_letters + string.digits
print(a)

