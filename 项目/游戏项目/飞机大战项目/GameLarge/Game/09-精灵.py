from sprite import *

# 在python 没有真正的常量. 
# 为了表达 恒定不变的值, 就将 变量名 改成 纯大写
# 意味该常量 不能随意修改
SCREEN_RECT = pygame.Rect(0,0,480,700)

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
# 1.3 扣出 飞机	
plane = plane_img.subsurface(plane_rect)

# 2. 显示图像
plane_pos = list(plane_rect.center)
screen.blit(plane, plane_pos)
# 3. 刷新屏幕
pygame.display.update()


# 初始化位置 (存储的都是 上下左右按键)
offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}

# 创建一个时钟
clock = pygame.time.Clock()


# 创建 敌机精灵
enemy_rect = pygame.Rect(538,616,51,35)
enemy = plane_img.subsurface(enemy_rect)
enemy1 = Enemy(enemy) 	# 敌机1号
enemy2 = Enemy(enemy) 	# 敌机2号
enemy3 = Enemy(enemy) 	# 敌机3号

enemy_group = pygame.sprite.Group(enemy1, enemy2, enemy3)


# 无限循环, 才是真正意义上的开始游戏
while True:
	clock.tick(60)


	# 重新绘制背景
	screen.blit(background, (0,0))

	# 绘制 敌机飞机
	enemy_group.update()
	enemy_group.draw(screen)

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
				offset[event.key] = 20
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


	# 边框限制
	if plane_pos[0] < 0:
		plane_pos[0] = 0
	elif plane_pos[0] > SCREEN_RECT.width - plane_rect.width:
		plane_pos[0] = SCREEN_RECT.width - plane_rect.width

	if plane_pos[1] < 0:
		plane_pos[1] = 0
	elif plane_pos[1] > SCREEN_RECT.height - plane_rect.height:
		plane_pos[1] = SCREEN_RECT.height - plane_rect.height





