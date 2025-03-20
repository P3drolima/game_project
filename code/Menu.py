#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect, QUIT, MOUSEBUTTONDOWN
from pygame.font import Font

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_RED, COLOR_BLACK


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('./asset/background-day.png').convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font_title = pygame.font.Font(None, 100)  # Fonte para o título
        self.font_options = pygame.font.Font(None, 74)  # Fonte para as opções
        self.title_text = self.font_title.render("Fly Bird", True, COLOR_RED)  # Título
        self.play_text = self.font_options.render("Play", True, COLOR_BLACK)  # Opção Play
        self.exit_text = self.font_options.render("Exit", True, COLOR_BLACK)  # Opção Exit
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))  # Posição do título
        self.play_rect = self.play_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Posição do Play
        self.exit_rect = self.exit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))  # Posição do Exit

    def draw(self):
        # Desenha o fundo
        self.screen.blit(self.background, (0, 0))
        # Desenha o título
        self.screen.blit(self.title_text, self.title_rect)
        # Desenha as opções
        self.screen.blit(self.play_text, self.play_rect)
        self.screen.blit(self.exit_text, self.exit_rect)
        pygame.display.update()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if self.play_rect.collidepoint(event.pos):
                    return "play"
                elif self.exit_rect.collidepoint(event.pos):
                    return "exit"
        return None
