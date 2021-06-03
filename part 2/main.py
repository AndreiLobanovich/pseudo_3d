import pygame
from settings import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

font = pygame.font.SysFont('Arial', 36, bold=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    ray_casting(sc, player.pos, player.angle)

    display_fps = str(int(clock.get_fps()))
    render = font.render(display_fps, 0, RED)
    sc.blit(render, (1100, 700))

    pygame.display.flip()
    clock.tick(FPS)