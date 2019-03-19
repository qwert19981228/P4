'''
	压缩包模块
'''

import zipfile

# ZIP 支持windows. 支持 Linux
# TAR 支持Linux
# 如果后期需要再linux上操作tar压缩包, 了解一下 tarfile 模块



# 1. 压缩
# 	1.1 创建一个zip包
zipBao = zipfile.ZipFile('./x.zip', 'a')

#  	1.2 将指定文件 写入 zip包
# zipBao.write('./b.txt')
# zipBao.write('./c')
# zipBao.write('./a.txt', 'a1.txt')
# zipBao.write('./b.txt', 'b1.txt')
# zipBao.write('./c.txt', 'c1.txt')


# 分析:
# 	zip包.ZipFile(filename, mode, compression, allowZip64)
# 		filename: 给zip包 取个名字
# 		
# 		mode:  打开方式
# 			r 读取zip包里面的文件
# 			w 往zip包里面写入文件 (会清除原有的内容)
# 			a 往zip包里面写入文件 (不会清除原有的内容)
# 
# 		compression: 压缩方法
# 			ZIP_STORED 		 仅仅将文件存入zip, 不会真正的压缩, 默认
# 			ZIP_DEfLATED 	 通过zip压缩算法, 再将文件存入zip
# 
# 		allowZip64: 是否允许创建 >= 2G的zip包
# 			True: 允许, 默认
# 			False: 不允许
# 
# 
# 	zip包.write(filename, arcname, compression)
# 		filename: 将哪个文件/目录 写入zip包
# 		arcname: 给写入zip包里的文件/目录 取个别名 (防止出现重名)
# 		compression: 压缩方式
# 			ZIP_STORED 		仅仅将文件存入zip包, 并非真正的压缩, 默认
# 			ZIP_DEFLATED  	将文件 压缩到zip包, 提前通过zip压缩算法处理一次
# 	
#  	1.3 关闭zip包
zipBao.close()



print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 2. 解压
# 	2.1 打开zip包
zipBao = zipfile.ZipFile('./x.zip', 'r')

# 	2.2 解压zip包中的所有文件
# zipBao.extractall('./e') 		# 全部解压到e目录下
zipBao.extract('a1.txt', './x') # 局部解压到e目录下

# 	2.3 关闭zip包
zipBao.close()


# 分析:
# 	zip包.extract(文件名, 指定目录)
#  		功能: 解压一个文件 到 指定目录
#  
# 	zip包.extractall(指定目录)
# 		功能: 解压所有文件 到 指定目录
# 	
# 	
# 	注意:
# 		如果指定目录不存在, 则自动创建
# 	
# 	

# 	





