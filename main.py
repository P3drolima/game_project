import sys

import pygame

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Game import main_game
from code.Menu import Menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu = Menu(screen)

    while True:
        menu.draw()
        action = menu.handle_input()
        if action == "play":
            main_game()
        elif action == "exit":
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
