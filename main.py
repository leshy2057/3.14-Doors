import requests, threading, time, json, random, pygame, sys
from Classes.Levels import Menus
from Classes.Settings import *


pygame.init()
clock = pygame.time.Clock()
windows = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Test")

surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))

MENU = Menus.Menu(surface)
LEVEL_SELECTOR = Menus.LevelSelector(surface)
SETTINGS = Menus.Settings(surface)
UPGRADE = Menus.Upgrade(surface)
MENU_BETWEEN = Menus.MenuBetweenLevelCreator(surface)
GAME = None
LEVEL_CREATOR = None

runGame = True

pygame.key.set_repeat(1, 10)
while runGame:
    windows.fill([255, 255, 255])
    if (Menus.currentStage == "Menu"):
        MENU.Update(windows)
        if (GAME):
            GAME = None
        if (LEVEL_CREATOR):
            LEVEL_CREATOR = None
    elif (Menus.currentStage == "Level Selector"):
        LEVEL_SELECTOR.Update(windows)
        if (GAME):
            GAME = None
        if (LEVEL_CREATOR):
            LEVEL_CREATOR = None
    elif (Menus.currentStage == "Settings"):
        SETTINGS.Update(windows)
    elif (Menus.currentStage == "Upgrade"):
        UPGRADE.Update(windows)
    elif (Menus.currentStage == "Game"):
        if (not GAME):
            GAME = Menus.Game(windows)
        elif (GAME.reload):
            GAME = Menus.Game(windows)
        GAME.Update(windows)
    elif (Menus.currentStage == "MenuB"):
        MENU_BETWEEN.Update(windows)
        if (LEVEL_CREATOR):
            LEVEL_CREATOR = None
    elif (Menus.currentStage == "Level Creator"):
        if (not LEVEL_CREATOR):
            LEVEL_CREATOR = Menus.LevelCreator(windows)
        LEVEL_CREATOR.Update(windows)

    clock.tick(30)
    pygame.display.flip()


pygame.quit()