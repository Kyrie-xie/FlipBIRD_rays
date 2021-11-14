'''
@Editor: Jinxing
@Description: FlipBird-ray
'''
from time import sleep
import pygame
import flipbird_function

# Parameters:
H: int = 900
W: int = 1500
SIZE = (W,H )
BIRD_ROW: int = 50
BIRD_COL: int = 200
BIRD_HEIGHT = int(H/BIRD_ROW)
BIRD_WIDTH = int(W/BIRD_COL)

tick: int = 20

BIRD_COLOR : tuple = (176,48,96)
RAYS_COLOR : tuple = (30, 144, 255)
BG_COLOR: tuple = (0,0,0)


BIRD_X =  int(BIRD_COL/10) # 鸟的x是不动的，只在y上进行变动,
BIRD_Y =  int(BIRD_ROW/2) # Note: 鸟的位置是col， row，不是绝对位置


DOWN_SPEED = 0.1 # 下降的速度和上升的速度
UP_SPEED = 6

RAYS_LEN = 100
RAYS_WIDTH = 10
RAYS_ROW = H/RAYS_WIDTH
RAYS_SPEED = 6

K = 30 # 初始化发射射线的帧数（频率）

GRAVITY = 1.01
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
                              DOWN_SPEED,
                              GRAVITY
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


def show_score(score_):
    _score = font.render('Score : ' + str(score_), True, (255,255,255))
    window.blit(_score, (5,5))

def show_dead(score_):
    pygame.draw.rect(window, (0, 0, 0), (0, 0, W, H))  # 背景
    _cai = font.render('Que Shi Cai', True, (255, 255, 255))
    window.blit(_cai, (int(W/2), int(H  / 2)))


# 死掉？
dead_ = flipbird_function.dead(bird,
                               BIRD_WIDTH,
                               BIRD_HEIGHT,
                               RAYS_WIDTH,
                               RAYS_LEN)





show_dead(score)
pygame.display.flip()
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
    K *= 0.999
    if not score % int(K): # 每K帧发射一次射线
        shooter.add_ray()


    # 渲染 - 画面
    pygame.draw.rect(window, BG_COLOR, (0, 0, W, H))  # 背景

    bird_rect(*bird(), BIRD_COLOR)  # 画出鸟的位置

    RAYS_SPEED *= 1.000000001 #加速

    ray_list = shooter(int(RAYS_SPEED))
    for ray in ray_list :
        y = ray[0]
        head = max(0, ray[1])
        tail = min(W, ray[1]+RAYS_LEN)
        rays_rect(head, y, RAYS_COLOR, tail)

    show_score(score)

    dead = dead_(ray_list)
    if dead:
        break

    pygame.display.flip()  # 让出控制权给系统


    # 设置帧数
    clock.tick(tick)

# 收尾工作
show_dead(score)
pygame.display.flip()
sleep(1)
pygame.display.quit()
pygame.quit()
