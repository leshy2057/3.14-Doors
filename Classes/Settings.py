import json,os

PLAYER_JUMP_FORCE_LEVELS = {
    1: {"value": 5, "price": 1},
    2: {"value": 6, "price": 10},
    3: {"value": 7, "price": 20},
    4: {"value": 8, "price": 30},
}

PLAYER_SPEED_LEVELS = {
    1: {"value": 4, "price": 1},
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
        except: pass

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


PLAYER_SIZE = (32, 64)


GRAVITY = 0.35


BLOCK_SIZE = (32, 32)
DOOR_SIZE = (32, 64)
BUTTON_LEVEL_SELECTOR_SIZE = (150, 150)
BUTTON_LEVEL_SELECTOR_STEP = 300
SCROLL_LEVEL_SELECTOR_STEP = 300


COLOR = (0, 0, 0)
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
        "Background": "Images\\UI\\BackgroundWinter.png"
    }
}

UI_SPRITES = {
    "BackgroundWinter": "Images\\UI\\BackgroundWinter.png",
    "D1_Button": "Images\\UI\\D1_Button.png",
    "Earse": "Images\\Editor\\Earse.png",
    "Paint": "Images\\Editor\\Paint.png",
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
    "W1_Music": "Sounds\\Game\\W1_Music.ogg",
}

