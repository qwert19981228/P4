'''
	os模块
'''

import os
# os.system('type null>a.txt')

# .remove(文件路径)
#  	功能: 删除一个文件
#  	
#  	注意: 若文件不存在, 则报错

# d.txt 位置: 1218/a/b/c/d.txt
# os.remove('./a/b/c/d.txt')




# .listdir(目录路径)
#  功能: 获取指定目录下的  所有文件 和 文件夹
#  返回值: list
# result = os.listdir('./a')
# print(result)


# .path.exists(路径)
# 	功能: 判断一个文件 或 目录是否存在
# 	返回值: bool

print( os.path.exists('./a/a (1).txt') )
print( os.path.exists('./a/a (999).txt') )
print( os.path.exists('./a/b') )
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# .path.isfile(文件路径)
# 	功能: 判断是否为 文件
print( os.path.isfile( './a/a (1).txt') )
print( os.path.isfile( './a/b') )
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# .path.isdir(目录路径)
# 	功能: 判断是否为 文件
print( os.path.isdir( './a/a (1).txt') )
print( os.path.isdir( './a/b') )
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .path.abspath(路径)
# 	功能: 获取绝对路径
# 	返回值: 字符串
# 	
# 	分析:
# 		windows: 指的就是某个盘符
# 		linux: 指的是 根目录

print( os.path.abspath('./a'))
print( os.path.abspath('./a/a (1).txt'))


# .path.join(路径1, 路径2)
#  	功能: 拼接目录和文件名
#  	返回值: string
print( os.path.join('./a', 'a (1).txt')  ) 	# 中间的分隔符, 会自动采用当前系统的默认分隔符
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .path.split(路径)
# 	功能: 拆分路径
# 	返回值: tuple
url = 'C:/Python3/P4/1218/a/a (1).txt'
print( os.path.split(url) )


# .path.dirname(路径)
# 	功能: 只获取目录
url = 'C:/Python3/P4/1218/a/a (1).txt'
print( os.path.dirname(url))



# .path.basename(路径)
#  	功能: 只获取文件名
url = 'C:/Python3/P4/1218/a/a (1).txt'
print( os.path.basename(url))



# .path.getsize(文件路径) 
#  	功能: 获取文件的大小
#  	返回值: 字节
#  	
#  	注意:
#  		仅支持文件大小, 不支持目录大小

# print( os.path.getsize('./a/a (1).txt')  )
# print( os.path.getsize('./a')  ) 	 		




