import pygame
from Classes.Settings import *


class Image(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, h=100, w=100, name="U_Speed"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMAGES[name])
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (x, y)
