'''
	高阶文件模块
'''
import shutil


# src: 源文件
# dst: 目标文件


# .copyfile(src, dst)
# 	功能: 将文件src 的内容 复制给 dst
# 	
# 	分析:
# 		仅仅将内存复制过给dst
# 		
# 		dst 若不存在, 则自动创建
# 		dst 若存在, 则删除原有内容, 重新写入

# shutil.copyfile('./a.txt', './b.txt')



# .copymode(src, dst)
# 	功能: 将src 的文件权限 复制给了 dst
# 	
# 	分析:
# 		dst 若不存在, 则报错
# 		dst 若存在, 只把src的权限给了dst, 不会复制内容

# shutil.copymode('./c.txt', './d.txt')


# .copystat(src, dst)
# 	功能: 将 src文件的 权限 和 时间 复制给了dst
#   
#   分析:
#   	dst 若不存在, 则报错
#   	dst 若存在, 仅仅复制权限和时间,  不包括内容
# shutil.copystat('./e.txt', './f.txt')


# .copy(src, dst)
# 	功能: 将 src文件的 权限 和 内容 复制给了dst
# 	
# 	分析: 
# 		dst 若不存在, 则自动创建
# 		dst 若存在, 仅仅复制权限和内容, 不包括时间
# shutil.copy('./e.txt', './g.txt')


# .copy2(src, dst)
# 	功能: 将 src文件的 权限, 内容 和 时间 复制给了dst
# 	
# 	分析:
# 		dst 若不存在, 则自动创建
# 		dst 若存在, 那都复制, 内容会重写
# shutil.copy2('./e.txt', './h.txt')


# shutil.copy2('./a', './b') 	# 以上都不是目录操作



# .copytree(src, dst)
# 	功能: 将 src目录 递归复制给 dst
# 	
# 	分析:
# 		src 和 dst 都是目录
# 		在复制src 时, 会递归复制所有的子文件 和 子目录
# 		dst若不存在, 则自动创建
# shutil.copytree('./a', './b')


# .rmtree(src)
# 	功能: 递归删除目录 src 
# 	
# 	分析:
# 		src 不存在, 则报错
# 		src 存在, 则删除里面所有的文件和目录, 包括自己

# shutil.rmtree('./b')


# .move(src, dst)
#	功能: 剪切文件 或 重命名文件
#	
#	分析:
#		适用于 文件 或 目录
#		重命名: 只要目录没变即可
#		剪切:  必须要换一个目录
#		
#	注意:
#		剪切目录时, 拒绝访问的文件不能被剪切


# shutil.move('./h.txt', './hhh.txt') 	# 重命名
# shutil.move('./hhh.txt', './a/h.txt') # 剪切
# shutil.move('./a', './b')
# shutil.move('./b', './c/b')
















