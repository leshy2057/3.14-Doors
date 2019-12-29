import pygame
from Classes.Settings import *


class Button(object):
    def __init__(self, x=0, y=0, w=100, h=100, name=None, text="Text", fontSize=20, color=(255, 0, 0), onColor=(200, 0, 0), pressColor=(150, 0, 0), func=None):
        self.normalColor = color
        self.onColor = onColor
        self.pressColor = pressColor

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name

        self.font = pygame.font.Font(None, fontSize)

        self.text = text
        if (self.name and LANGUAGE in LANGUAGE_FILE):
            self.text = LANGUAGE_FILE[LANGUAGE][name]
        self.event = func

    def Update(self, screen):
        if (not self.OnButton()):
            bg = self.normalColor
        elif (self.OnButton() and bool(pygame.mouse.get_pressed()[0])):
            bg = self.pressColor
            if (self.event): self.event()
        else:
            bg = self.onColor

        surf = self.font.render(self.text, True, (0, 0, 0), bg)
        rect = (self.x, self.y, self.w, self.h)
        xo = self.x + (self.w - surf.get_width()) // 2
        yo = self.y + (self.h - surf.get_height()) // 2
        screen.fill(bg, rect)
        screen.blit(surf, (xo, yo))

    def OnButton(self):
        pos = pygame.mouse.get_pos()
        return self.x <= pos[0] and self.x + self.w > pos[0] and self.y <= pos[1] and self.y + self.h > pos[1]