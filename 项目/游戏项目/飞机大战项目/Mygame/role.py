import pygame
import random

#屏幕矩形
SCREEN_RECT = pygame.Rect(0,0,480,700)


#小敌机事件
ENEMY1_EVENT = pygame.USEREVENT

#中敌机事件
ENEMY2_EVENT = pygame.USEREVENT+1

#英雄子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT+2

#敌机子弹事件
ENEMY_FIRE_EVENT = pygame.USEREVENT+3

#中等敌机子弹事件
ENEMY1_FIRE_EVENT = pygame.USEREVENT+4

class Background(pygame.sprite.Sprite):
    '''背景精灵'''

    def __init__(self,image='./img/background.png',is_second=False):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        #判断是否为第二张背景
        if is_second == True:
            self.rect.y = -SCREEN_RECT.height

    def update(self):
        self.rect.y += 2

        #判断是否超出屏幕,交替背景
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Enemy(pygame.sprite.Sprite):
    '''敌机精灵'''
    def __init__(self,image):
        super().__init__()
        #敌机子弹精灵组
        self.embullet_group = pygame.sprite.Group()

        self.image = image
        self.rect = self.image.get_rect()
        #设置随机速度
        self.speedy = random.randint(1,5)
        self.speedx = random.randint(-2,2)

        #设置敌机初始出现位置
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)

    def update(self):
        #敌机向下飞行
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        #判断是否超出屏幕,销毁敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

        # 边框限制
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
    def fire(self,embullet_img):
        #子弹精灵
        embullet = EMBullet(embullet_img)
        #初始位置
        embullet.rect.centerx = self.rect.centerx
        embullet.rect.y = self.rect.y + self.rect.height
        #将精灵添加进组
        self.embullet_group.add(embullet)

class Enemy2(pygame.sprite.Sprite):
    '''敌机精灵'''
    def __init__(self,image):
        super().__init__()
        #敌机子弹精灵组
        self.embullet2_group = pygame.sprite.Group()

        self.image = image
        self.rect = self.image.get_rect()
        #设置随机速度
        self.speedy = random.randint(1,5)
        self.speedx = random.randint(-2,2)

        #设置敌机初始出现位置
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)

    def update(self):
        #敌机向下飞行
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        #判断是否超出屏幕,销毁敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

        # 边框限制
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
    def fire(self,embullet_img):
        #子弹精灵
        embullet2 = EMBullet(embullet_img)
        #初始位置
        embullet2.rect.centerx = self.rect.centerx
        embullet2.rect.y = self.rect.y + self.rect.height
        #将精灵添加进组
        self.embullet2_group.add(embullet2)

class Hero(pygame.sprite.Sprite):
    '''我方英雄'''
    #初始化英雄飞机
    def __init__(self,image):
        super().__init__()
        #创建子弹精灵组
        self.bullet = pygame.sprite.Group()
        #获取surface图像
        self.image = image
        #获取图像矩形
        self.rect = self.image.get_rect()

        #获取初始位置
        self.rect.x = SCREEN_RECT.width/2 - self.rect.width/2
        self.rect.y = SCREEN_RECT.height - self.rect.height-120

        #初始化移动

    #移动飞机
    def update(self,offset):
        #移动飞机
        self.speedx = offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
        self.speedy = offset[pygame.K_DOWN] - offset[pygame.K_UP]


        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #边框限制
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height
    #发射子弹
    def fire(self,bullet_img):
        #创建子弹精灵
        bullet1 = Bullet(bullet_img)

        #设置子弹初始位置
        bullet1.rect.centerx = self.rect.centerx
        bullet1.rect.y = self.rect.y

        #将子弹添加进精灵组
        self.bullet.add(bullet1)


class Bullet(pygame.sprite.Sprite):
    '''子弹精灵'''
    def __init__(self,image,speed =-5):
        super().__init__()

        #子弹图像
        self.image = image
        #子弹矩形
        self.rect = self.image.get_rect()
        #子弹速度
        self.speed = speed
        bullet_sound = pygame.mixer.Sound('./sound/bullet.wav')
        bullet_sound.set_volume(0.3)
        bullet_sound.play()

    #移动子弹
    def update(self):
        self.rect.y += self.speed
        # 判断是否超出屏幕,销毁子弹
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

class EMBullet(pygame.sprite.Sprite):
    '''敌机子弹精灵'''
    def __init__(self,image,speed =5):
        super().__init__()

        #子弹图像
        self.image = image
        #子弹矩形
        self.rect = self.image.get_rect()
        #子弹速度
        self.speed = speed

    #移动子弹
    def update(self):
        self.rect.y += self.speed

