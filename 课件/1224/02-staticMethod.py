'''
	静态方法
'''


# 1. 定义
#  	不需要使用类属性, 也不需要使用实例属性, 即可定义为 静态方法
#  	
#  	作用: 说明书, 更新内容, 协议展示 ...


# 2. 格式
# 
# 	@staticmethod
# 	def 静态方法名():
# 		代码块
# 
# 	注意: 
# 		不需要强制传入 self 或 cls

class Doll():
	name = '小强'

	@staticmethod
	def explain():
		'''说明书'''
		print('该娃娃产自 火星, 可以随便凑, 打坏包赔, 解压神器')

a = Doll()
a.explain()
Doll.explain()





