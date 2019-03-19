import pygame
import time
from role import *

pygame.init()
pygame.mixer.init()
class Plane():
    def __init__(self):
        #初始化屏幕
        self.screen = pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))

        #创建时钟
        self.clock = pygame.time.Clock()

        #获取各种图像
        #大图
        self.shoot = pygame.image.load('./img/shoot.png')

        #小飞机
        self.enemy1_rect = pygame.Rect(534,612,57,43)
        self.enemy1_img = self.shoot.subsurface(self.enemy1_rect)

        #中飞机
        self.enemy2_rect = pygame.Rect(0,0,69,93)
        self.enemy2_img = self.shoot.subsurface(self.enemy2_rect)

        #英雄飞机
        self.hero_rect = pygame.Rect(0,99,100,130)
        self.hero_img = self.shoot.subsurface(self.hero_rect)

        #子弹
        self.bullet_rect = pygame.Rect(1004,987,9,21)
        self.bullet_img = self.shoot.subsurface(self.bullet_rect)

        #敌机子弹
        self.embullet_rect = pygame.Rect(66,74,15,26)
        self.embullet_img = self.shoot.subsurface(self.embullet_rect)

        #初始化英雄位移速度
        self.offset = {pygame.K_RIGHT:0,pygame.K_LEFT:0,pygame.K_UP:0,pygame.K_DOWN:0}

        # 初始化得分
        self.score = 0
        self.score_font = pygame.font.Font(None, 36)

        # 游戏结束图片
        self.gameover = pygame.image.load('./img/gameover.png')

        #游戏运行初始化
        self.running = True

        #音乐初始化
        pygame.mixer.music.load('./sound/game_music.wav')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.25)

        self.enemy1_down_sound = pygame.mixer.Sound('./sound/enemy1_down.wav')
        self.enemy1_down_sound.set_volume(0.5)

        #定时器
        #
        #1.每1s触发敌机事件
        pygame.time.set_timer(ENEMY1_EVENT,1000)
        pygame.time.set_timer(ENEMY2_EVENT,2000)
        pygame.time.set_timer(HERO_FIRE_EVENT,400)
        pygame.time.set_timer(ENEMY_FIRE_EVENT,400)
        pygame.time.set_timer(ENEMY1_FIRE_EVENT,400)

        #创建精灵组
        self.__create_sprite()

    #创建精灵组
    def __create_sprite(self):
        #背景精灵
        bg1 = Background()
        bg2 = Background(is_second=True)
        self.bg_group = pygame.sprite.Group(bg1,bg2)

        #敌机精灵
        self.enemy1 = Enemy(self.enemy1_img)
        self.enemy_group = pygame.sprite.Group()
        #敌机精灵2
        self.enemy2 = Enemy(self.enemy2_img)
        self.enemy2_group = pygame.sprite.Group()

        #英雄精灵
        self.hero = Hero(self.hero_img)
        self.hero_group = pygame.sprite.Group(self.hero)

    #开始游戏
    def start_game(self):
        print('游戏开始')

        while self.running:
            #设置帧率
            self.clock.tick(60)

            #调用事件监听
            self.__event_monitor()

            #检测碰撞
            self._collied()

            #更新并绘制精灵组
            self.__update_sprite_group()

            #打印得分
            self.__score()

            #刷新屏幕
            pygame.display.update()
    #事件监听
    def __event_monitor(self):
        for event in pygame.event.get():

            #监听 关闭窗口
            if event.type == pygame.QUIT:
                self.__gameover()

            #监听小敌机事件
            if event.type == ENEMY1_EVENT:
                self.enemy1 = Enemy(self.enemy1_img)
                self.enemy_group.add(self.enemy1)
            #监听中敌机事件
            elif event.type == ENEMY2_EVENT:
                self.enemy2 = Enemy(self.enemy2_img)
                self.enemy2_group.add(self.enemy2)

            #监听英雄移动
            elif event.type == pygame.KEYDOWN:
                if event.key in self.offset:
                    self.offset[event.key] = 10
            elif event.type == pygame.KEYUP:
                if event.key in self.offset:
                    self.offset[event.key] = 0

            #监听发射子弹事件
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire(self.bullet_img)

            #监听敌机发射子弹事件
            elif event.type == ENEMY_FIRE_EVENT:
                self.enemy1.fire(self.embullet_img)
            elif event.type == ENEMY1_FIRE_EVENT:
                self.enemy2.fire(self.embullet_img)


    #飞机,子弹碰撞
    def _collied(self):
        #子弹碰撞敌机1
        bullet = pygame.sprite.groupcollide(self.hero.bullet, self.enemy_group, True, True)
        if len(bullet) > 0:
            self.score += 10
            self.enemy1_down_sound.play()
        # 子弹碰撞敌机2
        bullet2 = pygame.sprite.groupcollide(self.hero.bullet, self.enemy2_group, True, True)
        if len(bullet2) > 0:
            self.score += 30
            self.enemy1_down_sound.play()

        #敌机碰撞英雄
        enemy_list = pygame.sprite.spritecollide(self.hero, self.enemy_group,True)
        # 如果列表有值, 说明英雄和敌机已经碰撞
        if len(enemy_list) > 0:
        # 杀死英雄
            self.hero.kill()
        # 结束游戏
            self.running = False
            self.gameover_before()

        #敌机2碰撞英雄
        enemy2_list = pygame.sprite.spritecollide(self.hero, self.enemy2_group,True)
        # 如果列表有值, 说明英雄和敌机已经碰撞
        if len(enemy2_list) > 0:
            # 杀死英雄
            self.hero.kill()
            # 结束游戏
            self.running = False
            self.gameover_before()

        #小飞机子弹碰撞英雄
        enemy_bullet_list = pygame.sprite.spritecollide(self.hero,self.enemy1.embullet_group,True)
        if len(enemy_bullet_list) > 0:
            #杀死英雄
            self.hero.kill()
            #结束游戏
            self.running = False
            self.gameover_before()

        #大飞机子弹碰撞英雄
        enemy1_bullet_list = pygame.sprite.spritecollide(self.hero,self.enemy2.embullet_group,True)
        if len(enemy1_bullet_list) > 0:
            self.hero.kill()
            self.running = False
            self.gameover_before()

    #更新绘制精灵组
    def __update_sprite_group(self):
        #背景精灵组
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        #敌机精灵组
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        #敌机精灵组2
        self.enemy2_group.update()
        self.enemy2_group.draw(self.screen)

        #英雄精灵组
        self.hero_group.update(self.offset)
        self.hero_group.draw(self.screen)

        #子弹精灵组
        self.hero.bullet.update()
        self.hero.bullet.draw(self.screen)

        # #敌机子弹精灵组1
        # self.enemy1.embullet_group.update()
        # self.enemy1.embullet_group.draw(self.screen)
        #
        # #敌机子弹精灵组2
        # self.enemy2.embullet_group.update()
        # self.enemy2.embullet_group.draw(self.screen)

    def __score(self):
        self.score_text = self.score_font.render(str(self.score), True, (128, 128, 128))
        self.text_rect = self.score_text.get_rect()
        self.text_rect.topleft = [10, 10]
        self.screen.blit(self.score_text, self.text_rect)

    def gameover_before(self):
        font = pygame.font.Font(None, 48)
        text = font.render('Score: ' + str(self.score), True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx
        text_rect.centery = self.screen.get_rect().centery + 50

        self.screen.blit(self.gameover, (0, 0))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        game_over_sound = pygame.mixer.Sound('./sound/game_over.wav')
        game_over_sound.set_volume(0.3)
        game_over_sound.play()
        pygame.mixer.music.stop()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('游戏结束')

                    pygame.quit()
                    exit()


    #游戏结束
    def __gameover(self):
        print('游戏结束')
        pygame.quit()
        exit()

game = Plane()
game.start_game()
print('GameOver')


