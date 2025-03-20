import pygame

from code.Const import SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, GRAVITY


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load('./asset/bluebird-upflap.png').convert_alpha(),
            pygame.image.load('./asset/bluebird-midflap.png').convert_alpha(),
            pygame.image.load('./asset/bluebird-downflap.png').convert_alpha()
        ]
        self.speed = SPEED
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.speed += GRAVITY
        self.rect[1] += self.speed  # Atualiza a altura

    def bump(self):
        self.speed = -SPEED  # Faz o pássaro "pular"
