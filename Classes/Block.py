import pygame
from Classes.Settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, name="1"):
        super().__init__()
        self.image = pygame.image.load(LEVEL_GENERATOR_SPRITES[name])
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)

        self.tag = 'Block'
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.use = False


class Coin(Block):
    def __init__(self, x, y, name="Coin"):
        super().__init__(x, y, name)
        self.tag = "Coin"
        self.use = False


class Door(Block):
    def __init__(self, x, y, name="Door_Close"):
        super().__init__(x, y, name)
        self.image = pygame.transform.scale(self.image, DOOR_SIZE)
        self.tag = "Door"
        self.use = False


class Key(Block):
    def __init__(self, x, y, name="Key"):
        super().__init__(x, y, name)
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.tag = "Key"
        self.use = False
