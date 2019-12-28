import requests, threading, time, json, random, pygame, sys
from Classes.Player import Player
from Classes.Block import Block
from Classes.Camera import *
from Classes.Settings import *
from Classes.UI.Button import Button
from Classes.Settings import *


class Menus:
    currentStage = "Menu"
    currentLevel = ""


    class Menu:
        def __init__(self, surface):
            self.surface = surface
            self.buttonStart = Button(200, 40, 300, 100, text="Start", fontSize=60, color=(0, 230, 0), onColor=(0, 200, 0), pressColor=(0, 150, 0), func=self.ToLevelSelector)
            self.buttonExit = Button(200, 220, 300, 100, text="Exit", fontSize=60, color=(230, 0, 0), onColor=(200, 0, 0), pressColor=(150, 0, 0), func=self.Exit)

        def ToLevelSelector(self):
            Menus.currentStage = "Level Selector"
            time.sleep(PAUSE_TO_LOAD)

        def Exit(self):
            sys.exit()

        def Update(self, windows):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.surface.fill((255, 255, 255))
            self.buttonStart.Update(self.surface)
            self.buttonExit.Update(self.surface)
            windows.blit(self.surface, (0, 0))



    class LevelSelector:
        def __init__(self, surface):
            self.surface = surface

            self.buttonMenu = Button(x=650, y=0, w=50, h=50, text="Menu", color=(230, 0, 0), onColor=(200, 0, 0), pressColor=(150, 0, 0), fontSize=25, func=self.ToMenu)
            self.levelButtons = [
                Button(x=0, y=0, w=100, h=100, text="1", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=lambda: self.ToGame("level_1")),
                Button(x=100, y=0, w=100, h=100, text="2", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=lambda: self.ToGame("level_2")),
                Button(x=200, y=0, w=100, h=100, text="3", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=lambda: self.ToGame("level_3"))
            ]

        def ToGame(self, level_name):
            Menus.currentStage = "Game"
            Menus.currentLevel = level_name
            time.sleep(PAUSE_TO_LOAD)
        
        def ToMenu(self):
            Menus.currentStage = "Menu"
            time.sleep(PAUSE_TO_LOAD)

        def Update(self, windows):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.surface.fill((255, 255, 255))

            for i in self.levelButtons:
                i.Update(self.surface)

            self.buttonMenu.Update(self.surface)
            windows.blit(self.surface, (0, 0))



    class Game:
        def __init__(self, surface):
            self.surface = surface
            self.level_name = Menus.currentLevel

            self.map = []
            self.player = Player()

            self.blocks = pygame.sprite.Group()
            self.wallList = pygame.sprite.Group()
            self.platforms = []

            self.camera = None

            self.buttonMenu = Button(x=650, y=0, w=50, h=50, text="LS", color=(230, 0, 0), onColor=(200, 0, 0), pressColor=(150, 0, 0), fontSize=25, func=self.ToLevelSelector)

            self.GenerateLevel()

        def ToLevelSelector(self):
            Menus.currentStage = "Level Selector"
            Menus.currentLevel = ""
            time.sleep(PAUSE_TO_LOAD)

        def GenerateLevel(self):
            try:
                with open("Levels\\levels.json", "r") as levels:
                    self.level = json.load(levels)[self.level_name]
            except:
                raise Exception("Level not found in json!")

            
            x, y, step = 0, 0, 32
            level_for = ""
            for i in self.level: level_for += i
            for symbol in level_for:
                if (symbol == "-"):
                    block = Block(x, y)
                    self.blocks.add_internal(block)
                    self.wallList.add_internal(block)
                    x += step
                elif (symbol == "|"):
                    x = 0
                    y += step
                else:
                    x += step
            self.blocks.add_internal(self.player)
            self.player.walls = self.wallList


            total_level_width = len(self.level[0]) * BLOCK_SIZE[0]  # Высчитываем фактическую ширину уровня
            total_level_height = len(self.level) * BLOCK_SIZE[1]  # высоту
            self.camera = Camera(camera_configure, total_level_width, total_level_height)
        
        def Update(self, windows):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.player.Move(pygame.key.get_pressed())
            self.player.update()
            self.surface.fill((255, 255, 255))

            self.camera.update(self.player)

            for i in self.blocks:
                self.surface.blit(i.image, self.camera.apply(i))

            self.buttonMenu.Update(self.surface)
    
            windows.blit(self.surface, (0, 0))
