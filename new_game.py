import pygame
import sys

from back_ground.back_ground import BackGround
from common.constant import FPS, GAME_TITLE
from common.params import window_size_x, window_size_y
from display.display import Display
from player.player import Player


def main():
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()

    back_ground = BackGround()
    x, y = (back_ground.size_x - window_size_x) / 2, (back_ground.size_y - window_size_y) / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()

        x, y = back_ground.move(key, x, y)
        player.move(key, x, y)

        Display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()

    # exampleゲーム、上のmain()をコメントアウトすること
    # import pygame.examples.aliens
    # pygame.examples.aliens.main()

    # https://github.com/search?q=pygame.examples.aliens.main&type=Code&l=Python
