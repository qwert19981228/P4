import pygame
from plane_role import *



class Plane():
	def __init__(self):
		# 初始化屏幕
		self.screen = pygame.display.set_mode( (SCREEN_RECT.width, SCREEN_RECT.height) )

		# 创建时钟
		self.clock = pygame.time.Clock()

		# 获取各种图像

		# 大图
		self.shoot = pygame.image.load('./img/shoot.png')


		# 小飞机
		enemy_rect = pygame.Rect(538,616,51,35)
		self.enemy_img = self.shoot.subsurface(enemy_rect)


		# 定时器
		# 
		# 1. 每1s 触发敌机事件
		pygame.time.set_timer(ENEMY_EVENT, 500)


		# 创建精灵组
		self.__create_sprite()

	# 创建精灵组
	def __create_sprite(self):
		# 背景精灵
		bg1 = Background()
		bg2 = Background(is_second=True)
		self.bg_group = pygame.sprite.Group(bg1, bg2)

		# 敌机精灵组
		self.enemy_group = pygame.sprite.Group()

	# 开始游戏
	def start_game(self):
		print('游戏开始')

		while True:
			# 设置帧率
			self.clock.tick(60)

			# 调用事件监听
			self.__event_monitor()

			# 检测碰撞
			self.__collied()

			# 更新并绘制精灵组
			self.__update_sprite_group()

			# 刷新屏幕
			pygame.display.update()

	# 事件监听
	def __event_monitor(self):
		for event in pygame.event.get():

			# 监听 关闭窗口
			if event.type == pygame.QUIT:
				self.__gameover()

			# 监听 敌机事件
			elif event.type == ENEMY_EVENT:
				enemy = Enemy(self.enemy_img)
				self.enemy_group.add(enemy)


	# 飞机,子弹碰撞
	def __collied(self):
		pass

	# 更新绘制精灵组
	def __update_sprite_group(self):
		self.bg_group.update()
		self.bg_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

	# 游戏结束
	def __gameover(self):
		print('游戏结束')
		pygame.quit()
		exit()


game = Plane()
game.start_game()