 '''
	单例模式
'''


# 1. 定义
# 	第一次通过类 实例化时, 产生一个对象.
# 	第二次及以后再次通过类 实例化时, 会直接获取第一次实例化得到的对象. 不会再创建新的对象


# 2. 优势
# 	由于只会产生一个对象, 所以内存得到节省(内存是同一个)


# 3. 案例
# 	显卡
# 	音乐播放器
# 		第一次听歌时, 需要先打开播放器, 点第一首歌.
# 		当想要听第二首歌是, 需要再打开播放器吗????
# 		
# 		显而易见, 不需要再打开播放器.
# 		如果再打开播放器, 也可以听, 不过内存中, 也需要再多占一个内存
# 		如果直接使用第一次听歌的播放器, 也能听第二首歌, 而且不需要再多占一个内存
# 		


# 非单例模式
class Music(object):
	pass

a = Music()
b = Music()
print(a,id(a))
print(b,id(b))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# --------------------------------------------------


# 单例模式 - 残缺版
class Music(object):
	# 用于记录 第一个对象
	first = None


	def __new__(cls): 	# 重写object里面的new
		# 若first为空, 则证明从未实例化过, 那么允许创建一个对象
		# 若first非空, 则证明已经实例化过, 那么不允许创建对象

		if cls.first is None:
			cls.first = super().__new__(cls)

		return cls.first

a = Music()
b = Music()
c = Music()
d = Music()
e = Music()
f = Music()
print(a, b, c, d, e, f)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# --------------------------------------------------



# Bug
class Music(object):
	# 用于记录 第一个对象
	first = None

	def __new__(cls): 	# 重写object里面的new
		# 若first为空, 则证明从未实例化过, 那么允许创建一个对象
		# 若first非空, 则证明已经实例化过, 那么不允许创建对象

		if cls.first is None:
			cls.first = super().__new__(cls)

		return cls.first

	def __init__(self):
		print('hello, 酷狗')

a = Music()
b = Music()
c = Music()
d = Music()
e = Music()
f = Music()
print(a, b, c, d, e, f)
# Bug: 每一次实例化时, 对象确实只有一个, 总不能没换一首歌, 播放器就重启一次吧
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# 单例模式 - 完整版
# 	对象只有一个
# 	初始化只做一次


class Music(object):
	# 用于记录 第一个对象
	first = None
	is_init = False

	def __new__(cls): 
		if cls.first is None:
			cls.first = super().__new__(cls)

		return cls.first

	def __init__(self):
		if Music.is_init == True:
			return None

		print('hello, 酷狗')
		Music.is_init = True


a = Music()
b = Music()
c = Music()
print(a)
print(b)
print(c)


# 小结:
# 	初始化时, 会自动 执行 new 和 init (先new, 再init)
# 	
# 	单例模式:
# 		只有一个对象
# 		只执行一次初始化
