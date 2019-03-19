'''
	需求:
		查看目录a 下所有的文件
		注意: 
			如果目录a 含有子目录, 直接忽略
'''

import os

# 获取目录下所有的文件名 (不包含子目录)
# @param  dirname 	目录名 
def get_filename(dirname):

	# 1. 获取 dirname 下所有文件和目录
	allfile = os.listdir(dirname)

	# 2. 遍历allfile
	# 	每一次i 会获取到 文件名/目录名
	for i in allfile:
		# 2.1 凑完整路径
		perfect_path = os.path.join(dirname, i)

		# 2.2 判断是否为文件:
		# 	是: 输出文件名
		if os.path.isfile(perfect_path):
			print(i)

get_filename('./a')



