from common.constant import DisplayOrder
from common.params import img_weapon
from display.display import Display


class Gun:
    MAX_ATTACK = 100

    bullet_list = []

    def attack(self, x, y, dx, dy):
        """攻撃"""
        if len(self.bullet_list) < self.MAX_ATTACK:
            bullet = Bullet(x, y, dx, dy)
            self.bullet_list.append(bullet)

    def move(self):
        """移動"""
        remove_list = []

        for bullet in self.bullet_list:
            if bullet.validate():
                bullet.move()
            else:
                remove_list.append(bullet)

        for bullet in remove_list:
            self.bullet_list.remove(bullet)


class Bullet:
    SHOOTING_RANGE = 200
    SPEED = 8

    def __init__(self, x, y, dx, dy):
        self.start_x = x
        self.start_y = y

        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx * self.SPEED
        self.y += self.dy * self.SPEED
        Display.set_reserve_blit(DisplayOrder.Weapon, img_weapon, self.x, self.y)

    def validate(self):
        x = (self.x - self.start_x) ** 2
        y = (self.y - self.start_y) ** 2
        return x + y < self.SHOOTING_RANGE ** 2
