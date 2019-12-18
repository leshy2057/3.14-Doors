import requests, threading, time, json, random, pygame, sys
from Classes.Player import Player, AnimatedSprite
from Classes.Block import Block
from Classes.Camera import *
from Classes.Settings import *


map = []
player = Player()
def ifpos(player):
    if player.p == 'l':
        player = AnimatedSprite(ANIMATION_LEFT)
    elif player.p == 'r':
        player = AnimatedSprite(ANIMATION_RIGHT)
    elif player.p == 'j':
        player = AnimatedSprite(ANIMATION_JUMP)
    elif player.p == 'n':
        player = Player()


pygame.init()
clock = pygame.time.Clock()
windows = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Test")

surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))

blocks = pygame.sprite.Group()
wallList = pygame.sprite.Group()
platforms = []

level = [
       "-                           -|",
       "-                           -|",
       "-                           -|",
       "-                           -|",
       "-                           -|",
       "-                       -----|",
       "-                   --  -----|",
       "---------        --     -----|",
       "-           ---         -----|",
       "-                       -----|",
]

x, y, step = 0, 0, 32
level_for = ""
for i in level: level_for += i
for symbol in level_for:
    if (symbol == "-"):
        block = Block(x, y)
        blocks.add_internal(block)
        wallList.add_internal(block)
        x += step
    elif (symbol == "|"):
        x = 0
        y += step
    else:
        x += step
blocks.add_internal(player)
player.walls = wallList


total_level_width = len(level[0]) * BLOCK_SIZE[0]  # Высчитываем фактическую ширину уровня
total_level_height = len(level) * BLOCK_SIZE[1]  # высоту
camera = Camera(camera_configure, total_level_width, total_level_height)


pygame.key.set_repeat(1, 10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
            sys.exit()

    player.Move(pygame.key.get_pressed())
    player.update()
    surface.fill((255, 255, 255))

    camera.update(player)

    for i in blocks:
        surface.blit(i.image, camera.apply(i))
    
    windows.blit(surface, (0, 0))
    pygame.display.flip()
    clock.tick(30)


pygame.quit()