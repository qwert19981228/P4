import pygame
import random

# 屏幕矩形
SCREEN_RECT = pygame.Rect(0,0,480,700)

# 敌机事件
ENEMY_EVENT = pygame.USEREVENT

class Background(pygame.sprite.Sprite):	
	'''背景精灵'''
	
	def __init__(self, image='./img/background.png', is_second=False):
		super().__init__()

		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()

		# 判断是否为第二张背景
		if is_second == True:
			self.rect.y = -SCREEN_RECT.height


	def update(self):
		self.rect.y += 2

		# 判断是否超出屏幕, 交替背景
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -SCREEN_RECT.height

class Enemy(pygame.sprite.Sprite):
	'''敌机精灵'''

	def __init__(self, image):
		super().__init__()

		self.image = image
		self.rect = self.image.get_rect()
		# 设置 随机速度
		self.speed = random.randint(1,5) 	

		# 设置 敌机初始 出现位置
		self.rect.x = random.randint( 0, SCREEN_RECT.width - self.rect.width  )

	def update(self):
		# 敌机向下飞行
		self.rect.y += self.speed
	
		# 判断是否超出屏幕, 销毁敌机
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()

