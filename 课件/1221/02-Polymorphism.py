'''
	OOP三大特性:
	1. 封装性
	2. 继承性
	3. 多态性
'''


# 3. 多态性
# 	定义: 通过一个类, 传入不同的对象, 从而实现不同的效果
# 	优点: 提高代码的灵活度



class usb():
	def run(self): 	# run 方法代表运行接入的设备
		pass

class mouse(usb):
	def run(self):
		print('已连接鼠标')


class keyboard(usb):
	def run(self):
		print('已连接键盘')

class udisk(usb):
	def run(self):
		print('已连接U盘')


# 准备在电脑上实现效果
class computer():
	def start(self, usb):
		usb.run() 	# 一开机, 就通过usb来调用run() 方法



c = computer()
m = mouse()
k = keyboard()
u = udisk()

c.start(m) 	# 电脑开机, 运行usb上的鼠标
c.start(k)  # 电脑开机, 运行usb上的键盘
c.start(u) 


# 分析:
# 	这里准备了 3个usb设备, 如何体现代码的灵活度
# 	
# 	这里computer类, 一旦开机(start), 就会usb下的run方法直接运行. (根本不管是什么usb设备, 只知道接入usb, 就要运行)







