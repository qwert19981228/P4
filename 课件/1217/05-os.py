'''
	os模块
'''

# os模块
# 	简述: 操作系统 相关的模块

import os


# .name 属性/变量
# 	
# 	返回值
# 		nt 		=> windowns      winNT
# 		posix   => linux
a = os.name 
print(a)


# .sep 	属性
# 	返回值: 
# 		当前系统支持的路径分隔符
# 		windows:  \ 
# 		linux:    / 
print( os.sep )


# .getcwd()
# 	功能: 获取当前工作路径
print( os.getcwd() )


# .mkdir(目录路径)
# 	功能: 创建目录
# 
# 	分析:
# 		1) 
# 			./ 		当前目录
# 			../ 	上一级目录
# 			../../  上上级目录
# 			依次类推
# 			
# 			这里的当前, 是指你正在运行的文件.   此文件在哪, 那么当前目录就在哪
# 		
# 		2) 
# 			如果目录已存在, 则报错

# os.mkdir('a')
# os.mkdir('./a')
# os.mkdir('../a')
# os.mkdir('../../b')
# os.mkdir('.../c') 	# 没有.../,  顶多就两个.
# os.mkdir('./x/y/z') 	# 无法创建多级目录



# .makedirs(目录路径)
# 	功能: 创建多级目录
# 	
# 	分析:
# 		如果该目录已存在, 则报错

# os.makedirs('./x/y/z')



# .rmdir(目录路径)
# 	功能: 删除空目录
# 	
# 	分析:
# 		只能删除 空目录 (里面不能含有任何文件或目录)

# os.rmdir('./a')


# .chdir(目录)
# 	功能: 修改当前工作路径
# 	
# os.chdir('./a') 	# 切换当前目录 到 a里面
# os.mkdir('./z') 	# 此时创建目录, 是在 a目录里面创建


# os没有直接创建文件的命令, 但是可以运行window脚本命令. 而windows脚本命令中有 创建文件的命令
# 

#   
#   在哪个系统下, 就用哪个命令


os.system('type null > a.txt')
os.system('del a.txt')

os.system('mkdir aaa')
os.system('rmdir aaa')











