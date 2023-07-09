
import pygame
from pygame import mixer
import jonaEngine
from random import randint as rnd
from jonaEngine import colors
from jonaEngine import Fonts
import math


pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Create game window
Name = ""
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(Name)

# Icon
jonaEngine.icon("data/jIcon.ico")

# game loop
run = True
while run:
    
    # FPS
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()  


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


# Top left text
    jonaEngine.draw_text(screen, Name, Fonts.font, colors.BLACK, 10, 10)
    jonaEngine.FPS(screen, 10, 40, clock)
    pygame.display.flip()

pygame.quit()