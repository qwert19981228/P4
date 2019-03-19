'''
	案例:  搜索文件

	需求: 提示用户输入要搜索的文件名
		  根据提示查询文件:
		  	找到: 返回文件的地址
		  	找不到: 提示找不到


	如果 函数自己调用自己, 这种函数, 我们称之为: 递归函数

	递归:
		1. 自己调用自己
		2. 函数必须要有终结值

'''

import os


def get_filename(dirname, search, bz = 0):

	# 1. 获取 dirname 下所有文件和目录
	allfile = os.listdir(dirname)

	# 2. 遍历allfile
	for i in allfile:
		# 2.1 凑完整路径
		perfect_path = os.path.join(dirname, i)

		# 2.2 判断是否为文件:
		if os.path.isfile(perfect_path):
			if search in i:
				print('已经找到该文件, 地址: %s' % os.path.abspath(i))
				bz = 1 	# 一旦找到文件, 立马修改bz = 1, 代表已找到文件

		# 2.3 判断是否为目录
		if os.path.isdir(perfect_path):
			bz = get_filename(perfect_path, search, bz)

	return bz 	# 返回标志, 让外面的人可以判断

# 1. 获取当前工作目录
dirpath = os.getcwd()

# 2. 提示用户输入文件名  input()
search = input('请输入您要搜索的文件名: ')

# 3. 调用函数, 查找 搜索文件
bz = get_filename(dirpath, search)
if bz == 0:
	print('找不到你搜索的文件')