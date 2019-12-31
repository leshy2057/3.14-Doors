import requests, threading, time, json, random, pygame, sys
from Classes.Player import Player
from Classes.Block import *
from Classes.Camera import *
from Classes.Settings import *
from Classes.UI.Button import Button
from  Classes.UI.Slider import Slider
from Classes.UI.Background import Background
from Classes.UI.Image import Image
from Classes.UI.Panel import Panel
from Classes.UI.Text import Text
from Classes.Settings import *


class Menus:
    currentStage = "Menu"
    currentLevel = ""

    class Menu:
        def __init__(self, surface):
            self.surface = surface

            self.BackGround = Background()
            self.buttonStart = Button(200, 20, 300, 70,spriteName="D1_Button",  name="Start", text="Start", fontSize=60, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=self.ToLevelSelector)
            self.buttonSettings = Button(200, 110, 300, 70, name="Settings", text="Settings", fontSize=60, color=(0, 230, 230), onColor=(0, 200, 200), pressColor=(0, 150, 150), func=self.ToLevelSettings)
            self.buttonUpgrade = Button(200, 220, 300, 70, name="Upgrade", text="Upgrade", fontSize=60, color=(0, 230, 230), onColor=(0, 200, 200), pressColor=(0, 150, 150), func=self.ToLevelUpgrade)
            self.buttonExit = Button(200, 310, 300, 70, name="Exit", text="Exit", fontSize=60, color=(230, 0, 0), onColor=(200, 0, 0), pressColor=(150, 0, 0), func=self.Exit)

        def ToLevelSelector(self):
            Menus.currentStage = "Level Selector"
            time.sleep(PAUSE_TO_LOAD)

        def ToLevelSettings(self):
            Menus.currentStage = "Settings"
            time.sleep(PAUSE_TO_LOAD)

        def ToLevelUpgrade(self):
            Menus.currentStage = "Upgrade"
            time.sleep(PAUSE_TO_LOAD)

        def Exit(self):
            SavesManager.SaveGame(SavesManager)
            sys.exit()

        def Update(self, windows):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    SavesManager.SaveGame(SavesManager)
                    sys.exit()

            # self.surface.fill((255, 255, 255))
            self.surface.blit(self.BackGround.image, self.BackGround.rect)
            self.buttonStart.Update(self.surface)
            self.buttonSettings.Update(self.surface)
            self.buttonUpgrade.Update(self.surface)
            self.buttonExit.Update(self.surface)
            windows.blit(self.surface, (0, 0))


    class Settings:
        def __init__(self, surface):
            self.surface = surface

            self.BackGround = Background()

            self.sliderVolume = Slider(text="Volume", x=150, y=20, w=400, h=100, out_x=20)
            self.buttonMenu = Button(x=150, y=280, w=400, h=100, name="Menu", text="Menu", color=(0, 230, 230), onColor=(0, 200, 200), pressColor=(0, 150, 150), fontSize=25, func=self.ToMenu)

            self.languages_button = [
                Button(x=150, y=140, w=180, h=100, name="Ru", text="Russian", color=(0, 230, 230), onColor=(0, 200, 200), pressColor=(0, 150, 150), fontSize=25, func=lambda: self.ChangeLanguage("ru")),
                Button(x=370, y=140, w=180, h=100, name="En", text="English", color=(0, 230, 230), onColor=(0, 200, 200), pressColor=(0, 150, 150), fontSize=25, func=lambda: self.ChangeLanguage("en")),
            ]

        def ToMenu(self):
            Menus.currentStage = "Menu"
            time.sleep(PAUSE_TO_LOAD)

        def ChangeLanguage(self, name):
            SavesManager.save["settings"]["language"] = name
            SavesManager.ChangeLanguage(SavesManager)

        def ChangeVolume(self, volume):
            SavesManager.save["settings"]["volume"] = volume
            SavesManager.ChangeVolume(SavesManager)


        def Update(self, windows):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    SavesManager.SaveGame(SavesManager)
                    sys.exit()

            # self.surface.fill((255, 255, 255))
            self.surface.blit(self.BackGround.image, self.BackGround.rect)
            self.sliderVolume.Update(self.surface)
            self.ChangeVolume(self.sliderVolume.value)
            self.buttonMenu.Update(self.surface)

            for button in self.languages_button:
                button.Update(self.surface)

            windows.blit(self.surface, (0, 0))


    class Upgrade:
        def __init__(self, surface):
            self.surface = surface

            self.BackGround = Background()

            self.u_speedPanel = Panel(x=20, y=0, w=230, h=310, color=(220, 220, 220, 150))
            self.u_speedImage = Image(x=50, y=20, w=160, h=220)
            self.u_speedButton = Button(x=20, y=240, w=230, h=70, name="Speed", text="Speed", color=(0, 230, 230), onColor=(0, 200, 200), pressColor=(0, 150, 150), fontSize=25, func=lambda: self.UpgradeStat("speed_level"))

            self.u_jumpPanel = Panel(x=450, y=0, w=230, h=310, color=(220, 220, 220, 150))
            self.u_jumpImage = Image(x=490, y=20, w=160, h=220, name="U_Jump")
            self.u_jumpButton =  Button(x=450, y=240, w=230, h=70, name="Jump", text="Jump", color=(0, 230, 230), onColor=(0, 200, 200), pressColor=(0, 150, 150), fontSize=25, func=lambda: self.UpgradeStat("jump_level"))


            self.buttonMenu = Button(x=150, y=330, w=400, h=50, name="Menu", text="Menu", color=(0, 230, 230), onColor=(0, 200, 200), pressColor=(0, 150, 150), fontSize=25, func=self.ToMenu)


        def ToMenu(self):
            Menus.currentStage = "Menu"
            time.sleep(PAUSE_TO_LOAD)

        def UpgradeStat(self, name):
            # print(SavesManager.save["player"][name] + 1,  PLAYER_SPEED_LEVELS.keys())
            if (name == "jump_level"):
                if (SavesManager.save["player"][name] + 1 in PLAYER_SPEED_LEVELS.keys()):
                    if (SavesManager.save["player"]["moneys"] >= PLAYER_SPEED_LEVELS[SavesManager.save["player"][name] + 1]["price"]):
                        SavesManager.save["player"]["moneys"] -= PLAYER_SPEED_LEVELS[SavesManager.save["player"][name] + 1]["price"]
                        SavesManager.save["player"][name] += 1
                    else:
                        print("You don't have moneys!")
            elif (name == "speed_level"):
                if (SavesManager.save["player"][name] + 1 in PLAYER_JUMP_FORCE_LEVELS.keys()):
                    if (SavesManager.save["player"]["moneys"] >= PLAYER_JUMP_FORCE_LEVELS[SavesManager.save["player"][name] + 1]["price"]):
                        SavesManager.save["player"]["moneys"] -= PLAYER_JUMP_FORCE_LEVELS[SavesManager.save["player"][name] + 1]["price"]
                        SavesManager.save["player"][name] += 1
                    else:
                        print("You don't have moneys!")
            SavesManager.UpgradeStats(SavesManager)



        def Update(self, windows):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    SavesManager.SaveGame(SavesManager)
                    sys.exit()

            # self.surface.fill((255, 255, 255))
            self.surface.blit(self.BackGround.image, self.BackGround.rect)

            self.surface.blit(self.u_speedPanel.image, self.u_speedPanel.rect)
            self.surface.blit(self.u_speedImage.image, self.u_speedImage.rect)
            self.u_speedButton.Update(self.surface)

            self.surface.blit(self.u_jumpPanel.image, self.u_jumpPanel.rect)
            self.surface.blit(self.u_jumpImage.image, self.u_jumpImage.rect)
            self.u_jumpButton.Update(self.surface)

            self.buttonMenu.Update(self.surface)

            #for button in self.languages_button:
                #button.Update(self.surface)

            windows.blit(self.surface, (0, 0))


    class LevelSelector:
        def __init__(self, surface):
            self.surface = surface

            self.BackGround = Background()

            self.buttonMenu = Button(x=650, y=0, w=50, h=50, name="Menu", text="Menu", color=(230, 0, 0), onColor=(200, 0, 0), pressColor=(150, 0, 0), fontSize=25, func=self.ToMenu)
            self.levelButtons = [
                Button(x=0, y=0, w=100, h=100, text="1", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=lambda: self.ToGame("level_1")),
                Button(x=100, y=0, w=100, h=100, text="2", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=lambda: self.ToGame("level_2")),
                Button(x=200, y=0, w=100, h=100, text="3", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=lambda: self.ToGame("level_3")),
            ]

        def ToGame(self, level_name):
            if (SavesManager.save["levels"][level_name]["open"]):
                Menus.currentStage = "Game"
                Menus.currentLevel = level_name
                time.sleep(PAUSE_TO_LOAD)
        
        def ToMenu(self):
            Menus.currentStage = "Menu"
            time.sleep(PAUSE_TO_LOAD)

        def Update(self, windows):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    SavesManager.SaveGame(SavesManager)
                    sys.exit()

            # self.surface.fill((255, 255, 255))
            self.surface.blit(self.BackGround.image, self.BackGround.rect)

            for i in self.levelButtons:
                i.Update(self.surface)

            self.buttonMenu.Update(self.surface)
            windows.blit(self.surface, (0, 0))



    class Game:
        def __init__(self, surface):
            self.surface = surface

            self.BackGround = Background()
            self.DieText = Text(text="DIE! Press R to restart!", w=WIN_WIDTH, h=WIN_HEIGHT, color=(255, 255, 255, 1), fontSize=90)
            self.level_name = Menus.currentLevel

            self.on_level_collect = 0

            self.map = []
            self.player = Player()

            self.blocks = pygame.sprite.Group()
            self.wallList = pygame.sprite.Group()
            self.prefabs = []
            self.reload = False

            self.sound = pygame.mixer.Sound(SOUNDS_GAME["W1_Music"])
            self.sound.set_volume(SavesManager.AUDIO_VOLUME)

            self.sound.play(loops=10000)

            self.camera = None

            self.buttonMenu = Button(x=650, y=0, w=50, h=50, name="LS", text="LS", color=(230, 0, 0), onColor=(200, 0, 0), pressColor=(150, 0, 0), fontSize=25, func=self.ToLevelSelector)

            self.GenerateLevel()

        def ToLevelSelector(self):
            self.sound.stop()
            Menus.currentStage = "Level Selector"
            Menus.currentLevel = ""
            time.sleep(PAUSE_TO_LOAD)

        def OpenNextLevel(self):
            SavesManager.save["levels"][self.levels_list[Menus.currentLevel]]["open"] = True

        def GenerateLevel(self):
            try:
                with open("Levels\\levels.json", "r") as levels:
                    data = json.load(levels)
                    self.level = data[self.level_name]
                    self.levels_list = data["levels_list"]
            except:
                raise Exception("Level not found in json!")
            typeWorld = self.level["type"]
            self.level = self.level["map"]

            self.BackGround = Background(typeWorld=typeWorld)

            x, y, step = 0, 0, 32
            level_for = ""
            for i in self.level: level_for += i
            for symbol in level_for:
                if (symbol in LEVEL_GENERATOR_SPRITES[typeWorld].keys()):
                    block = Block(x, y, symbol, typeWorld=typeWorld)
                    self.blocks.add_internal(block)
                    self.wallList.add_internal(block)
                    x += step
                elif (symbol == "C"):
                    coin = Coin(x, y, typeWorld=typeWorld)
                    self.blocks.add_internal(coin)
                    self.wallList.add_internal(coin)
                    x += step
                elif (symbol == "D"):
                    door = Door(x, y, typeWorld=typeWorld)
                    self.blocks.add_internal(door)
                    self.wallList.add_internal(door)
                    x += step
                elif (symbol == "K"):
                    key = Key(x, y, typeWorld=typeWorld)
                    self.blocks.add_internal(key)
                    self.wallList.add_internal(key)
                    x += step
                elif (symbol == "W"):
                    water = Water(x, y, typeWorld=typeWorld)
                    self.blocks.add_internal(water)
                    self.wallList.add_internal(water)
                    x += step
                elif (symbol == "V"):
                    waterKill = WaterKill(x, y, typeWorld=typeWorld)
                    self.blocks.add_internal(waterKill)
                    self.wallList.add_internal(waterKill)
                    x += step
                elif (symbol == "S"):
                    spikes = Spikes(x, y, typeWorld=typeWorld)
                    self.blocks.add_internal(spikes)
                    self.wallList.add_internal(spikes)
                    x += step
                elif (symbol == "P"):
                    self.player.rect.topleft = (x, y)
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
                    SavesManager.SaveGame(SavesManager)
                    sys.exit()

                if (event.type == pygame.KEYDOWN):
                    if (self.player.die and event.key == pygame.K_r):
                        self.sound.stop()
                        self.reload = True

            if (not self.player.die):
                self.sound.set_volume(SavesManager.AUDIO_VOLUME)

                self.player.Move(pygame.key.get_pressed())
                self.player.update()
                # self.surface.fill((255, 255, 255))
                self.surface.blit(self.BackGround.image, self.BackGround.rect)

                self.camera.update(self.player)

                for i in self.blocks:
                    if (not i.use):
                        self.surface.blit(i.image, self.camera.apply(i))

            else:
                self.DieText.Update(self.surface)

            self.buttonMenu.Update(self.surface)

            if (self.player.inDoor):
                SavesManager.ApeendMoneys(SavesManager, self.player.on_level_collect)
                self.OpenNextLevel()
                SavesManager.SaveGame(SavesManager)
                self.ToLevelSelector()

            windows.blit(self.surface, (0, 0))
