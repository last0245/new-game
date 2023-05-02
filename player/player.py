import pygame

from common.constant import HALF_ROOT2, DisplayOrder
from common.params import img_player
from display.display import Display
from weapon.weapon import Gun



class PlayerParams:
    speed = 10
    attack_interval = 15


class Player:
    attack_interval_cnt = 0

    # 入力をやめた時に何回前の入力まで参照するか
    PRE_CNT = 5
    pre_x_list = [0] * PRE_CNT
    pre_y_list = [0] * PRE_CNT

    def __init__(self, x, y):
        img_size_x, img_size_y = img_player.get_size()
        self.offset_x = img_size_x / 2
        self.offset_y = img_size_y / 2

        # 位置
        self.x = x
        self.y = y
        # 向き
        self.dx = 0
        self.dy = -1
        # 武器
        self.weapon = Gun()

    def move(self, key, x, y):
        key_x = key[pygame.K_RIGHT] - key[pygame.K_LEFT]
        key_y = key[pygame.K_DOWN] - key[pygame.K_UP]

        self.pre_x_list = self.pre_x_list[1:] + [key_x]
        self.pre_y_list = self.pre_y_list[1:] + [key_y]

        # 向きの更新
        if key_x or key_y:
            self.dx = self.get_dx()
            self.dy = self.get_dy()

        # todo 移動制限は画面側で行う
        # 移動
        # self.x = x
        # self.y = y

        # todo 背景の移動と打ち消しあう必要がある
        Display.set_reserve_blit(DisplayOrder.Player, img_player, self.x - self.offset_x, self.y - self.offset_y)

        self.weapon.move()
        self.attack_interval_cnt += 1
        # インターバルごとに攻撃する
        if self.attack_interval_cnt >= PlayerParams.attack_interval:
            self.attack_interval_cnt = 0
            dx = self.dx
            dy = self.dy
            # 斜め入力は補正する
            if dx and dy:
                dx = self.dx * HALF_ROOT2
                dy = self.dy * HALF_ROOT2
            self.weapon.attack(self.x, self.y, dx, dy)

    def get_dx(self):
        for pre_x in self.pre_x_list:
            if pre_x:
                return pre_x
        return 0

    def get_dy(self):
        for pre_y in self.pre_y_list:
            if pre_y:
                return pre_y
        return 0
