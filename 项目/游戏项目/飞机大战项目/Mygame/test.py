import pygame

# 初始化游戏
pygame.init()

# 初始化屏幕 	返回Surface对象
screen = pygame.display.set_mode( (480, 700) )


# 游戏背景
# 1. 加载图像 	返回Surface对象
background = pygame.image.load('../Game/img/background.png')

# 2. 显示图像
screen.blit(background,(0,0))

# 3. 刷新屏幕
pygame.display.update()

# --------------------------------------------------

# 1.1 加载一张大图 (含有各种小飞机)
plane_img = pygame.image.load('../Game/img/shoot.png')
# 1.2 设置矩形, 用于框中其中一架飞机
plane_rect = pygame.Rect(2,101, 100, 120)
# 1.3 扣出 飞机	
plane = plane_img.subsurface(plane_rect)
plane2 = plane_img.subsurface(plane_rect)

# 2. 显示图像
plane_pos = [200, 500]
plane_pos2 = [200, 500]

screen.blit(plane, plane_pos)
screen.blit(plane2, plane_pos2)

# 3. 刷新屏幕
pygame.display.update()

# 无限循环, 才是真正意义上的开始游戏
while True:

	# 重新绘制背景
	screen.blit(background, (0,0))


	# 移动我方飞机
	plane_pos[1] -= 20
	plane_pos2[0] -= 20
	screen.blit(plane, plane_pos)
	screen.blit(plane2, plane_pos2)

	pygame.display.update()

	# 扩展:
	# 	飞机移出屏幕时, 将飞机重置屏幕的最下方
	if plane_pos[1] == -120 :
		plane_pos = [200,700]
		plane_pos[1] -= 20
		screen.blit(plane, plane_pos)
		pygame.display.update()

	if plane_pos2[0] == -100:
		plane_pos2 = [480,500]
		plane_pos2[0] -= 20
		screen.blit(plane2, plane_pos2)
		pygame.display.update()

	# 关闭窗口
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print('退出游戏')

			# 退出游戏, 需要卸载模块和退出程序
			pygame.quit() 	# 卸载模块
			exit() 			# 退出程序


