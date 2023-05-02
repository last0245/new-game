import pygame

from common.constant import HALF_ROOT2, DisplayOrder
from common.params import img_bg, window_size_y, window_size_x
from display.display import Display
from player.player import PlayerParams


class BackGround:

    def __init__(self):
        img_size_x, img_size_y = img_bg.get_size()
        self.offset_x = int((img_size_x - window_size_x) / 2)
        self.offset_y = int((img_size_y - window_size_y) / 2)

        self.size_x = max(window_size_x, img_size_x)
        self.size_y = max(window_size_y, img_size_y)

    def move(self, key, x, y):
        PlayerParams.speed = 10

        key_x = key[pygame.K_RIGHT] - key[pygame.K_LEFT]
        key_y = key[pygame.K_DOWN] - key[pygame.K_UP]

        # 斜め入力は補正する
        if key_x and key_y:
            key_x *= HALF_ROOT2
            key_y *= HALF_ROOT2

        x = (x + key_x * PlayerParams.speed) % self.size_x
        y = (y + key_y * PlayerParams.speed) % self.size_y

        for i in range(2):
            bg_x = self.size_x * i - x

            for j in range(2):
                bg_y = self.size_y * j - y
                Display.set_back_ground(img_bg, bg_x, bg_y)

        return x, y
