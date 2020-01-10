import time, sys
from Classes.Player import Player
from Classes.Settings import *
from Classes.UI.Slider import Slider
from Classes.UI.Background import Background
from Classes.UI.Image import Image
from Classes.UI.Panel import Panel
from Classes.UI.Text import Text
from Classes.UI.Button import Button
from Classes.Camera import Camera
from Classes.Block import *

from Classes.Editor.Settings import *
from Classes.Editor.Pointer import *
from Classes.Editor.Camera import *
from Classes.Editor.Block import *
from Classes.Editor.Tools import *
from Classes.Editor.UI.Button import *


class Menus:
    currentStage = "Menu"
    currentLevel = ""

    class Menu:
        def __init__(self, surface):
            self.surface = surface

            self.BackGround = Background()
            self.buttonStart = Button(200, 5, 300, 70,spriteName="D1_Button",  name="Start", text="Start", fontSize=60, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=self.ToLevelSelector)
            self.buttonSettings = Button(200, 85, 300, 70,spriteName="D1_Button", name="Settings", text="Settings", fontSize=60, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=self.ToLevelSettings)
            self.buttonUpgrade = Button(200, 165, 300, 70,spriteName="D1_Button", name="Upgrade", text="Upgrade", fontSize=60, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=self.ToLevelUpgrade)
            self.buttonCreator = Button(200, 245, 300, 70,spriteName="D1_Button", name="Level Creator", text="Level Creator", fontSize=60, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=self.ToLevelCreator)
            self.buttonExit = Button(200, 325, 300, 70,spriteName="D1_Button", name="Exit", text="Exit", fontSize=60, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=self.Exit)

        def ToLevelSelector(self):
            Menus.currentStage = "Level Selector"
            time.sleep(PAUSE_TO_LOAD)

        def ToLevelSettings(self):
            Menus.currentStage = "Settings"
            time.sleep(PAUSE_TO_LOAD)

        def ToLevelUpgrade(self):
            Menus.currentStage = "Upgrade"
            time.sleep(PAUSE_TO_LOAD)

        def ToLevelCreator(self):
            Menus.currentStage = "MenuB"
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
            self.buttonCreator.Update(self.surface)
            self.buttonExit.Update(self.surface)
            windows.blit(self.surface, (0, 0))


    class Settings:
        def __init__(self, surface):
            self.surface = surface

            self.BackGround = Background()

            self.sliderVolume = Slider(text="Volume", x=150, y=20, w=400, h=100, out_x=20)
            self.buttonMenu = Button(x=150, y=280, w=400, h=100, spriteName="D1_Button", name="Menu", text="Menu", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), fontSize=25, func=self.ToMenu)

            self.languages_button = [
                Button(x=150, y=140, w=180, h=100, spriteName="Ru", name=None, text=None, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), fontSize=25, func=lambda: self.ChangeLanguage("ru")),
                Button(x=370, y=140, w=180, h=100, spriteName="Eng", name=None, text=None, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), fontSize=25, func=lambda: self.ChangeLanguage("en")),
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
            self.u_speedButton = Button(x=20, y=240, w=230, h=70, spriteName="D1_Button", name="Speed", text="Speed", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), fontSize=25, func=lambda: self.UpgradeStat("speed_level"))

            self.u_jumpPanel = Panel(x=450, y=0, w=230, h=310, color=(220, 220, 220, 150))
            self.u_jumpImage = Image(x=490, y=20, w=160, h=220, name="U_Jump")
            self.u_jumpButton =  Button(x=450, y=240, w=230, h=70, spriteName="D1_Button", name="Jump", text="Jump", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), fontSize=25, func=lambda: self.UpgradeStat("jump_level"))

            self.u_coinPanel = Panel(x=270, y=0, w=160, h=310, color=(220, 220, 220, 150))
            self.u_coinImage = Image(x=270, y=20, w=160, h=184, name="U_Coin")
            self.u_coinText = Text(x=270, y=240, w=160, h=70, text="100", fontSize=30)

            self.buttonMenu = Button(x=150, y=330, w=400, h=50, spriteName="D1_Button", name="Menu", text="Menu", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), fontSize=25, func=self.ToMenu)


        def ToMenu(self):
            Menus.currentStage = "Menu"
            time.sleep(PAUSE_TO_LOAD)

        def UpgradeStat(self, name):
            # print(SavesManager.save["player"][name] + 1,  PLAYER_SPEED_LEVELS.keys())
            if (name == "speed_level"):
                if (SavesManager.save["player"][name] + 1 in PLAYER_SPEED_LEVELS.keys()):
                    if (SavesManager.save["player"]["moneys"] >= PLAYER_SPEED_LEVELS[SavesManager.save["player"][name] + 1]["price"]):
                        SavesManager.save["player"]["moneys"] -= PLAYER_SPEED_LEVELS[SavesManager.save["player"][name] + 1]["price"]
                        SavesManager.save["player"][name] += 1
                    else:
                        print("You don't have moneys!")
            elif (name == "jump_level"):
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

            self.u_coinText.text = f"{SavesManager.save['player']['moneys']}"

            # self.surface.fill((255, 255, 255))
            self.surface.blit(self.BackGround.image, self.BackGround.rect)

            textSpeed = "Max"
            textJump = "Max"

            if (SavesManager.save["player"]["speed_level"] + 1 in PLAYER_SPEED_LEVELS.keys()):
                textSpeed = f': {PLAYER_SPEED_LEVELS[SavesManager.save["player"]["speed_level"] + 1]["price"]}'

            if (SavesManager.save["player"]["jump_level"] + 1 in PLAYER_JUMP_FORCE_LEVELS.keys()):
                textJump = f': {PLAYER_JUMP_FORCE_LEVELS[SavesManager.save["player"]["jump_level"] + 1]["price"]}'

            self.surface.blit(self.u_speedPanel.image, self.u_speedPanel.rect)
            self.surface.blit(self.u_speedImage.image, self.u_speedImage.rect)
            self.u_speedButton.Update(self.surface, textSpeed)

            self.surface.blit(self.u_jumpPanel.image, self.u_jumpPanel.rect)
            self.surface.blit(self.u_jumpImage.image, self.u_jumpImage.rect)
            self.u_jumpButton.Update(self.surface, textJump)

            self.surface.blit(self.u_coinPanel.image, self.u_coinPanel.rect)
            self.surface.blit(self.u_coinImage.image, self.u_coinImage.rect)
            self.u_coinText.Update(self.surface)

            self.buttonMenu.Update(self.surface)

            #for button in self.languages_button:
                #button.Update(self.surface)

            windows.blit(self.surface, (0, 0))


    class MenuBetweenLevelCreator:
        def __init__(self, surface):
            self.surface = surface

            self.BackGround = Background()
            self.buttonMenu = Button(200, 210, 300, 70,spriteName="D1_Button", name="Menu", text="Menu", fontSize=60, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=self.ToMenu)

            self.worldButtons = [
                Button(200, 20, 300, 70,spriteName="D1_Button", name=None, text="World_1", fontSize=60, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=lambda: self.ChangeWorldType("World_1")),
                Button(200, 110, 300, 70,spriteName="D1_Button", name=None, text="World_2", fontSize=60, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=lambda: self.ChangeWorldType("World_2"))
            ]


        def ToMenu(self):
            Menus.currentStage = "Menu"
            time.sleep(PAUSE_TO_LOAD)

        def ChangeWorldType(self, typeOfWorld="World_1"):
            DynamicSettings.WORLD_TYPE = typeOfWorld
            Menus.currentStage = "Level Creator"
            time.sleep(PAUSE_TO_LOAD)

        def Update(self, windows):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    SavesManager.SaveGame(SavesManager)
                    sys.exit()

            self.surface.fill(BACKGROUND_COLOR)
            self.surface.blit(self.BackGround.image, self.BackGround.rect)

            for button in self.worldButtons:
                button.Update(self.surface)

            self.buttonMenu.Update(self.surface)

            windows.blit(self.surface, (0, 0))



    class LevelCreator:
        def __init__(self, surface):
            self.surface = surface

            self.mapEditorSurface = pygame.Surface((DRAW_WIDTH, DRAW_HEIGHT))

            self.POINTER = Pointer()
            self.CAMERA = CameraLevelCreator(camera_configure, TOTAL_WIDTH, TOTAL_HEIGHT)

            self.buttons = [
                Button(x=600, y=000, text=None, spriteName="Paint", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=lambda: Tools.ChangeTool(Tools, "Paint")),
                Button(x=600, y=100, text=None, spriteName="Earse", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=lambda: Tools.ChangeTool(Tools, "Earse")),
                Button(x=600, y=200, text=None, spriteName="Back", color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=self.ToMenu)
            ]

            self.matrix = []
            x, y, step = 0, 0, 32

            for i in range(COUNT_HEIGHT):
                for j in range(COUNT_WIDTH):
                    self.matrix.append(EmptyBlock(x, y))
                    x += step
                y += step
                x = 0

            self.pallete = []
            x, y, step = 0, DRAW_HEIGHT, 50

            self.pallete_names = [i.rsplit(".", 1)[0] for i in os.listdir(f"{os.getcwd()}\\Images\\Blocks\\{DynamicSettings.WORLD_TYPE}")]
            count = 0

            for i in range(2):
                for j in range(12):
                    self.pallete.append(TileBlock(x, y, name=self.pallete_names[count] if count < len(self.pallete_names) else "EmptyBlock"))
                    count += 1
                    x += step
                y += step
                x = 0

        def ToMenu(self):
            Menus.currentStage = "MenuB"
            time.sleep(PAUSE_TO_LOAD)

        def GenrateLevel(self):
            level = {"map": None, "type": DynamicSettings.WORLD_TYPE}

            map = []

            line = ""
            for block in self.matrix:
                if (len(line) < COUNT_WIDTH - 1):
                    line += block.name if (block.name != "EmptyBlock") else " "
                else:
                    line += block.name if (block.name != "EmptyBlock") else " "
                    line += "|"
                    map.append(line)
                    line = ""

            level["map"] = map

            self.level_names = [i.rsplit(".", 1)[0] for i in os.listdir(f"{os.getcwd()}\\Levels")]
            next_num = int(self.level_names[-1].rsplit("_")[-1]) + 1

            with open(f"Levels\\level_{next_num}.json", "w", encoding="utf-8") as file:
                file.write(json.dumps(level))


        def Update(self, windows):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    SavesManager.SaveGame(SavesManager)
                    sys.exit()

                elif (event.type == pygame.KEYUP):
                    if (event.key == pygame.K_F5):
                        self.GenrateLevel()

            self.mapEditorSurface.fill(BACKGROUND_COLOR)

            self.POINTER.Move(pygame.key.get_pressed())

            for block in self.matrix:
                block.Update()
                self.CAMERA.apply(block)
                self.mapEditorSurface.blit(block.image, block.rectTwo)

            for button in self.buttons:
                button.Update(self.surface)

            for tile in self.pallete:
                tile.Update()
                windows.blit(tile.image, tile.rect)

            self.POINTER.Update(self.mapEditorSurface)
            self.CAMERA.update(self.POINTER)

            self.surface.blit(self.mapEditorSurface, (0, 0))
            windows.blit(self.surface, (0, 0))


    class LevelSelector:
        def __init__(self, surface):
            self.surface = surface

            self.BackGround = Background()

            self.buttonMenu = Button(x=650, y=0, w=50, h=50, spriteName="Back", name=None, text=None, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), fontSize=25, func=self.ToMenu)
            self.levelButtons = []
            self.last = []

            self.GenerateButtons()


        def GenerateButtons(self):
            new = os.listdir(f"{os.getcwd()}\\Levels")
            if (new != self.last):
                names = [i.rsplit(".", 1)[0] for i in new]

                x, y, step = (WIN_WIDTH - BUTTON_LEVEL_SELECTOR_SIZE[0]) // 2, (WIN_HEIGHT - BUTTON_LEVEL_SELECTOR_SIZE[1]) // 2, BUTTON_LEVEL_SELECTOR_STEP
                for name in names:
                    self.levelButtons.append(Button(x=x, y=y, w=BUTTON_LEVEL_SELECTOR_SIZE[0], h=BUTTON_LEVEL_SELECTOR_SIZE[1], spriteName="Empty", text=name.rstrip("_")[-1], fontSize=60, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), func=self.ToGame, kwargs={"levelName": name}))
                    x += step

                self.last = new


        def ToGame(self, kwargs):
            if (SavesManager.save["levels"][kwargs["levelName"]]["open"]):
                Menus.currentStage = "Game"
                Menus.currentLevel = kwargs["levelName"]
                time.sleep(PAUSE_TO_LOAD)
        
        def ToMenu(self):
            Menus.currentStage = "Menu"
            time.sleep(PAUSE_TO_LOAD)


        def Update(self, windows):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    SavesManager.SaveGame(SavesManager)
                    sys.exit()

                elif (event.type == pygame.KEYUP):
                    if (event.key == pygame.K_d):
                        if (self.levelButtons[-1].x >= SCROLL_LEVEL_SELECTOR_STEP):
                            for button in self.levelButtons:
                                button.x -= SCROLL_LEVEL_SELECTOR_STEP

                    elif (event.key == pygame.K_a):
                        if (self.levelButtons[0].x <= 0):
                            for button in self.levelButtons:
                                button.x += SCROLL_LEVEL_SELECTOR_STEP

            self.surface.blit(self.BackGround.image, self.BackGround.rect)
            self.GenerateButtons()

            for i in self.levelButtons:
                i.Update(self.surface)

            self.buttonMenu.Update(self.surface)
            windows.blit(self.surface, (0, 0))



    class Game:
        def __init__(self, surface):
            self.surface = surface

            self.BackGround = Background()
            self.DieText = Text(text="DIE! Press R to restart!", name="Die", w=WIN_WIDTH, h=WIN_HEIGHT, color=(30, 30, 30, 1), fontSize=90)
            # self.DieImage = pygame.image.load(PICTURE_AFTER_DIE)
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

            self.toLevelSelectorTimer = 0.3

            self.sound.play(loops=10000)

            self.camera = None

            self.buttonMenu = Button(x=650, y=0, w=50, h=50, spriteName="Back", name=None, text=None, color=(230, 230, 230), onColor=(200, 200, 200), pressColor=(150, 150, 150), fontSize=25, func=self.ToLevelSelector)

            self.GenerateLevel()

        def ToLevelSelector(self):
            self.sound.stop()
            Menus.currentStage = "Level Selector"
            Menus.currentLevel = ""
            time.sleep(PAUSE_TO_LOAD)

        def OpenNextLevel(self):
            if (Menus.currentLevel != list(SavesManager.save["levels"].keys())[-1]):
                SavesManager.save["levels"][list(SavesManager.save["levels"].keys())[list(SavesManager.save["levels"].keys()).index(Menus.currentLevel) + 1]]["open"] = True

        def GenerateLevel(self):
            print(self.level_name)
            try:
                with open(f"Levels\\{self.level_name}.json", "r") as levels:
                    self.level = json.load(levels)
            except:
                raise Exception("Level not found in json!")
            typeWorld = self.level["type"]
            self.level = self.level["map"]

            self.BackGround = Background(typeWorld=typeWorld)

            if (typeWorld == "World_2"):
                self.sound.stop()
                self.sound = pygame.mixer.Sound(SOUNDS_GAME["W2_Music"])
                self.sound.set_volume(SavesManager.AUDIO_VOLUME)
                self.sound.play(loops=10000)

            x, y, step = 0, 0, 32
            level_for = ""
            for i in self.level: level_for += i
            for symbol in level_for:
                if (symbol in LEVEL_GENERATOR_SPRITES[typeWorld].keys() and symbol not in "WVKCDPS|"):
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
                # self.surface.blit(self.DieImage, (0, 0))
                

            self.buttonMenu.Update(self.surface)

            if (self.player.inDoor):
                if (self.toLevelSelectorTimer <= 0):
                    SavesManager.ApeendMoneys(SavesManager, self.player.on_level_collect)
                    self.OpenNextLevel()
                    SavesManager.SaveGame(SavesManager)
                    self.ToLevelSelector()
                self.toLevelSelectorTimer -= (pygame.time.get_ticks() - self.getTicksLastFrame) / 1000.0

            self.getTicksLastFrame = pygame.time.get_ticks()

            windows.blit(self.surface, (0, 0))
