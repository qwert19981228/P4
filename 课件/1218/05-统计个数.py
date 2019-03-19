'''
	需求:
		统计某目录下 文件总个数, 目录总个数
'''
import os

def get_count(dirname):
	# 初始值
	file_count = 0 	# 文件总个数
	dir_count = 0 	# 目录总个数

	# 2. 获取 dirname 的所有文件和目录
	allfile = os.listdir(dirname)

	# 3. 遍历 allfile
	for i in allfile:
		# 3.1 凑完整的路径
		perfect_path = os.path.join(dirname, i)

		# 3.2 判断是否为文件
		if os.path.isfile(perfect_path):
			file_count += 1

		# 3.3 判断是否为目录
		if os.path.isdir(perfect_path):
			dir_count += 1 	# 当前目录+1
			# 获取 子目录的文件/目录总个数
			result = get_count(perfect_path) 

			# 再将 当前文件/目录总个数 + 子目录文件/目录总个数
			file_count += result[0]
			dir_count += result[1]
			# 分析:
			# 	file_count 只代表当前dirname下 文件总个数
			# 	dir_count 只代表当前dirname下 目录总个数
			# 	
			# 	result[0] 只代表子目录下 文件总个数
			# 	result[1] 只代表子目录下 目录总个数


	return file_count, dir_count

result = get_count('./a')
print('a目录 一共有 %d 文件' %  result[0])
print('a目录 一共有 %d 文件夹' % result[1])

