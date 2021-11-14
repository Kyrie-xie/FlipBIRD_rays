from time import sleep
import pygame
from FlipBIRD_rays.engine import flipbird_function
import time
from FlipBIRD_rays.base.color import  color


##########
# Codes: #
##########
class Game_Main:
    # Parameters:
    H: int = 900
    W: int = 1500
    BIRD_ROW: int = 50
    BIRD_COL: int = 200
    BIRD_HEIGHT = int(H / BIRD_ROW)
    BIRD_WIDTH = int(W / BIRD_COL)

    tick: int = 100

    BIRD_COLOR: tuple = (176, 48, 96)
    RAYS_COLOR: tuple = (30, 144, 255)
    BG_COLOR: tuple = (0, 0, 0)

    BIRD_X = int(BIRD_COL / 10)  # 鸟的x是不动的，只在y上进行变动,
    BIRD_Y = int(BIRD_ROW / 2)  # Note: 鸟的位置是col， row，不是绝对位置

    DOWN_SPEED = 0.1  # 下降的速度和上升的速度
    UP_SPEED = 6

    RAYS_LEN = 100
    RAYS_WIDTH = 10
    RAYS_ROW = H / RAYS_WIDTH
    RAYS_SPEED = 6

    K = 30  # 初始化发射射线的帧数（频率）

    GRAVITY = 1.01

    def __init__(self, window, font):
        self.window = window
        self.font = font

    def run(self):
        s0 = time.time()  # 活着的时间
        dead = False
        quit = False
        score = 0

        clock = pygame.time.Clock()
        # 给鸟初始化
        bird = flipbird_function.BIRD(self.BIRD_X,
                                      self.BIRD_Y,
                                      self.UP_SPEED,
                                      self.DOWN_SPEED,
                                      self.GRAVITY
                                      )
        # 初始化射线发射器
        shooter = flipbird_function.rays(self.RAYS_LEN,
                                         self.RAYS_ROW,
                                         self.W
                                         )

        # 方块画手
        bird_rect = flipbird_function.Draw_Rect(self.BIRD_HEIGHT,
                                                self.BIRD_WIDTH,
                                                self.window)
        rays_rect = flipbird_function.RAY_Draw_Rect(self.RAYS_WIDTH,
                                                    self.RAYS_LEN,
                                                    self.window)

        dead_ = flipbird_function.dead(bird,
                                       self.BIRD_WIDTH,
                                       self.BIRD_HEIGHT,
                                       self.RAYS_WIDTH,
                                       self.RAYS_LEN)



        pygame.display.flip()

        while not quit and not dead:
            score += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == 32:  # 回车让鸟飞高
                        bird.up()

            bird.down()  # 鸟的自然下降

            # 发射射线
            self.K *= 0.999
            if not score % int(self.K):  # 每K帧发射一次射线
                shooter.add_ray()

            # 渲染 - 画面
            pygame.draw.rect(self.window, self.BG_COLOR, (0, 0, self.W, self.H))  # 背景

            bird_rect(*bird(), self.BIRD_COLOR)  # 画出鸟的位置

            self.RAYS_SPEED *= 1.000000001  # 加速

            ray_list = shooter(int(self.RAYS_SPEED))
            for ray in ray_list:
                y = ray[0]
                head = max(0, ray[1])
                tail = min(self.W, ray[1] + self.RAYS_LEN)
                rays_rect(head, y, self.RAYS_COLOR, tail)

            self.show_score(int(time.time() - s0))

            dead = dead_(ray_list)
            if dead:
                break

            pygame.display.flip()  # 让出控制权给系统

            # 设置帧数
            clock.tick(self.tick)

        self.show_dead(time.time() - s0)

        # 收尾工作
        self.show_dead(score)
        pygame.display.flip()
        sleep(1)

    def show_score(self, score_):
        _score = self.font.render('Score : ' + str(score_), True, (255, 255, 255))
        self.window.blit(_score, (5, 5))

    def show_dead(self, score_):
        pygame.draw.rect(self.window, (0, 0, 0), (0, 0, self.W, self.H))  # 背景
        # _cai = self.font.render('Dead', True, (255, 255, 255))
        # _cai.center = (self.W/2, self.H/2)
        # self.window.blit(_cai, (int(self.W / 2), int(self.H / 2)))
        TextSurf, TextRect = self.text_objects('Dead', color.white)
        TextRect.center = (self.W/2, self.H/2)
        self.window.blit(TextSurf, TextRect)

    def text_objects(self, text, _color):
        textSurface = self.font.render(text, True, _color)
        return textSurface, textSurface.get_rect()
#
# def main(window):
#     # Parameters:
#     H: int = 900
#     W: int = 1500
#     BIRD_ROW: int = 50
#     BIRD_COL: int = 200
#     BIRD_HEIGHT = int(H / BIRD_ROW)
#     BIRD_WIDTH = int(W / BIRD_COL)
#
#     tick: int = 20
#
#     BIRD_COLOR: tuple = (176, 48, 96)
#     RAYS_COLOR: tuple = (30, 144, 255)
#     BG_COLOR: tuple = (0, 0, 0)
#
#     BIRD_X = int(BIRD_COL / 10)  # 鸟的x是不动的，只在y上进行变动,
#     BIRD_Y = int(BIRD_ROW / 2)  # Note: 鸟的位置是col， row，不是绝对位置
#
#     DOWN_SPEED = 0.1  # 下降的速度和上升的速度
#     UP_SPEED = 6
#
#     RAYS_LEN = 100
#     RAYS_WIDTH = 10
#     RAYS_ROW = H / RAYS_WIDTH
#     RAYS_SPEED = 6
#
#     K = 30  # 初始化发射射线的帧数（频率）
#
#     GRAVITY = 1.01
#     score = 0  # 活着的时间
#     dead = False
#     quit = False
#
#     clock = pygame.time.Clock()
#     # 给鸟初始化
#     bird = flipbird_function.BIRD(BIRD_X,
#                                   BIRD_Y,
#                                   UP_SPEED,
#                                   DOWN_SPEED,
#                                   GRAVITY
#                                   )
#     # 初始化射线发射器
#     shooter = flipbird_function.rays(RAYS_LEN,
#                                      RAYS_ROW,
#                                      W
#                                      )
#
#     # 方块画手
#     bird_rect = flipbird_function.Draw_Rect(BIRD_HEIGHT,
#                                             BIRD_WIDTH,
#                                             window)
#     rays_rect = flipbird_function.RAY_Draw_Rect(RAYS_WIDTH,
#                                                 RAYS_LEN,
#                                                 window)
#
#     pygame.font.init()
#     font = pygame.font.Font('freesansbold.ttf', 32)
#
#     # 死掉？
#     dead_ = flipbird_function.dead(bird,
#                                    BIRD_WIDTH,
#                                    BIRD_HEIGHT,
#                                    RAYS_WIDTH,
#                                    RAYS_LEN)
#
#     show_dead(score)
#     pygame.display.flip()
#     while not quit and not dead:
#         score += 1
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 quit = True
#                 break
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == 32:  # 回车让鸟飞高
#                     bird.up()
#
#         bird.down()  # 鸟的自然下降
#
#         # 发射射线
#         K *= 0.999
#         if not score % int(K):  # 每K帧发射一次射线
#             shooter.add_ray()
#
#         # 渲染 - 画面
#         pygame.draw.rect(window, BG_COLOR, (0, 0, W, H))  # 背景
#
#         bird_rect(*bird(), BIRD_COLOR)  # 画出鸟的位置
#
#         RAYS_SPEED *= 1.000000001  # 加速
#
#         ray_list = shooter(int(RAYS_SPEED))
#         for ray in ray_list:
#             y = ray[0]
#             head = max(0, ray[1])
#             tail = min(W, ray[1] + RAYS_LEN)
#             rays_rect(head, y, RAYS_COLOR, tail)
#
#         show_score(score)
#
#         dead = dead_(ray_list)
#         if dead:
#             break
#
#         pygame.display.flip()  # 让出控制权给系统
#
#         # 设置帧数
#         clock.tick(tick)
#
#     # 收尾工作
#     show_dead(score)
#     pygame.display.flip()
#     sleep(1)
