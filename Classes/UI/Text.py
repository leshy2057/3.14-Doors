import pygame
from Classes.Settings import SavesManager


class Text:
    def __init__(self, x=0, y=0, w=100, h=100, name=None, text="Text", fontSize=20, color=(255, 255, 255), fontColor=(255, 0, 0)):
        self.normalColor = color
        self.fontColor = fontColor

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name

        self.font = pygame.font.Font(None, fontSize)

        self.text = text
        if (self.name and SavesManager.LANGUAGE in SavesManager.LANGUAGE_FILE):
            self.text = SavesManager.LANGUAGE_FILE[SavesManager.LANGUAGE][name]

    def Update(self, screen):
        if (self.name and SavesManager.LANGUAGE in SavesManager.LANGUAGE_FILE):
            self.text = SavesManager.LANGUAGE_FILE[SavesManager.LANGUAGE][self.name]

        surf = self.font.render(self.text, True, self.fontColor, self.normalColor)
        rect = (self.x, self.y, self.w, self.h)
        xo = self.x + (self.w - surf.get_width()) // 2
        yo = self.y + (self.h - surf.get_height()) // 2
        screen.fill(self.normalColor, rect)
        screen.blit(surf, (xo, yo))