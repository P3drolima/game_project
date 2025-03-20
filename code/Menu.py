#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect, QUIT, MOUSEBUTTONDOWN
from pygame.font import Font

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.play_text = self.font.render("Play", True, (255, 255, 255))
        self.exit_text = self.font.render("Exit", True, (255, 255, 255))
        self.play_rect = self.play_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.exit_rect = self.exit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    def draw(self):
        self.screen.fill((0, 0, 0))
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