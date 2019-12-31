import pygame
from Classes.Settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, name="1"):
        super().__init__()
        self.image = pygame.image.load(LEVEL_GENERATOR_SPRITES[name])
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)

        self.tag = "Block"
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


class Water(Block):
    def __init__(self, x, y, name="Water"):
        super().__init__(x, y, name)
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.tag = "Water"
        self.use = False


class WaterKill(Block):
    def __init__(self, x, y, name="WaterKill"):
        super().__init__(x, y, name)
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.tag = "WaterKill"
        self.use = False


class Spikes(Block):
    def __init__(self, x, y, name="Spikes"):
        super().__init__(x, y, name)
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.tag = "Spikes"
        self.use = False
