import pygame
from Classes.Settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, type="ground_1"):
        super().__init__()

        self.image = pygame.image.load(f"Images\\Blocks\\{type}.png")
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)

        self.tag = 'Block'
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.use = False


class Coin(Block):
    def __init__(self, x, y, type="Coin"):
        super().__init__(x, y, type)
        self.tag = "Coin"
        self.use = False


class Door(Block):
    def __init__(self, x, y, type="Door_Close"):
        super().__init__(x, y, type)
        self.image = pygame.transform.scale(self.image, DOOR_SIZE)
        self.tag = "Door"
        self.use = False


class Key(Block):
    def __init__(self, x, y, type="Key"):
        super().__init__(x, y, type)
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.tag = "Key"
        self.use = False
