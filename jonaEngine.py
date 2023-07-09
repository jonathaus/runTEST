# JONA Engine v2.7

import pygame
import pickle
import os

# Colors
class colors():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0 , 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255 , 0)
    CYAN = (0, 255, 255)
    BROWN = (57, 45, 35)
    GRAY = (128, 128, 128)
    ORANGE = (255, 128, 0)
    PURPLE = (128, 0, 255)
    PINK = (255, 0, 255)
    DARK_GREEN = (0, 128, 0)
    DARK_RED = (128, 0, 0)
    DARK_BLUE = (0, 0, 128)
    DARK_GRAY = (64, 64, 64)
    DARK_ORANGE = (128, 64, 0)
    DARK_PURPLE = (64, 0, 128)
    DARK_PINK = (128, 0, 128)
    LIGHT_GREEN = (128, 255, 0)
    LIGHT_RED = (255, 128, 128)
    LIGHT_BLUE = (128, 128, 255)
    LIGHT_GRAY = (192, 192, 192)
    LIGHT_ORANGE = (255, 192, 128)
    LIGHT_PURPLE = (192, 128, 255)
    LIGHT_PINK = (255, 128, 255)

# Button Maker
class button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  
        self.clicked = False
        
    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if pygame.event.get(pygame.MOUSEBUTTONUP):
                    self.clicked = True
                    action = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

# Save and Load System
class SaveLoadSystem():
    def __init__(self, file_extension, save_folder):
        self.file_extension = file_extension
        self.save_folder = save_folder

    def save_data(self, data, name):
        data_file = open(self.save_folder + "/" + name + self.file_extension, "wb")
        pickle.dump(data, data_file)

    def load_data(self, name):
        data = open(self.save_folder + "/" + name + self.file_extension, "rb")
        data = pickle.load(data)
        return data
    
# Normal Text
def draw_text(surface, text, font, texl_col, x, y):
    img = font.render(text, True, texl_col)
    surface.blit(img, (x, y))

class spriteA():
    # Loading Animating Sprites
    def get_image(layer, sheet, frame, width, height, scale, color=None):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), layer, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image

    # Animating Sprites
    def animate(frame, steps, cooldown, last_time, current_time):
        current_time = pygame.time.get_ticks()
        if current_time - last_time > cooldown:
            last_time = current_time
            frame += 1
            if frame >= steps:
                frame = 0
        return frame, last_time

    # list creator
    def create_animator(spriteSheet, list_name, steps, last_time, cooldown, frame=0, layer=0):
        list_name = []
        for i in range(steps):
            list_name.append(spriteA.get_image(layer, spriteSheet, i, 288, 160, 3))
        return list_name, frame, last_time, cooldown

# Debugger
pygame.init()
debugfont = pygame.font.Font(None, 30)

def debug(info, y= 10, x= 10, title=""):
    display_surface = pygame.display.get_surface()
    debug_surf = debugfont.render(str(info), True, colors.WHITE)
    debug_rect = debug_surf.get_rect(topleft=(x, y))    
    pygame.draw.rect(display_surface, colors.BLACK, debug_rect)
    display_surface.blit(debug_surf, debug_rect)
    draw_text(display_surface, title, Fonts.small_font, colors.WHITE, x, y-15)

class Fonts():
    font = pygame.font.SysFont('Open Sans', 30)
    title_font = pygame.font.SysFont('Open Sans', 60)
    middle_font = pygame.font.SysFont('Open Sans', 45)
    giant_font = pygame.font.SysFont('Open Sans', 100)
    small_font = pygame.font.SysFont('Open Sans', 20)

def icon(iconImage):
    icon = pygame.image.load(iconImage).convert_alpha()
    pygame.display.set_icon(icon)

def FPS(screen, x, y, clock):
    draw_text(screen, "FPS: "+str(int(clock.get_fps())), Fonts.font, colors.BLACK, x, y)

def timer(time, press):
    current_time = pygame.time.get_ticks()
    if current_time - press > time:
        print("1 second")


    

