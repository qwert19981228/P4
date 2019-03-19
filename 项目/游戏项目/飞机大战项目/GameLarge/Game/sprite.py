import pygame
import random

class Enemy(pygame.sprite.Sprite):
	'''敌机精灵类'''

	def __init__(self, image, speed=1):
		super().__init__() 		# 先调用精灵类的初始化, 防止被重写

		self.image = image 		# 获取 image Surface图像
		self.rect = self.image.get_rect() 	# 获取图像的矩形

		self.speed = random.randint(1,5)


	def update(self):
		# 敌机精灵 的移动
		self.rect.y += self.speed
		