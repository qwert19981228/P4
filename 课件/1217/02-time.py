'''
	时间模块
'''

import time

a = time.time() 	# 时间戳,   从1970-现在的秒数.  格林威治时间
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 格式化时间
# 	.ctime( 时间戳 )
# 	参数: 不填, 默认当前时间戳
# 	
# 	返回值: Fri Dec 14 13:40:28 2018
# 	       周几 月  日 时 分 秒  年
# 	
a = time.ctime() 	
# a = time.ctime(1039483945) 	
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .gmtime()
# 返回值: 时间结构体 - 世界时间元组
# 
# 分析: 世界时间, 格林威治时间, 世界标准时间, 世界统一时间.  简单理解: 英国时间
a = time.gmtime()
print(a)


# .localtime()
# 返回值:时间结构体 - 本地时间元组
# 
# 分析: 当前地区的时间. 
a = time.localtime()
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .asctime( 时间元组 )
# 	返回值: 格式化之后的时间字符串
# 	
# 	分析:
# 		时间元组不填, 默认当前本地时间元组
a = time.asctime()
a = time.asctime(  time.localtime()  )
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .strftime(格式, 时间元组)
# 返回值: 格式化后的时间字符串
# 
# 分析: 
# 	格式参考 "时间模块.pdf"

a = time.strftime('%Y/%m/%d %H:%M:%S ', time.localtime() )
a = time.strftime('%Y/%m/%d %I:%M:%S %p', time.localtime() )
a = time.strftime('%U', time.localtime() )
a = time.strftime('%x', time.localtime() )
a = time.strftime('%X', time.localtime() )
# a = time.strftime('%Z', time.localtime() )
a = time.strftime('%Y %%  %m %%  %d %I:%M:%S %p', time.localtime() )
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



# .strptime(时间字符串, 格式)
# 返回值: 时间元组
# 
# 分析:
# 	就是strftime的逆操作

a = time.strptime('2018-12-17 10:12:30', '%Y-%m-%d %H:%M:%S')
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .mktime(时间元组)
#  返回值: 时间戳
#  
#  分析:
#  	此处的时间是可以自己编, 从而获取指定的时间戳
#   注意点: 
#   	参数一定要是 时间元组
a = time.mktime(  time.localtime() )

# 获取 2018年12月17日 10点15分30秒 的时间戳
a = time.mktime(  (2018,12,17,10,15,30,0,0,0)   )
print(a)


# 计算 王嘉诚活了多少秒
now = time.time()
birthday = time.mktime( (1994,4,3,11,11,11,0,0,0) )
diff = now - birthday
print('王嘉诚已经活了 %d 秒' % diff)


# 计算 现在王嘉诚活了 多少年
import math
year = diff/60/60/24/365
print('王嘉诚现在已经活了 %d  年' % year )
print('王嘉诚现在已经活了'+ str(math.floor(year)) +'年'  )

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# .sleep(秒数)
# 返回值: 无
# 
# 分析: 
# 	当程序执行到sleep时, 会暂时睡眠一会. 常用于 延迟效果

# time.sleep(2)
# print('倒计时结束')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .perf_counter()
# 	返回值: 系统运行的时间, 包含睡眠时间
a = time.perf_counter()
print(a)


# .process_time()
# 	返回值: 消耗cpu的时间, 不包含睡眠时间
a = time.process_time()
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')




# 案例: 
# 	执行100次命令, 需要花多长时间

start = time.perf_counter()

# for i in range(100):
for i in range(10000000):
	pass

stop = time.perf_counter()
print('程序一共花了 %f  秒' %  (stop-start) )




















