'''
	文件指针
	1. 当前指针
	2. 移动指针
'''

# 准备工作
a = open('a1.txt', 'w')
a.write('laomuji')
#a.write('老母鸡')
a.close()




# 1. 当前指针
# 	io对象.tell()

a = open('a1.txt', 'r')
print(a.tell()) 	# 当前指针为 0
print(a.read(2)) 	# 读取2位, 指针向后移2位
print(a.tell()) 	# 当前指针为 2

print(a.read()) 	# 读取到最后
print(a.tell()) 	# 当前指针是几,  该文件就有多大字节
a.close()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 2. 移动指针
# 	io对象.seek()
a = open('a1.txt', 'r')
print(a.tell())
print(a.read(2))
print(a.tell())
a.seek(0) 			# 将指针移到 最前面
print(a.tell())
a.seek(3)
print(a.tell())

a.read()	# 也可以利用 read读完, 将指针移到最后











