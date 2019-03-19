import pygame
import random


#创建敌机精灵
class Enemy(pygame.sprite.Sprite):
    '''敌机精灵'''
    def __init__(self,image,speed = 1):
        super().__init__()      #调用初始化
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = random.randint(1,2)
        self.rect.x = random.randint(0,440)
        self.rect.y = random.randint(0,650)
    def update(self):
        self.rect.y += self.speed