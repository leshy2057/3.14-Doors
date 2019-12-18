import pygame
from Classes.Settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position=[100, 100], rotation=0, walls=[]):
        super().__init__()

        self.position = position
        self.rotation = rotation
        self.color = ""

        self.image = pygame.image.load("Images\\playerTest.png")
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)

        self.walls = walls

        self.speed = PLAYER_SPEED
        self._movingX = self.speed

        self.JUMP_POWER = PLAYER_JUMP_FORCE
        self.GRAVITY = GRAVITY  # Сила, которая будет тянуть нас вниз

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position[0], self.position[1]

        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.p = 'n'


    def Move(self, keys):
        if (keys[pygame.K_d]):
            if (self._movingX == -self.speed):
                self.Flip()
                self._movingX = self.speed
            self.xvel = self.speed
            self.p = 'r'
        elif (keys[pygame.K_a]):
            if (self._movingX == self.speed):
                self.Flip()
                self._movingX = -self.speed
            self.xvel = -self.speed
            self.p = 'l'

        if (keys[pygame.K_SPACE]):
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -self.JUMP_POWER
            self.p = 'j'

        if not (keys[pygame.K_d] or keys[pygame.K_a]):  # стоим, когда нет указаний идти
            self.xvel = 0
            self.p = 'n'

        if not self.onGround:
            self.yvel += self.GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.Collide(0, self.yvel, self.walls)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.Collide(self.xvel, 0, self.walls)

        if self.p == 'l':
            player = AnimatedSprite(ANIMATION_LEFT)
        elif self.p == 'r':
            player = AnimatedSprite(ANIMATION_RIGHT)
        elif self.p == 'j':
            player = AnimatedSprite(ANIMATION_JUMP)
        elif self.p == 'n':
            player = Player()


    def Collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.p = 'r'

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.p = 'l'
                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
                    self.p = 'j'


    def Flip(self):
        self.image = pygame.transform.flip(self.image, True, False)


    def rot_center(self):
        center = self.image.get_rect().center
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        new_rect = rotated_image.get_rect(center=center)
        return rotated_image

class AnimatedSprite(Player):
    def __init__(self, animation_list, x=100, y=100):
        super().__init__()
        self.frames = animation_list
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.update()

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.name = self.frames[self.cur_frame]
        self.image = pygame.image.load(self.name)