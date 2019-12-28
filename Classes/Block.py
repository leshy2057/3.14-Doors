import pygame
from Classes.Settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("Images/ground_1.png")
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)

        self.tag = 'Block'
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
