'''
	函数名
	1. 命名规范
	2. 大小写
	3. 命名形式
	4. 注意点
'''


# 1. 命名规范:
# 	由数字, 字母和下划线组成
# 	但不能以数字开头

def a1():
	print('多年之前, 你若主动, 我们就会有故事')
a1()

def _a2():
	print('多年之后, 你若嫁了, 我若没娶, 叫你儿子放学路上小心点')
_a2()

# def 2B():
# 	pass

# def 中文():
# 	print('看看中文能不能用, 看看绿不绿, 不推荐, 因为会变绿')
# 中文()


# 2. 大小写
# 	严格区分大小写
# 	严格区分大小写
# 	严格区分大小写
def a():
	print('我的这个有点小')

a()
# A()


# 3. 命名形式
# 	参考: PEP8
# 
# 3.1 小写单词
def getmessage():
	print('苍老师发来的邀约信息')

# 3.2 下划线
def get_message():
	print('波老师发来的邀约信息')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 4. 注意点
# 	4.1 函数重名
# 		调用函数, 会调用前面最近的一个指定函数
# 		函数可以覆盖, 后面的覆盖前面的
# 		尽量别重名

def get_message():
	print('波老师昨天带学员喝酒去了')

get_message()


# 	4.2 函数名意义
# 	为了后期的维护, 提高代码的可读性, 函数名最好通俗易懂
# 	看到名字就大致知道什么功能
# 	
# 	惯性:
# 		函数名习惯以 动词+名词 形式出现


