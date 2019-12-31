import pygame
from Classes.Settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position=[100, 100], rotation=0, walls=[], on_level_collect=0):
        super().__init__()

        self.position = position
        self.rotation = rotation
        self.color = ""

        self.on_level_collect = on_level_collect

        self.image = pygame.image.load("Images\\Animations\\Player\\stay_r.png")
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)

        self.walls = walls

        self.on_level_collect = 0
        self.getKey = False
        self.inDoor = False

        self.speed = SavesManager.PLAYER_SPEED
        self._movingX = self.speed

        self.JUMP_POWER = SavesManager.PLAYER_JUMP_FORCE
        self.GRAVITY = GRAVITY  # Сила, которая будет тянуть нас вниз

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position[0], self.position[1]

        self.xvel = 0
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.stage = 'n'

        self.frames = ANIMATION_STAY_RIGHT
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

        self.use = False

        self.on_water = False

        self.update()


    def Move(self, keys):
        if (keys[pygame.K_d]):
            if (self._movingX == -self.speed):
                self.Flip()
                self._movingX = self.speed
            self.xvel = self.speed
            if (not keys[pygame.K_SPACE]):
                self.stage = 'r'
        elif (keys[pygame.K_a]):
            if (self._movingX == self.speed):
                self.Flip()
                self._movingX = -self.speed
            self.xvel = -self.speed
            if (not keys[pygame.K_SPACE]):
                self.stage = 'l'

        if (keys[pygame.K_SPACE]):
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -self.JUMP_POWER
            if (keys[pygame.K_d]):
                self.stage = 'jr'
            if (keys[pygame.K_a]):
                self.stage = 'jl'
            else:
                self.stage = 'j'

        if not (keys[pygame.K_d] or keys[pygame.K_a]):  # стоим, когда нет указаний идти
            if (self.xvel > 0):
                self.stage = "nr"
            elif (self.xvel < 0):
                self.stage = "nl"
            self.xvel = 0

        if not self.onGround:
            self.yvel += self.GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.Collide(0, self.yvel, self.walls)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.Collide(self.xvel, 0, self.walls)

        if self.stage == 'l':
            self.frames = ANIMATION_LEFT
        elif self.stage == 'r':
            self.frames = ANIMATION_RIGHT
        elif self.stage == 'j':
            self.frames = ANIMATION_JUMP
        elif self.stage == 'jr':
            self.frames = ANIMATION_JUMP_LEFT
        elif self.stage == 'jl':
            self.frames = ANIMATION_JUMP_LEFT
        elif self.stage == 'nl':
            self.frames = ANIMATION_STAY_LEFT
        elif self.stage == "nr":
            self.frames = ANIMATION_STAY_RIGHT


    def Collide(self, xvel, yvel, platforms):
        for prefab in platforms:
            if pygame.sprite.collide_rect(self, prefab):  # если есть пересечение платформы с игроком
                print(prefab.tag)
                if (prefab.tag == "Block"):
                    if xvel > 0:  # если движется вправо
                        self.rect.right = prefab.rect.left  # то не движется вправо
                        self.p = 'r'

                    if xvel < 0:  # если движется влево
                        self.rect.left = prefab.rect.right  # то не движется влево
                        self.p = 'l'
                    if yvel > 0:  # если падает вниз
                        self.rect.bottom = prefab.rect.top  # то не падает вниз
                        self.onGround = True  # и становится на что-то твердое
                        self.yvel = 0  # и энергия падения пропадает

                    if yvel < 0:  # если движется вверх
                        self.rect.top = prefab.rect.bottom  # то не движется вверх
                        self.yvel = 0  # и энергия прыжка пропадает
                        self.p = 'j'
                elif (prefab.tag == "Coin" and not prefab.use):
                    self.on_level_collect += 1
                    prefab.use = True
                elif (prefab.tag == "Key" and not prefab.use):
                    self.getKey = True
                    prefab.use = True
                elif (prefab.tag == "Door" and not prefab.use and self.getKey):
                    self.inDoor = True
                elif (prefab.tag == "WaterKill" and not prefab.use):
                    self.on_water = True


    def Flip(self):
        self.image = pygame.transform.flip(self.image, True, False)


    def rot_center(self):
        center = self.image.get_rect().center
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        new_rect = rotated_image.get_rect(center=center)
        return rotated_image


    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.name = self.frames[self.cur_frame]
        self.image = pygame.image.load(self.name)
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)