import pygame

#初始化游戏
pygame.init()

#初始化窗口
screen = pygame.display.set_mode((480,700))

#初始化游戏背景
background = pygame.image.load('../Game/img/background.png')
#绘制图像
screen.blit(background,(0,0))
#刷新图像
pygame.display.update()

#1.1加载大图
plane_img = pygame.image.load('../Game/img/shoot.png')
#1.2设置矩形,用于框中其中一架飞机
plane_rect = pygame.Rect(0,102,99,128)
#1.3扣出飞机
plane = plane_img.subsurface(plane_rect)
plane2 = plane_img.subsurface(plane_rect)

#2.显示图像
plane_pos = [20,500]
plane_pos2 = [360,500]

screen.blit(plane, plane_pos)
screen.blit(plane2, plane_pos2)

#3.刷新屏幕
pygame.display.update()


#````````````````````````````````````````````````````````

#初始化位置(存储上下左右按键)
offset = {pygame.K_a:0,pygame.K_d:0,pygame.K_w:0,pygame.K_s:0}
offset2 = {pygame.K_LEFT:0,pygame.K_RIGHT:0,pygame.K_UP:0,pygame.K_DOWN:0}

while True:


    #重新绘制背景
    screen.blit(background,(0,0))
    #移动我方飞机
    screen.blit(plane,plane_pos)
    screen.blit(plane2,plane_pos2)

    pygame.display.update()

    #事件监听
    for event in  pygame.event.get():

        #判断是否按下按键
        if event.type == pygame.KEYDOWN:
            #判断是否按的是上下左右
            if event.key in offset:
                offset[event.key] = 5
            if event.key in offset2:
                offset2[event.key] = 5
        #判断是否松开按键
        elif event.type == pygame.KEYUP:
            #判断是否按的是上下左右
            if event.key in offset:
                offset[event.key] = 0
            if event.key in offset2:
                offset2[event.key] = 0


        # 退出游戏
        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()               #关闭窗口
            exit()                      #退出程序

    plane_pos[0] = plane_pos[0] + (offset[pygame.K_d]-offset[pygame.K_a])
    plane_pos2[0] = plane_pos2[0] + (offset2[pygame.K_RIGHT]-offset2[pygame.K_LEFT])

    # x轴
    if plane_pos[0] < 0:
        plane_pos[0] = 0
    elif plane_pos[0] > 480 - plane_rect.width:
        plane_pos[0] = 480 - plane_rect.width

    # x轴
    if plane_pos2[0] < 0:
        plane_pos2[0] = 0
    elif plane_pos2[0] > 480 - plane_rect.width:
        plane_pos2[0] = 480 - plane_rect.width

    plane_pos[1] = plane_pos[1] + (offset[pygame.K_s]-offset[pygame.K_w])
    plane_pos2[1] = plane_pos2[1] + (offset2[pygame.K_DOWN]-offset2[pygame.K_UP])

    # y轴
    if plane_pos[1] < 0:
        plane_pos[1] = 0
    elif plane_pos[1] > 700 - plane_rect.height:
        plane_pos[1] = 700 - plane_rect.height

    # y轴
    if plane_pos2[1] < 0:
        plane_pos2[1] = 0
    elif plane_pos2[1] > 700 - plane_rect.height:
        plane_pos2[1] = 700 - plane_rect.height