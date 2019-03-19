'''
	删除目录
'''

import os

def del_dir( dirname ):
    print(dirname)
	
	# 1. 获取所有的文件 和 目录
	allfile = os.listdir(dirname)

	# 2. 读取文件, 并删除
	#    读取目录, 进入目录, 删除里面的文件
	for i in allfile:
		# 2.1 凑完整路径
		perfect_path = os.path.join(dirname, i)

		# 2.2 判断是否为文件
		if os.path.isfile(perfect_path):
			os.remove(perfect_path)

		# 2.3 判断是否为目录
		if os.path.isdir(perfect_path):
			del_dir(perfect_path)


	# 3. 删除目录
	os.rmdir(dirname)


del_dir('./a')


