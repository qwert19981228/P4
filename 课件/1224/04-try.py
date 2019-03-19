'''
	异常传递
'''

# 1. 场景
# 	在实际开发中, 都是模块式开发, 每一个功能都是独立的
# 	最终会在一个主程序中 集中进行调试.
# 	如果在调用模块时, 其中一个模块发生了错误, 那么try应该写哪里
# 	解决方案: 
# 		把try写在主程序里面

def demo1():
	return int(input('请输入数字:'))


def demo2():
	return demo1()

try:
	demo2()
except Exception as e:
	# print('未知错误: %s' % e)
	pass

# ...














