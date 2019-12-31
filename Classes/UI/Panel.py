import pygame


class Panel(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, h=100, w=100, color=(220, 220, 220, 220)):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (x, y)


