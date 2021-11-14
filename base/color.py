'''
@Editor: Jinxing
@Description:
'''
import time


class Color:
    black = (0, 0, 0)
    green = (0, 200, 0)
    white = (255, 255, 255)
    dark_red = (200, 0, 0)
    bright_green = (0, 255, 0)
    leaf_green = (0, 175, 75)
    brown = (102, 51, 0)
    red = (255, 0, 0)

color = Color()

__all__ = ['color']

if __name__ == '__main__':
    print(color.red)