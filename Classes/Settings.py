import json,os
from pygame import image

PLAYER_JUMP_FORCE_LEVELS = {
    1: {"value": 5, "price": 0},
    2: {"value": 6, "price": 10},
    3: {"value": 7, "price": 20},
    4: {"value": 8, "price": 30},
}

PLAYER_SPEED_LEVELS = {
    1: {"value": 4, "price": 0},
    2: {"value": 5, "price": 12},
    3: {"value": 6, "price": 15},
    4: {"value": 7, "price": 20},
}


class SavesManager:
    save = {"player": {"jump_level": 1, "speed_level": 1, "moneys": 0}, "levels": {"level_1": {"open": True}, "level_2": {"open": False}, "level_3": {"open": False}}, "settings": {"language": "en", "volume": 1}}

    LANGUAGE_PATH = "Languages\\languages.json"

    LANGUAGE_FILE = {}
    with open(LANGUAGE_PATH, "r", encoding='utf-8') as language:
        LANGUAGE_FILE = json.load(language)

    LANGUAGE = save["settings"]["language"]
    AUDIO_VOLUME = save["settings"]["volume"]

    PLAYER_JUMP_FORCE = PLAYER_JUMP_FORCE_LEVELS[save["player"]["jump_level"]]["value"]
    PLAYER_SPEED = PLAYER_SPEED_LEVELS[save["player"]["speed_level"]]["value"]

    def LoadGame(self):
        try:
            names = [i.rsplit(".", 1)[0] for i in os.listdir(f"{os.getcwd()}\\Levels")]
            with open("Saves\\save.json", "r") as saves:
                self.save = json.load(saves)
            for name in names:
                if (name not in self.save["levels"].keys()):
                    self.save["levels"][name] = {"open": False}
        except: print("Save file not found! Create new file...")

    def SaveGame(self):
        with open("Saves\\save.json", "w") as saves:
            saves.write(json.dumps(self.save))

    def ApeendMoneys(self, count):
        self.save["player"]["moneys"] += count

    def ChangeLanguage(self):
        self.LANGUAGE = self.save["settings"]["language"]

    def ChangeVolume(self):
        self.AUDIO_VOLUME = self.save["settings"]["volume"]

    def UpgradeStats(self):
        self.PLAYER_JUMP_FORCE = PLAYER_JUMP_FORCE_LEVELS[self.save["player"]["jump_level"]]["value"]
        self.PLAYER_SPEED = PLAYER_SPEED_LEVELS[self.save["player"]["speed_level"]]["value"]


SavesManager.LoadGame(SavesManager)
SavesManager.ChangeLanguage(SavesManager)
SavesManager.ChangeVolume(SavesManager)


PLAYER_SIZE = (32, 48)


GRAVITY = 0.35


BLOCK_SIZE = (32, 32)
DOOR_SIZE = (32, 64)
BUTTON_LEVEL_SELECTOR_SIZE = (150, 150)
BUTTON_LEVEL_SELECTOR_STEP = 300
SCROLL_LEVEL_SELECTOR_STEP = 300

FPS = 30

WIN_WIDTH = 700  # Ширина создаваемого окна
WIN_HEIGHT = 400  # Высота

PAUSE_TO_LOAD = 0.01


ANIMATION_DELAY = 0.1 # скорость смены кадров
ANIMATION_RIGHT = [('Images\\Animations\\Player\\run_r1.png'),
                   ('Images\\Animations\\Player\\run_r2.png'),
                   ('Images\\Animations\\Player\\run_r3.png')]
ANIMATION_LEFT = [('Images\\Animations\\Player\\run_l1.png'),
                  ('Images\\Animations\\Player\\run_l2.png'),
                  ('Images\\Animations\\Player\\run_l3.png')]
ANIMATION_JUMP_LEFT = ['Images\\Animations\\Player\\jump_l.png']
ANIMATION_JUMP_RIGHT = ['Images\\Animations\\Player\\jump_r.png']

ANIMATION_STAY_RIGHT = ['Images\\Animations\\Player\\stay_r.png']
ANIMATION_STAY_LEFT = ['Images\\Animations\\Player\\stay_l.png']

PICTURE_AFTER_DIE = '\\Images\\Images\\died_pic.jpg'
PAUSE_BETWEEN_STEPS_PLAYER = 0.26


LEVEL_GENERATOR_SPRITES = {
    "World_1":{
        "1": "Images\\Blocks\\World_1\\1.png",
        "2": "Images\\Blocks\\World_1\\2.png",
        "3": "Images\\Blocks\\World_1\\3.png",
        "4": "Images\\Blocks\\World_1\\4.png",
        "5": "Images\\Blocks\\World_1\\5.png",
        "6": "Images\\Blocks\\World_1\\6.png",
        "7": "Images\\Blocks\\World_1\\7.png",
        "8": "Images\\Blocks\\World_1\\8.png",
        "9": "Images\\Blocks\\World_1\\9.png",
        "!": "Images\\Blocks\\World_1\\!.png",
        "@": "Images\\Blocks\\World_1\\@.png",
        "#": "Images\\Blocks\\World_1\\#.png",
        "$": "Images\\Blocks\\World_1\\$.png",
        "W": "Images\\Blocks\\World_1\\W.png",
        "V": "Images\\Blocks\\World_1\\V.png",
        "S": "Images\\Blocks\\World_1\\S.png",
        "D": "Images\\Blocks\\World_1\\D.png",
        "K": "Images\\Blocks\\World_1\\K.png",
        "C": "Images\\Blocks\\World_1\\C.png",
        "P": "Images\\Blocks\\World_1\\P.png",
        "Background": "Images\\UI\\BackgroundSummer.png"
    },
    "World_2":{
        "1": "Images\\Blocks\\World_2\\1.png",
        "2": "Images\\Blocks\\World_2\\2.png",
        "3": "Images\\Blocks\\World_2\\3.png",
        "4": "Images\\Blocks\\World_2\\4.png",
        "5": "Images\\Blocks\\World_2\\5.png",
        "6": "Images\\Blocks\\World_2\\6.png",
        "7": "Images\\Blocks\\World_2\\7.png",
        "8": "Images\\Blocks\\World_2\\8.png",
        "9": "Images\\Blocks\\World_2\\9.png",
        "!": "Images\\Blocks\\World_2\\!.png",
        "@": "Images\\Blocks\\World_2\\@.png",
        "#": "Images\\Blocks\\World_2\\#.png",
        "$": "Images\\Blocks\\World_2\\$.png",
        "W": "Images\\Blocks\\World_2\\W.png",
        "V": "Images\\Blocks\\World_2\\V.png",
        "S": "Images\\Blocks\\World_2\\S.png",
        "D": "Images\\Blocks\\World_2\\D.png",
        "K": "Images\\Blocks\\World_2\\K.png",
        "C": "Images\\Blocks\\World_2\\C.png",
        "P": "Images\\Blocks\\World_2\\P.png",
        "Background": "Images\\UI\\BackgroundWinter.png"
    }
}

UI_SPRITES = {
    "BackgroundWinter": "Images\\UI\\BackgroundWinter.png",
    "D1_Button": "Images\\UI\\D1_Button.png",
    "Earse": "Images\\Editor\\Earse.png",
    "Paint": "Images\\Editor\\Paint.png",
    "Save": "Images\\Editor\\Save.png",
    "Back": "Images\\UI\\Back.png",
    "Ru": "Images\\UI\\RuLangUI.png",
    "Eng": "Images\\UI\\EngLangUI.png",
    "Empty": "Images\\UI\\Empty.png",
}


IMAGES = {
    "U_Speed": "Images\\Images\\U_Speed.png",
    "U_Jump": "Images\\Images\\U_Jump.png",
    "U_Coin": "Images\\Images\\U_Coin.png",
}


SOUNDS_UI = {
    "B_Click": "Sounds\\UI\\B_Click.ogg",
    "Test": "Sounds\\UI\\Test.wav",
}

SOUNDS_GAME = {
    "W1_Music": "Sounds\\Game\\W1_Background_JASS.ogg",
    "W2_Music": "Sounds\\Game\\W2_Background.ogg",
    "Step": "Sounds\\Game\\Step.ogg",
    "Water": "Sounds\\Game\\FallWater.ogg",
    "CollectCoin": "Sounds\\Game\\CollectCoin.ogg",
    "CollectKey": "Sounds\\Game\\CollectKey.ogg",
    "LockedDoor": "Sounds\\Game\\LockedDoor.ogg",
    "SpikeTrap": "Sounds\\Game\\SpikeTrap.ogg",
    "OpenDoor": "Sounds\\Game\\OpenDoor.ogg",
}



class PlayerImages:
    imagesList_Jump_S = [
                  'Images\\Animations\\Player\\jump\\Прыгает_000.png', 'Images\\Animations\\Player\\jump\\Прыгает_001.png', 'Images\\Animations\\Player\\jump\\Прыгает_002.png', 'Images\\Animations\\Player\\jump\\Прыгает_003.png', 'Images\\Animations\\Player\\jump\\Прыгает_004.png', 'Images\\Animations\\Player\\jump\\Прыгает_005.png', 'Images\\Animations\\Player\\jump\\Прыгает_006.png', 'Images\\Animations\\Player\\jump\\Прыгает_007.png', 'Images\\Animations\\Player\\jump\\Прыгает_008.png',
                  'Images\\Animations\\Player\\jump\\Прыгает_009.png', 'Images\\Animations\\Player\\jump\\Прыгает_010.png', 'Images\\Animations\\Player\\jump\\Прыгает_011.png', 'Images\\Animations\\Player\\jump\\Прыгает_012.png', 'Images\\Animations\\Player\\jump\\Прыгает_013.png', 'Images\\Animations\\Player\\jump\\Прыгает_014.png', 'Images\\Animations\\Player\\jump\\Прыгает_015.png', 'Images\\Animations\\Player\\jump\\Прыгает_016.png', 'Images\\Animations\\Player\\jump\\Прыгает_017.png',
                  'Images\\Animations\\Player\\jump\\Прыгает_018.png', 'Images\\Animations\\Player\\jump\\Прыгает_019.png', 'Images\\Animations\\Player\\jump\\Прыгает_020.png', 'Images\\Animations\\Player\\jump\\Прыгает_021.png', 'Images\\Animations\\Player\\jump\\Прыгает_022.png', 'Images\\Animations\\Player\\jump\\Прыгает_023.png', 'Images\\Animations\\Player\\jump\\Прыгает_024.png', 'Images\\Animations\\Player\\jump\\Прыгает_025.png', 'Images\\Animations\\Player\\jump\\Прыгает_026.png',
                  'Images\\Animations\\Player\\jump\\Прыгает_027.png', 'Images\\Animations\\Player\\jump\\Прыгает_028.png', 'Images\\Animations\\Player\\jump\\Прыгает_029.png', 'Images\\Animations\\Player\\jump\\Прыгает_030.png', 'Images\\Animations\\Player\\jump\\Прыгает_031.png', 'Images\\Animations\\Player\\jump\\Прыгает_032.png', 'Images\\Animations\\Player\\jump\\Прыгает_033.png', 'Images\\Animations\\Player\\jump\\Прыгает_034.png', 'Images\\Animations\\Player\\jump\\Прыгает_035.png',
                  'Images\\Animations\\Player\\jump\\Прыгает_036.png', 'Images\\Animations\\Player\\jump\\Прыгает_037.png', 'Images\\Animations\\Player\\jump\\Прыгает_038.png', 'Images\\Animations\\Player\\jump\\Прыгает_039.png', 'Images\\Animations\\Player\\jump\\Прыгает_040.png', 'Images\\Animations\\Player\\jump\\Прыгает_041.png', 'Images\\Animations\\Player\\jump\\Прыгает_042.png', 'Images\\Animations\\Player\\jump\\Прыгает_043.png', 'Images\\Animations\\Player\\jump\\Прыгает_044.png',
                  'Images\\Animations\\Player\\jump\\Прыгает_045.png', 'Images\\Animations\\Player\\jump\\Прыгает_046.png', 'Images\\Animations\\Player\\jump\\Прыгает_047.png', 'Images\\Animations\\Player\\jump\\Прыгает_048.png', 'Images\\Animations\\Player\\jump\\Прыгает_049.png', 'Images\\Animations\\Player\\jump\\Прыгает_050.png', 'Images\\Animations\\Player\\jump\\Прыгает_051.png', 'Images\\Animations\\Player\\jump\\Прыгает_052.png', 'Images\\Animations\\Player\\jump\\Прыгает_053.png',
                  'Images\\Animations\\Player\\jump\\Прыгает_054.png', 'Images\\Animations\\Player\\jump\\Прыгает_055.png', 'Images\\Animations\\Player\\jump\\Прыгает_056.png', 'Images\\Animations\\Player\\jump\\Прыгает_057.png', 'Images\\Animations\\Player\\jump\\Прыгает_058.png', 'Images\\Animations\\Player\\jump\\Прыгает_059.png', 'Images\\Animations\\Player\\jump\\Прыгает_060.png', 'Images\\Animations\\Player\\jump\\Прыгает_061.png']

    imagesList_Run_S = ['Images\\Animations\\Player\\run\\бегает_000.png', 'Images\\Animations\\Player\\run\\бегает_002.png', 'Images\\Animations\\Player\\run\\бегает_003.png', 'Images\\Animations\\Player\\run\\бегает_004.png', 'Images\\Animations\\Player\\run\\бегает_005.png', 'Images\\Animations\\Player\\run\\бегает_006.png', 'Images\\Animations\\Player\\run\\бегает_007.png', 'Images\\Animations\\Player\\run\\бегает_008.png', 'Images\\Animations\\Player\\run\\бегает_009.png', 'Images\\Animations\\Player\\run\\бегает_010.png', 'Images\\Animations\\Player\\run\\бегает_011.png', 'Images\\Animations\\Player\\run\\бегает_012.png', 'Images\\Animations\\Player\\run\\бегает_013.png', 'Images\\Animations\\Player\\run\\бегает_014.png', 'Images\\Animations\\Player\\run\\бегает_015.png', 'Images\\Animations\\Player\\run\\бегает_016.png', 'Images\\Animations\\Player\\run\\бегает_017.png', 'Images\\Animations\\Player\\run\\бегает_018.png', 'Images\\Animations\\Player\\run\\бегает_019.png', 'Images\\Animations\\Player\\run\\бегает_020.png', 'Images\\Animations\\Player\\run\\бегает_021.png', 'Images\\Animations\\Player\\run\\бегает_022.png', 'Images\\Animations\\Player\\run\\бегает_023.png', 'Images\\Animations\\Player\\run\\бегает_024.png', 'Images\\Animations\\Player\\run\\бегает_025.png', 'Images\\Animations\\Player\\run\\бегает_026.png', 'Images\\Animations\\Player\\run\\бегает_027.png', 'Images\\Animations\\Player\\run\\бегает_028.png', 'Images\\Animations\\Player\\run\\бегает_029.png', 'Images\\Animations\\Player\\run\\бегает_030.png', 'Images\\Animations\\Player\\run\\бегает_031.png', 'Images\\Animations\\Player\\run\\бегает_032.png', 'Images\\Animations\\Player\\run\\бегает_033.png', 'Images\\Animations\\Player\\run\\бегает_034.png', 'Images\\Animations\\Player\\run\\бегает_035.png', 'Images\\Animations\\Player\\run\\бегает_036.png', 'Images\\Animations\\Player\\run\\бегает_037.png', 'Images\\Animations\\Player\\run\\бегает_038.png', 'Images\\Animations\\Player\\run\\бегает_039.png', 'Images\\Animations\\Player\\run\\бегает_040.png', 'Images\\Animations\\Player\\run\\бегает_041.png', 'Images\\Animations\\Player\\run\\бегает_042.png', 'Images\\Animations\\Player\\run\\бегает_043.png', 'Images\\Animations\\Player\\run\\бегает_044.png', 'Images\\Animations\\Player\\run\\бегает_045.png', 'Images\\Animations\\Player\\run\\бегает_046.png', 'Images\\Animations\\Player\\run\\бегает_047.png', 'Images\\Animations\\Player\\run\\бегает_048.png', 'Images\\Animations\\Player\\run\\бегает_049.png', 'Images\\Animations\\Player\\run\\бегает_050.png', 'Images\\Animations\\Player\\run\\бегает_051.png', 'Images\\Animations\\Player\\run\\бегает_052.png', 'Images\\Animations\\Player\\run\\бегает_053.png', 'Images\\Animations\\Player\\run\\бегает_054.png', 'Images\\Animations\\Player\\run\\бегает_055.png', 'Images\\Animations\\Player\\run\\бегает_056.png', 'Images\\Animations\\Player\\run\\бегает_057.png', 'Images\\Animations\\Player\\run\\бегает_058.png', 'Images\\Animations\\Player\\run\\бегает_059.png', 'Images\\Animations\\Player\\run\\бегает_060.png', 'Images\\Animations\\Player\\run\\бегает_061.png']

    imagesList_Idle_S = ['Images\\Animations\\Player\\idle\\стаит_000.png', 'Images\\Animations\\Player\\idle\\стаит_001.png', 'Images\\Animations\\Player\\idle\\стаит_002.png', 'Images\\Animations\\Player\\idle\\стаит_003.png', 'Images\\Animations\\Player\\idle\\стаит_004.png', 'Images\\Animations\\Player\\idle\\стаит_005.png', 'Images\\Animations\\Player\\idle\\стаит_006.png', 'Images\\Animations\\Player\\idle\\стаит_007.png', 'Images\\Animations\\Player\\idle\\стаит_008.png',
                  'Images\\Animations\\Player\\idle\\стаит_009.png', 'Images\\Animations\\Player\\idle\\стаит_010.png', 'Images\\Animations\\Player\\idle\\стаит_011.png', 'Images\\Animations\\Player\\idle\\стаит_012.png', 'Images\\Animations\\Player\\idle\\стаит_013.png', 'Images\\Animations\\Player\\idle\\стаит_014.png', 'Images\\Animations\\Player\\idle\\стаит_015.png', 'Images\\Animations\\Player\\idle\\стаит_016.png', 'Images\\Animations\\Player\\idle\\стаит_017.png',
                  'Images\\Animations\\Player\\idle\\стаит_018.png', 'Images\\Animations\\Player\\idle\\стаит_019.png', 'Images\\Animations\\Player\\idle\\стаит_020.png', 'Images\\Animations\\Player\\idle\\стаит_021.png', 'Images\\Animations\\Player\\idle\\стаит_022.png', 'Images\\Animations\\Player\\idle\\стаит_023.png', 'Images\\Animations\\Player\\idle\\стаит_024.png', 'Images\\Animations\\Player\\idle\\стаит_025.png', 'Images\\Animations\\Player\\idle\\стаит_026.png',
                  'Images\\Animations\\Player\\idle\\стаит_027.png', 'Images\\Animations\\Player\\idle\\стаит_028.png', 'Images\\Animations\\Player\\idle\\стаит_029.png', 'Images\\Animations\\Player\\idle\\стаит_030.png', 'Images\\Animations\\Player\\idle\\стаит_031.png', 'Images\\Animations\\Player\\idle\\стаит_032.png', 'Images\\Animations\\Player\\idle\\стаит_033.png', 'Images\\Animations\\Player\\idle\\стаит_034.png', 'Images\\Animations\\Player\\idle\\стаит_035.png',
                  'Images\\Animations\\Player\\idle\\стаит_036.png', 'Images\\Animations\\Player\\idle\\стаит_037.png', 'Images\\Animations\\Player\\idle\\стаит_038.png', 'Images\\Animations\\Player\\idle\\стаит_039.png', 'Images\\Animations\\Player\\idle\\стаит_040.png', 'Images\\Animations\\Player\\idle\\стаит_041.png', 'Images\\Animations\\Player\\idle\\стаит_042.png', 'Images\\Animations\\Player\\idle\\стаит_043.png', 'Images\\Animations\\Player\\idle\\стаит_044.png',
                  'Images\\Animations\\Player\\idle\\стаит_045.png', 'Images\\Animations\\Player\\idle\\стаит_046.png', 'Images\\Animations\\Player\\idle\\стаит_047.png', 'Images\\Animations\\Player\\idle\\стаит_048.png', 'Images\\Animations\\Player\\idle\\стаит_049.png', 'Images\\Animations\\Player\\idle\\стаит_050.png', 'Images\\Animations\\Player\\idle\\стаит_051.png', 'Images\\Animations\\Player\\idle\\стаит_052.png', 'Images\\Animations\\Player\\idle\\стаит_053.png',
                  'Images\\Animations\\Player\\idle\\стаит_054.png', 'Images\\Animations\\Player\\idle\\стаит_055.png', 'Images\\Animations\\Player\\idle\\стаит_056.png', 'Images\\Animations\\Player\\idle\\стаит_057.png', 'Images\\Animations\\Player\\idle\\стаит_058.png', 'Images\\Animations\\Player\\idle\\стаит_059.png', 'Images\\Animations\\Player\\idle\\стаит_060.png', 'Images\\Animations\\Player\\idle\\стаит_061.png']

    imagesList = {
        "jump": [],
        "run": [],
        "idle": []
    }

    def GenerateImages(self):
        freq = 4

        count = freq - 4
        for i in self.imagesList_Jump_S:
            if (count == 0):
                self.imagesList["jump"].append(image.load(i))
                count = freq - 4
            else:
                count -= 1

        count = freq
        for i in self.imagesList_Run_S:
            if (count == 0):
                self.imagesList["run"].append(image.load(i))
                count = freq
            else:
                count -= 1

        count = freq
        for i in self.imagesList_Idle_S:
            if (count == 0):
                self.imagesList["idle"].append(image.load(i))
                count = freq
            else:
                count -= 1

        print(len(self.imagesList["jump"]))



PlayerImages.GenerateImages(PlayerImages)



class Color:
    White = (0, 0, 0)
    Black = (255, 255, 255)

