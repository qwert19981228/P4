import pygame

# 初始化游戏
pygame.init()
print('欢迎进入 召唤师峡谷')


# 初始化屏幕
pygame.display.set_mode( (480, 700) )


# 无限循环, 才是真正意义上的开始游戏
while True:

	# 获取所有的是件
	# a = pygame.event.get()
	# if len(a) > 0:
	# 	print(a)


	# 关闭窗口
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print('退出游戏')

			# 退出游戏, 需要卸载模块和退出程序
			pygame.quit() 	# 卸载模块
			exit() 			# 退出程序



# 退出游戏, 卸载游戏模块
# print('可以滚蛋了...')
# pygame.quit()

