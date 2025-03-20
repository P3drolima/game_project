import random

import pygame

from code.Const import GROUND_WIDTH, GROUND_HEIGHT, SCREEN_HEIGHT, GAME_SPEED, PIPE_GAP
from code.Pipe import Pipe


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./asset/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED


# Função para verificar se um sprite saiu da tela
def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


# Função para gerar canos aleatórios
def get_random_pipes(xpos):
    size = random.randint(100, 300)
    pipe = Pipe(False, xpos, size)
    pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
    return pipe, pipe_inverted
