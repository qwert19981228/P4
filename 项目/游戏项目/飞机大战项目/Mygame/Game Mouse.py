import pygame
import random
from sprite import *
# 初始化游戏
pygame.init()


# 初始化屏幕 	返回Surface对象
screen = pygame.display.set_mode((480, 700))


# 游戏背景
# 1. 加载图像 	返回Surface对象
background = pygame.image.load('../Game/img/background.png')

# 2. 显示图像
screen.blit( background, (0,0) )

# 3. 刷新屏幕
pygame.display.update()

# 1.1 加载一张大图 (含有各种小飞机)
plane_img = pygame.image.load('../Game/img/shoot.png')
# 1.2 设置矩形, 用于框中其中一架飞机
plane_rect = pygame.Rect(0,102, 99, 128)
# 1.3 扣出 飞机	
plane = plane_img.subsurface(plane_rect)

# 2. 显示图像
plane_pos = [200, 500]

screen.blit(plane, plane_pos)
# 3. 刷新屏幕
pygame.display.update()

#创建一个时钟
clock = pygame.time.Clock()



#调用敌机精灵
enemy_rect = pygame.Rect(537,613,53,40)
enemy = plane_img.subsurface(enemy_rect)

enemy1 = Enemy(enemy)
enemy_group = pygame.sprite.Group(enemy1)



# 无限循环, 才是真正意义上的开始游戏
while True:

	#确定帧率
	clock.tick(60)

	# 重新绘制背景
	screen.blit(background, (0, 0))


	# 移动我方飞机
	screen.blit(plane, plane_pos)


	#绘制敌方飞机
	enemy_group.update()
	enemy_group.draw(screen)

	pygame.display.update()
	# 事件监听
	for event in pygame.event.get():
		#鼠标移动
		if event.type == pygame.MOUSEMOTION:
			mouse_pos = [event.pos[0], event.pos[1]]
			mouse_rel = [event.rel[0], event.rel[1]]
			plane_pos[0] = mouse_pos[0] + mouse_rel[0]
			plane_pos[1] = mouse_pos[1] + mouse_rel[1]
		# 关闭窗口
		if event.type == pygame.QUIT:
			print('退出游戏')

			# 退出游戏, 需要卸载模块和退出程序
			pygame.quit() 	# 卸载模块
			exit() 			# 退出程序

	# x轴
	if plane_pos[0] < 0:
		plane_pos[0] = 0
	elif plane_pos[0] > 480 - plane_rect.width:
		plane_pos[0] = 480 - plane_rect.width

	# y轴
	if plane_pos[1] < 0:
		plane_pos[1] = 0
	elif plane_pos[1] > 700 - plane_rect.height:
		plane_pos[1] = 700 - plane_rect.height
