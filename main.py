import pygame
from pygame.locals import *
from sys import *
from perlin_noise import PerlinNoise
from random import randint

pygame.init()
pygame.display.set_caption('long severe cold')

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont('JetBrains Mono ExtraLight', 12)
noise = PerlinNoise(octaves=randint(2, 5), seed=114514)
Grass = pygame.image.load('long severe cold\pack\Grass.png')
elevation0 = pygame.image.load('long severe cold\pack\elevation0~250.png')
grassRect = Grass.get_rect()

while True:
    mousePos = pygame.mouse.get_pos()
    text = font.render(str(mousePos), True, 'Black')
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    screen.blit(text, (mousePos[0], mousePos[1] - 20))
    for x in range(20):
        for z in range(15):
            grassRect.topleft = (x * 40 , z * 40)
            elevation = noise([x/24, z/24]) * 8
            screen.blit(Grass, grassRect)
            if 0 <= elevation >= 250:
                elevation0.set_alpha(elevation / 2)
                screen.blit(elevation0, grassRect)
    
    pygame.display.update()
    clock.tick(60)
