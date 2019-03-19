'''
	日期模块

	Pypi 官方第三方库: https://pypi.org/
'''

import datetime


# .datetime.now()
#  	返回值: 当前时间
a = datetime.datetime.now()
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# .datetime.from time stamp(时间戳)
# 返回值: 格式化时间戳
a = datetime.datetime.fromtimestamp( 1566666666 )
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# .datetime.datetime.strftime(格式)
#  返回值: 格式化后的时间
a = datetime.datetime(2018,11,11).strftime('%Y-%m-%d')
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .datetime.datetime.strptime('时间字符串', '格式')
a = datetime.datetime.strptime('2018-12-17', '%Y-%m-%d')
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .timedelta( 时间间隔 )
# 
a = datetime.datetime.now() - datetime.timedelta(days=1) 	# 昨天
a = datetime.datetime.now() + datetime.timedelta(days=1) 	# 明天
a = datetime.datetime.now() + datetime.timedelta(2) 		# 后天, 默认参数days=?.  如果是按天算, 可省略days
a = datetime.datetime.now() - datetime.timedelta(hours=3) 	# 3小时之前
a = datetime.datetime.now() + datetime.timedelta(hours=3) 	# 3小时之后
a = datetime.datetime.now() + datetime.timedelta(days=365) 	# 365天之后,   1年之后
print(a)























