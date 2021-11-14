import pygame, os,time
from FlipBIRD_rays.base.color import color
from FlipBIRD_rays.base.windowbase import WindowCreation
from FlipBIRD_rays.engine.main import Game_Main
from FlipBIRD_rays.engine._music import define_music


class StartSurf:
    def __init__(self,
                 window: WindowCreation):
        self.window = window
        pygame.font.init()
        self.font = pygame.font.Font('freesansbold.ttf', 80)
        # self.start_bottom()
        self.button: bool
        self.clock = pygame.time.Clock()

    def show(self):
        _quit = False
        _start = False
        define_music(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'music/bkg_music1.mp3'))
        while not _quit:
            pygame.draw.rect(self.window.get_window(), color.black, (0, 0, self.window.W, self.window.H))  # 背景

            TextSurf, TextRect = self.text_objects('FlipSpaceShip', color.white)
            TextRect.center = self.window.get_pos(0.5, 0.35)
            self.window.get_window().blit(TextSurf, TextRect)

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    _quit = True
                    break
            _start = self.button('Play', *self.window.get_pos(0.4, 0.55),
                                 *self.window.get_len(0.2, 0.09), color.red, color.green)

            _quit = self.button('Quit', *self.window.get_pos(0.4, 0.69),
                                 *self.window.get_len(0.2, 0.09), color.red, color.green)

            if _start:
                define_music(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'music/bkg_music0.mp3'))
                main = Game_Main(self.window.get_window(), self.font)
                main.run()
                _start = False
                define_music(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'music/bkg_music1.mp3'))
                time.sleep(2)

            pygame.display.flip()
            self.clock.tick(100)


    def text_objects(self, text, _color):
        textSurface = self.font.render(text, True, _color)
        return textSurface, textSurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac):

        mouse = pygame.mouse.get_pos()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.window.get_window(), ac, (x - 10, y - 10, w + 20, h + 20))
            TextSurf, TextRect = self.text_objects(msg, color.black)
            TextRect.center = (x + (w / 2), (y + (h / 2)))
            self.window.get_window().blit(TextSurf, TextRect)
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            pygame.draw.rect(self.window.get_window(), ic, (x, y, w, h))
            TextSurf, TextRect = self.text_objects(msg, color.black)
            TextRect.center = (x + (w / 2), (y + (h / 2)))
            self.window.get_window().blit(TextSurf, TextRect)
        return False


if __name__ == '__main__':
    import sys

    display_width = 1500
    H = 750
    H: int = 900
    W: int = 1500
    SIZE = (W, H)
    window = WindowCreation(*SIZE)

    pygame.display.set_caption('FlipBird')

    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 32)

    s = StartSurf(window)
    s.show()
    pygame.display.quit()
    pygame.quit()
    print('ok')
    sys.exit()
