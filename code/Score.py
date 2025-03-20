import random

import pygame

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_GAP
from code.Pipe import Pipe


class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 74)
        self.text = self.font.render(str(self.score), True, (255, 255, 255))
        self.rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, 50))

    def update(self):
        self.text = self.font.render(str(self.score), True, (255, 255, 255))

    def draw(self, screen):
        screen.blit(self.text, self.rect)

    def increase(self):
        self.score += 1  # Aumenta a pontuação

# Função para verificar se um sprite saiu da tela
def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

# Função para gerar canos aleatórios
def get_random_pipes(xpos):
    size = random.randint(100, 300)
    pipe = Pipe(False, xpos, size)
    pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
    return (pipe, pipe_inverted)