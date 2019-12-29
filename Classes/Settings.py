import json


class SavesManager:
    save = {"player": {"jump_level": 1, "speed_level": 1, "moneys": 0}, "levels": {"level_1": {"open": True}, "level_2": {"open": False}, "level_3": {"open": False}}}

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

SavesManager.LoadGame(SavesManager)


AUDIO_VOLUME = 0
LANGUAGE_PATH = "Languages\\languages.json"

LANGUAGE_FILE = {}
with open(LANGUAGE_PATH, "r", encoding='utf-8') as language:
    LANGUAGE_FILE = json.load(language)

LANGUAGE = "ru"


PLAYER_JUMP_FORCE_LEVELS = {
    1: 5,
    2: 6,
    3: 7,
    4: 8,
}

PLAYER_SPEED_LEVELS = {
    1: 4,
    2: 5,
    3: 6,
    4: 7,
}


PLAYER_SIZE = (32, 64)
PLAYER_JUMP_FORCE = 7
PLAYER_SPEED = 5


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
