import requests, threading, time, json, random, pygame, sys
from Classes.Levels import Menus
from Classes.Settings import *


pygame.init()
clock = pygame.time.Clock()
windows = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Test")

surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))

GAME = Menus.Game(surface)
runGame = True

pygame.key.set_repeat(1, 10)
while runGame:
    GAME.Update(windows, runGame)
    clock.tick(30)
    pygame.display.flip()


pygame.quit()