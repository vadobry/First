"""Module for classes"""
import random

import pygame

size = [700, 500]


class Ball:
    """Ball"""
    # --- Атрибуты класса ---
    # Ball position
    move_x = 0
    move_y = 0

    # Ball's vector
    change_x = 10
    change_y = 0

    # Ball size
    size = 10

    # Ball color
    color = [255, 255, 255]

    # --- Методы класса ---
    def move(self):
        """Move"""
        self.move_x += self.change_x
        screen_w = pygame.display.get_surface().get_width()
        if self.move_x > (screen_w - 10):
            self.change_x = self.change_x * -1
        if self.move_x < 10:
            self.change_x = self.change_x * -1

    def jump(self):
        """jump"""
        self.move_y += self.change_y * -1
        if self.move_y < 80:
            self.change_y = self.change_y * -1
        if self.move_y > 99:
            self.change_y = self.change_y * -1

    def draw(self, screen):
        """draw ball"""
        pygame.draw.circle(screen, self.color, [self.move_x, self.move_y], self.size)


class Block(pygame.sprite.Sprite):
    """block class"""
    """it is inherited from the class Sprite from pygame"""

    def __init__(self, color, width, height):
        # call the constructor parent class Sprite
        super().__init__()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Достать прямоугольный объект, обладающий размерами картинки
        # Обновить позицию этого объекта, задав значения rect.x и rect.y
        self.rect = self.image.get_rect()

    def update(self, *pos):
        # Подвинуть блок на один пиксель вниз
        # self.rect.y += 1
        # if self.rect.y > size[1]:
        #     self.rect.y = random.randrange(-100, -10)
        # self.rect.x = random.randrange(0, size[0])
        # run from player

        if self.rect.x < pos[0][0] + 10 and self.rect.y < pos[0][1]+10:
            self.rect.x -= 10
        # if self.rect.x > (pos[0][0] - 10):
        #     self.rect.x += 10
        # if self.rect.y < (pos[0][1] + 10):
        #     self.rect.y -= 10
        # if self.rect.y > (int(pos[0][1]) - 10):
        #     self.rect.y += 10
        # if self.rect.x > size[0] or self.rect.x < 0:
        #     self.rect.x = self.rect.x*(-1)
        # if self.rect.y > size[1] or self.rect.y < 0:
        #     self.rect.y = self.rect.y*(-1)

