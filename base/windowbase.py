import pygame


class WindowCreation:
    def __init__(self, W, H):
        self.W = W
        self.H = H
        self.window = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()

    def get_window(self):
        return self.window

    def get_pos(self, col, row):
        return int(self.W*col), int(self.H*row)

    def get_len(self, width, height):
        return int(self.W*width), int(self.H*height)
