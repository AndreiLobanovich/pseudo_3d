from settings import *
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.sensitivity = sensitivity

    @property
    def pos(self):
        return self.x, self.y

    def movement(self, world_map):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_w]:
            if not mapping(self.x + player_speed * 2 * cos_a, self.y + player_speed * 2 * sin_a) in world_map:
                self.x += player_speed * cos_a
                self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            if not mapping(self.x - player_speed * 2 * cos_a, self.y - player_speed * 2 * sin_a) in world_map:
                self.x += -player_speed * cos_a
                self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            if not mapping(self.x + player_speed * 2 * sin_a, self.y - player_speed * 2 * cos_a) in world_map:
                self.x += player_speed * sin_a
                self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            if not mapping(self.x - player_speed * 2 * sin_a, self.y + player_speed * 2 * cos_a) in world_map:
                self.x += -player_speed * sin_a
                self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

        self.angle %= DOUBLE_PI

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - WIDTH // 2
            pygame.mouse.set_visible(False)
            pygame.mouse.set_pos((WIDTH / 2, HEIGHT / 2))
            self.angle += difference * self.sensitivity

        self.angle %= DOUBLE_PI
