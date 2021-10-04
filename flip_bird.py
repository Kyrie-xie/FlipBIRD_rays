'''
@Editor: Jinxing
@Description: FlipBird-ray
'''
import time
from time import sleep
import pygame
import random
import flipbird_function

# Parameters:
H: int = 600
W: int = 2000
SIZE = (W,H )
BIRD_ROW: int = 50
BIRD_COL: int = 200
BIRD_HEIGHT = int(H/BIRD_ROW)
BIRD_WIDTH = int(W/BIRD_COL)

tick: int = 10

BIRD_COLOR : tuple[int,int,int] = (176,48,96)
RAYS_COLOR : tuple[int,int,int] = (30, 144, 255)
BG_COLOR: tuple[int,int,int] = (0,0,0)


BIRD_X =  int(BIRD_COL/10) # 鸟的x是不动的，只在y上进行变动,
BIRD_Y =  int(BIRD_ROW/2) # Note: 鸟的位置是col， row，不是绝对位置


DOWN_SPEED = 1 # 下降的速度和上升的速度
UP_SPEED = 8

RAYS_LEN = 100
RAYS_ROW = 100
RAYS_WIDTH = 10
RAYS_SPEED = 20


##########
# Codes: #
##########
score = 0 # 活着的时间
dead = False
quit = False
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption('FlipBird')
clock = pygame.time.Clock()


# 给鸟初始化
bird = flipbird_function.BIRD(BIRD_X,
                              BIRD_Y,
                              UP_SPEED,
                              DOWN_SPEED
                              )
# 初始化射线发射器
shooter = flipbird_function.rays(RAYS_LEN,
                                 RAYS_ROW,
                                 W
                                 )

# 方块画手
bird_rect = flipbird_function.Draw_Rect(BIRD_HEIGHT,
                                   BIRD_WIDTH,
                                   window)
rays_rect = flipbird_function.RAY_Draw_Rect(RAYS_WIDTH,
                                        RAYS_LEN,
                                        window)
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
board = flipbird_function.show_score(window,)

while not quit and not dead:
    score += 1
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            quit = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == 32: #回车让鸟飞高
                bird.up()

    bird.down() #鸟的自然下降





    # 发射射线
    if not score % 5: # 每五帧发射一次射线
        shooter.add_ray()


    # 渲染 - 画面
    pygame.draw.rect(window, BG_COLOR, (0, 0, W, H))  # 背景

    bird_rect(*bird(), BIRD_COLOR)  # 画出鸟的位置

    ray_list = shooter(RAYS_SPEED)
    for ray in ray_list :
        y = ray[0]
        head = max(0, ray[1])
        tail = min(W, ray[1]+RAYS_LEN)
        rays_rect(head, y, RAYS_COLOR)


    pygame.display.flip()  # 让出控制权给系统


    # 设置帧数
    clock.tick(tick)

# 收尾工作
if not quit:
    sleep(10)
pygame.display.quit()
pygame.quit()