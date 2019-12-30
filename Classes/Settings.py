import json
import pygame


class SavesManager:
    save = {"player": {"jump_level": 1, "speed_level": 1, "moneys": 0}, "levels": {"level_1": {"open": True}, "level_2": {"open": False}, "level_3": {"open": False}}, "settings": {"language": "en", "volume": 1}}

    LANGUAGE_PATH = "Languages\\languages.json"

    LANGUAGE_FILE = {}
    with open(LANGUAGE_PATH, "r", encoding='utf-8') as language:
        LANGUAGE_FILE = json.load(language)

    LANGUAGE = save["settings"]["language"]
    AUDIO_VOLUME = save["settings"]["volume"]

    def LoadGame(self):
        try:
            with open("Saves\\save.json", "r") as saves:
                self.save = json.load(saves)
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


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


SavesManager.LoadGame(SavesManager)
SavesManager.ChangeLanguage(SavesManager)
SavesManager.ChangeVolume(SavesManager)


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


PLAYER_SIZE = (32, 64)
PLAYER_JUMP_FORCE = PLAYER_JUMP_FORCE_LEVELS[SavesManager.save["player"]["jump_level"]]["value"]
PLAYER_SPEED = PLAYER_SPEED_LEVELS[SavesManager.save["player"]["speed_level"]]["value"]


GRAVITY = 0.35


BLOCK_SIZE = (32, 32)
DOOR_SIZE = (32, 64)


COLOR = (0, 0, 0)
WIN_WIDTH = 700  # Ширина создаваемого окна
WIN_HEIGHT = 400  # Высота


PAUSE_TO_LOAD = 0.1


ANIMATION_DELAY = 0.1 # скорость смены кадров
ANIMATION_RIGHT = [('Images\\Animations\\Player\\run_r1.png'),
                   ('Images\\Animations\\Player\\run_r2.png'),
                   ('Images\\Animations\\Player\\run_r3.png')]
ANIMATION_LEFT = [('Images\\Animations\\Player\\run_l1.png'),
                  ('Images\\Animations\\Player\\run_l2.png'),
                  ('Images\\Animations\\Player\\run_l3.png')]
ANIMATION_JUMP_LEFT = ['Images\\Animations\\Player\\jump_l.png']
ANIMATION_JUMP_RIGHT = ['Images\\Animations\\Player\\jump_r.png']
ANIMATION_JUMP = ['Images\\Animations\\Player\\jump_r.png']
ANIMATION_STAY = ['Images\\Animations\\Player\\playerTest.png']
