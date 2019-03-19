'''
	案例模块
'''

name = '二狗'
money = 9999999999


def skill():
	print('蛤蟆功')

def skill2():
	print('如来神掌')


def skill3():
	print(__name__)


if __name__ == '__main__':
	print('这是自己给自己操办的婚礼, 用心程序100%')
else:
	print('这是帮忙操办的婚礼, 用心程度60%')