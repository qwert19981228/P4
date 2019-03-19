'''
	日历模块
'''

import calendar


# .calendar(年份, w=2,l=1,c=6)
#  	返回值: 1年的日历
# 	
# 	参数:
# 		年份, 必须填
# 		w=2 默认 日期间隔
# 		l=1 默认 上下行间距
# 		c=6 默认 月份间隔

a = calendar.calendar(2018)
a = calendar.calendar(2018, 2,1,20)
# print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .month(年, 月)
#  返回值: 某一月的日历
a = calendar.month(2018, 12)
a = calendar.month(2020, 12)
a = calendar.month(8000, 12)
print(a)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# .isleap(年份)
# 	返回值: Bool
# 	
a = calendar.isleap(2000)
print(a)

