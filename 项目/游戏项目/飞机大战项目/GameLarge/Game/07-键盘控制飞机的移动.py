import pygame

# 初始化游戏
pygame.init()
print('欢迎进入 召唤师峡谷')


# 初始化屏幕 	返回Surface对象
screen = pygame.display.set_mode( (480, 700) )


# 游戏背景
# 1. 加载图像 	返回Surface对象
background = pygame.image.load('./img/background.png')

# 2. 显示图像
screen.blit( background, (0,0) )

# 3. 刷新屏幕
pygame.display.update()



# 加载我方飞机
# 
# 方案1
# --------------------------------------------------
# 1. 加载图像
# plane = pygame.image.load('./img/single.png')
# plane = pygame.image.load('./img/single2.jpg')
# plane = pygame.image.load('./img/single2.png')
# # 2. 显示图像
# screen.blit(plane, (200,500))
# # 3. 刷新屏幕
# pygame.display.update()




# 方案2
# --------------------------------------------------

# 1.1 加载一张大图 (含有各种小飞机)
plane_img = pygame.image.load('./img/shoot.png')
# 1.2 设置矩形, 用于框中其中一架飞机
plane_rect = pygame.Rect(0,102, 99, 128)
print(plane_rect)
print(plane_rect.x)
print(plane_rect.y)
print(plane_rect.width)
print(plane_rect.height)
print(plane_rect.size)
# 1.3 扣出 飞机	
plane = plane_img.subsurface(plane_rect)

# 2. 显示图像
plane_pos = [200, 500]
screen.blit(plane, plane_pos)
# 3. 刷新屏幕
pygame.display.update()


# 初始化位置 (存储的都是 上下左右按键)
offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}


# 无限循环, 才是真正意义上的开始游戏
while True:

	# 重新绘制背景
	screen.blit(background, (0,0))


	# 移动我方飞机
	# plane_pos[1] -= 1
	screen.blit(plane, plane_pos)
	pygame.display.update()



	# 事件监听
	for event in pygame.event.get():
		# print(event)

		# 判断是否按下 按键
		if event.type == pygame.KEYDOWN:
			# 判断是否是 按得上下左右
			if event.key in offset:
				offset[event.key] = 5
				# plane_pos[1] -= 5
		
		# 判断是否松开 按键
		elif event.type == pygame.KEYUP:
			# 判断是否是 按得上下左右
			if event.key in offset:
				offset[event.key] = 0

		# 关闭窗口
		if event.type == pygame.QUIT:
			print('退出游戏')

			# 退出游戏, 需要卸载模块和退出程序
			pygame.quit() 	# 卸载模块
			exit() 			# 退出程序


	plane_pos[0] = plane_pos[0]+( offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]  )
	plane_pos[1] = plane_pos[1]+( offset[pygame.K_DOWN] - offset[pygame.K_UP]  )




# 退出游戏, 卸载游戏模块
# print('可以滚蛋了...')
# pygame.quit()

