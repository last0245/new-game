import pygame

from common.params import window_size_x, window_size_y


class Display:
    reserve_blit = []
    screen = pygame.display.set_mode((window_size_x, window_size_y))
    x = 0
    y = 0

    font = pygame.font.Font(None, 20)

    @classmethod
    def set_back_ground(cls, source, x, y):
        cls.x = x
        cls.y = y
        cls.screen.blit(source, [x, y])

    @classmethod
    def set_reserve_blit(cls, order, source, x, y):
        """描画処理の設定"""
        cls.reserve_blit.append([order, source, x, y])

    @classmethod
    def update(cls):
        """描画処理"""
        cls.reserve_blit.sort()

        for _, source, x, y in cls.reserve_blit:
            cls.screen.blit(source, [x, y])

        cls.reserve_blit = []
        pygame.display.update()
        print(cls.x, cls.y)
