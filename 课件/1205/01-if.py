'''
	分支结构
'''

# 分支5
# 	
# 	巢状结构
# 	
# 	if 条件1:
# 		true环境1 
# 		if 条件2:
# 			true 环境2
# 			if 条件3:
# 				true环境3
# 				...
# 			else:
# 				false环境3
# 		else:
# 			false环境2
# 	else:
# 		false
# 	
# 	
# 	要同时满足多个条件时, 才能进入相应的代码块

# 
# 例如: 
# 	男:
# 		年龄:
# 			大: 大叔
# 			小: 帅哥
# 	女
# 		年龄:
# 			大: 大姐
# 			小: 小姐

sex = '女'
age = 20

if sex == '男':
	if age < 30:
		print('帅哥')
	else:
		print('大叔')
else:
	if age < 30:
		print('小姐')
	else:
		print('大姐')


