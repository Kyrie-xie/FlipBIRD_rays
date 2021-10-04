'''
@Editor: Jinxing
@Description:
'''
import random

import pygame
import numpy as np

# Code
class BIRD:
    def __init__(self,
                 init_x,
                 init_y,
                 up_once,
                 down_once):
        self.x = init_x
        self.y = init_y
        self.up_mv = up_once
        self.down_mv = down_once

    def up(self):
        self.y -= self.up_mv

    def down(self):
        self.y += self.down_mv

    def __call__(self):
        return self.x, self.y

class Draw_Rect:
    def __init__(self,
                 cell_height,
                 cell_width,
                 window):
        self.cell_height = cell_height
        self.cell_width = cell_width
        self.window = window


    def __call__(self,
                  cordn_x,
                  cordn_y,
                  color):
        left = cordn_x*(self.cell_width)
        top = cordn_y*(self.cell_height)
        pygame.draw.rect(
            self.window, color,
            (left, top, self.cell_width, self.cell_width )
        )

class RAY_Draw_Rect:
    def __init__(self,
                 cell_height,
                 cell_width,
                 window):
        self.cell_height = cell_height
        self.cell_width = cell_width
        self.window = window


    def __call__(self,
                  cordn_x,
                  cordn_y,
                  color):
        top = cordn_y*(self.cell_height)
        pygame.draw.rect(
            self.window, color,
            (cordn_x, top, self.cell_width, self.cell_height )
        )

class rays:
    def __init__(self,
                 rays_len,
                 rows_num,
                 W):
        # 射线的长度, 射线能生成的rows 和 屏幕（window）的宽度，
        self.W = W
        self.rays_len = rays_len
        self.rows_num = rows_num
        self.rays = np.array([[random.randint(0, self.rows_num), self.W]]) # rays 是一个numpy array\
                                    # rows: 射线id
                                    # cols:
                                        # 1： rows of the ray
                                        # 2: 图片中显示的头

    def add_ray(self):
        # 随机一个rows去加入一个射线
        new_row = random.randint(0, self.rows_num)
        new_arr = np.array([[new_row, self.W]])
        self.rays = np.append(new_arr, self.rays, axis = 0)

    def __len__(self):
        return self.rays.shape[0]

    def __call__(self, speed):
        # 输入speed (方便在主程序中加入随机或者逐渐变快的speed)
        # 返回self.rays
        self.rays[:,1] -= speed
        for i,ray in enumerate(self.rays[::-1]):
            if ray[1]> -self.rays_len:
                break
        return self.rays[:self.__len__() - i]

class show_score:
    def __init__(self,window, font):
        self.window = window
        self.font = font

    def __call__(self, score_):
        _score = self.font.render('Score : ' + str(score_), True, (0,0,0))
        self.window.blit(_score, (5,5))


