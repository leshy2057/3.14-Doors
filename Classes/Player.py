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
        '''
        # self.image.set_colorkey(Color(COLOR)) # делаем фон прозрачным
        #        Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево        
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
                
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0)) # По-умолчанию, стоим
                
        self.boltAnimJumpLeft= pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()
                
        self.boltAnimJumpRight= pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()
                
        self.boltAnimJump= pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play() '''


    def Move(self, keys):
        if (keys[pygame.K_d]):
            if (self._movingX == -self.speed):
                self.Flip()
                self._movingX = self.speed
            self.xvel = self.speed
        elif (keys[pygame.K_a]):
            if (self._movingX == self.speed):
                self.Flip()
                self._movingX = -self.speed
            self.xvel = -self.speed

        if (keys[pygame.K_SPACE]):
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -self.JUMP_POWER

        if not (keys[pygame.K_d] or keys[pygame.K_a]):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not self.onGround:
            self.yvel += self.GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.Collide(0, self.yvel, self.walls)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.Collide(self.xvel, 0, self.walls)


    def Collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


    def Flip(self):
        self.image = pygame.transform.flip(self.image, True, False)


    def rot_center(self):
        center = self.image.get_rect().center
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        new_rect = rotated_image.get_rect(center=center)
        return rotated_image
