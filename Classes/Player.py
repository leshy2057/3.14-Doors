import pygame
from Classes.Settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position=[100, 100], rotation=0, walls=[], on_level_collect=0):
        super().__init__()

        self.position = position
        self.rotation = rotation
        self.color = ""

        self.on_level_collect = on_level_collect

        self.image = pygame.image.load("Images\\Animations\\Player\\stay_r.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position[0], self.position[1]

        self.mask = pygame.mask.from_surface(self.image)

        self.walls = walls

        self.on_level_collect = 0
        self.getKey = False
        self.inDoor = False

        self.speed = SavesManager.PLAYER_SPEED
        self._movingX = self.speed

        self.JUMP_POWER = SavesManager.PLAYER_JUMP_FORCE
        self.GRAVITY = GRAVITY  # Сила, которая будет тянуть нас вниз

        self.leftRight = "right"

        self.xvel = 0
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.stage = 'n'

        self.frames = ANIMATION_STAY_RIGHT
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

        self.soundStep = pygame.mixer.Sound(SOUNDS_GAME["Step"])
        self.soundStep.set_volume(SavesManager.AUDIO_VOLUME)

        self.soundWater = pygame.mixer.Sound(SOUNDS_GAME["Water"])
        self.soundWater.set_volume(SavesManager.AUDIO_VOLUME)

        self.soundCollectCoin = pygame.mixer.Sound(SOUNDS_GAME["CollectCoin"])
        self.soundCollectCoin.set_volume(SavesManager.AUDIO_VOLUME)

        self.soundCollectKey = pygame.mixer.Sound(SOUNDS_GAME["CollectKey"])
        self.soundCollectKey.set_volume(SavesManager.AUDIO_VOLUME)

        self.soundLockedDoor = pygame.mixer.Sound(SOUNDS_GAME["LockedDoor"])
        self.soundLockedDoor.set_volume(SavesManager.AUDIO_VOLUME)

        self.soundOpenDoor = pygame.mixer.Sound(SOUNDS_GAME["OpenDoor"])
        self.soundOpenDoor.set_volume(SavesManager.AUDIO_VOLUME)

        self.soundSpikesTrap = pygame.mixer.Sound(SOUNDS_GAME["SpikeTrap"])
        self.soundSpikesTrap.set_volume(SavesManager.AUDIO_VOLUME)

        self.use = False

        self.die = False

        self.pauseBetweenSteps = PAUSE_BETWEEN_STEPS_PLAYER
        self.getTicksLastFrame = pygame.time.get_ticks()

        self.update()


    def Move(self, keys):
        if (not self.inDoor):
            if not (keys[pygame.K_d] or keys[pygame.K_a]):  # стоим, когда нет указаний идти
                if (self.xvel > 0):
                    self.stage = "nr"
                elif (self.xvel < 0):
                    self.stage = "nl"
                else:
                    self.stage = 'nr' if (self.leftRight == "right") else 'nl'
                self.xvel = 0

            if (keys[pygame.K_d]):
                if (self._movingX == -self.speed):
                    self.Flip()
                    self._movingX = self.speed
                self.xvel = self.speed
                self.leftRight = "right"
                if (not keys[pygame.K_SPACE]):
                    self.stage = 'r'
            elif (keys[pygame.K_a]):
                if (self._movingX == self.speed):
                    self.Flip()
                    self._movingX = -self.speed
                self.xvel = -self.speed
                self.leftRight = "left"
                if (not keys[pygame.K_SPACE]):
                    self.stage = 'l'

            if (keys[pygame.K_SPACE]):
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -self.JUMP_POWER
                if (keys[pygame.K_d]):
                    self.stage = 'jr'
                elif (keys[pygame.K_a]):
                    self.stage = 'jl'
                else:
                    self.stage = 'jr' if (self.leftRight == "right") else 'jl'
        else:
            self.stage = 'nr' if (self.leftRight == "right") else 'nl'
            self.xvel = 0

        if not self.onGround:
            self.yvel += self.GRAVITY

        if (self.xvel != 0):
            if (self.pauseBetweenSteps <= 0):
                self.soundStep.play()
                self.pauseBetweenSteps = PAUSE_BETWEEN_STEPS_PLAYER
            self.pauseBetweenSteps -= (pygame.time.get_ticks() - self.getTicksLastFrame) / 1000.0
        else:
            self.pauseBetweenSteps = PAUSE_BETWEEN_STEPS_PLAYER
            self.soundStep.stop()

        self.getTicksLastFrame = pygame.time.get_ticks()

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.Collide(0, self.yvel, self.walls)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.Collide(self.xvel, 0, self.walls)
        # print(self.leftRight, self.stage)

        if self.stage == 'l':
            self.frames = ANIMATION_LEFT
        elif self.stage == 'r':
            self.frames = ANIMATION_RIGHT
        elif self.stage == 'jr':
            self.frames = ANIMATION_JUMP_RIGHT
        elif self.stage == 'jl':
            self.frames = ANIMATION_JUMP_LEFT
        elif self.stage == 'nl':
            self.frames = ANIMATION_STAY_LEFT
        elif self.stage == "nr":
            self.frames = ANIMATION_STAY_RIGHT


    def Collide(self, xvel, yvel, platforms):
        for prefab in platforms:
            if pygame.sprite.collide_rect(self, prefab):  # если есть пересечение платформы с игроком
                # print(prefab.tag)
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
                    self.soundCollectCoin.play()
                    prefab.use = True
                elif (prefab.tag == "Key" and not prefab.use):
                    self.getKey = True
                    self.soundCollectKey.play()
                    prefab.use = True
                elif (prefab.tag == "Door"):
                        if (not prefab.use and self.getKey):
                            self.soundOpenDoor.play()
                            self.inDoor = True
                        else:
                            self.soundLockedDoor.play()
                elif ((prefab.tag == "Water") and not prefab.use):
                    self.soundWater.play()
                elif ((prefab.tag == "WaterKill") and not prefab.use):
                    self.die = True

            if (pygame.sprite.collide_mask(self, prefab)):
                if (prefab.tag == "Spikes"):
                    self.soundSpikesTrap.play()
                    self.die = True


    def Flip(self):
        self.image = pygame.transform.flip(self.image, True, False)


    def rot_center(self):
        center = self.image.get_rect().center
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        new_rect = rotated_image.get_rect(center=center)
        return rotated_image


    def update(self):
        for event in pygame.event.get():
            if event.type == 30:
                print(1)

        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.name = self.frames[self.cur_frame]
        self.image = pygame.image.load(self.name).convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.mask = pygame.mask.from_surface(self.image)