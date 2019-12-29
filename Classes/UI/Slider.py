import pygame, math
from Classes.Settings import *


class Slider():
    def __init__(self, x=100, y=20, w=300, h=50, out_x=10, backgroundSliderH=10, sliderW=10, sliderH=20, value=0, minValue=0, maxValue=1, text="Text", fontSize=20, color=(200, 200, 200), sliderColor=(200, 0, 0), sliderBackgroundColor=(100, 100, 100)):
        self.normalColor = color
        self.sliderColor = sliderColor
        self.sliderBackgroundColor = sliderBackgroundColor

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.out_x = out_x

        self.value = SavesManager.AUDIO_VOLUME
        self.minValue = minValue
        self.maxValue = maxValue

        self.font = pygame.font.Font(None, fontSize)

        self.backgroundSlider = pygame.surface.Surface((w - 2 * self.out_x, backgroundSliderH))
        self.slider = pygame.surface.Surface((10, 20))

        self.sliderY = 0
        self.sliderW = sliderW
        self.sliderH = sliderH
        self.sliderX = (self.value - self.minValue)*(self.w - 2 * self.out_x - self.sliderW) / (self.maxValue - self.minValue) + 2*self.out_x + self.x - self.sliderW

        self.text = text


    def Update(self, screen):
        use = self.OnSlider() and pygame.mouse.get_pressed()[0]
        if (use):
            self.sliderX = pygame.mouse.get_pos()[0]
            if (self.sliderX + self.sliderW >= self.x - self.out_x + 1 + self.w):
                self.sliderX = self.w + self.x - self.sliderW - self.out_x + 1
            elif (self.sliderX <= self.x + self.out_x - 1):
                self.sliderX = self.x + self.out_x - 1


        self.value = (self.sliderX + self.sliderW - self.x - 2 * self.out_x) / (self.w - 2 * self.out_x - self.sliderW) * (self.maxValue - self.minValue) + self.minValue

        if (self.value < self.minValue + 0.1): self.value = self.minValue
        if (self.value > self.maxValue): self.value = self.maxValue

        surf = self.font.render(f"{self.text}: %.1f" % self.value, True, (0, 0, 0), self.normalColor)
        rect = (self.x, self.y, self.w, self.h)
        self.backgroundSlider.fill(self.sliderBackgroundColor)

        screen.fill(self.normalColor, rect)
        screen.blit(surf, (self.x, self.y))

        yo_S = self.y + (self.h - surf.get_height()) // 2
        yo_B = self.y + (self.h - surf.get_height() + self.backgroundSlider.get_height()) // 2

        self.sliderY = yo_S

        screen.blit(self.backgroundSlider, (self.out_x + self.x, yo_B))
        screen.blit(self.slider, (self.sliderX, yo_S))


    def OnSlider(self):
        pos = pygame.mouse.get_pos()
        return self.x <= pos[0] and self.x + self.w > pos[0] and self.y <= pos[1] and self.y + self.h > pos[1]

    def GetValue(self):
        return self.value

