import sys

import pygame
from pygame import QUIT, KEYDOWN, K_SPACE

from code.Bird import Bird
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_WIDTH, FPS, PIPE_WIDTH
from code.Ground import Ground
from code.Score import Score, get_random_pipes, is_off_screen


def main_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BACKGROUND = pygame.image.load('./asset/background-day.png')
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

    bird_group = pygame.sprite.Group()
    bird = Bird()
    bird_group.add(bird)

    ground_group = pygame.sprite.Group()
    for i in range(2):
        ground = Ground(GROUND_WIDTH * i)
        ground_group.add(ground)

    pipe_group = pygame.sprite.Group()
    for i in range(2):
        pipes = get_random_pipes(SCREEN_WIDTH * i + 800)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])

    score = Score()  # Instância do placar
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)  # Controla o FPS do jogo
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    bird.bump()

        screen.blit(BACKGROUND, (0, 0))

        # Verifica se o pássaro passou por um par de canos
        for pipe in pipe_group:
            if pipe.rect[0] + PIPE_WIDTH < bird.rect[0] and not hasattr(pipe, 'scored'):
                score.increase()  # Aumenta a pontuação
                pipe.scored = True  # Marca o cano como pontuado

        if is_off_screen(ground_group.sprites()[0]):
            ground_group.remove(ground_group.sprites()[0])
            new_ground = Ground(GROUND_WIDTH - 20)
            ground_group.add(new_ground)

        if is_off_screen(pipe_group.sprites()[0]):
            pipe_group.remove(pipe_group.sprites()[0])
            pipe_group.remove(pipe_group.sprites()[0])
            pipes = get_random_pipes(SCREEN_WIDTH * 2)
            pipe_group.add(pipes[0])
            pipe_group.add(pipes[1])

        bird_group.update()
        ground_group.update()
        pipe_group.update()

        bird_group.draw(screen)
        pipe_group.draw(screen)
        ground_group.draw(screen)

        score.update()
        score.draw(screen)  # Desenha o placar na tela

        pygame.display.update()

        if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or
                pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
            return  # Fim de jogo
