import Pet
import pygame

pygame.init()

EVENT = None
MY_PATH = "save/save.pickle"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ANIM_COUNT = 0  # кадры для анимок
ANIM_TIME = 150  # тики анимок
GAME_TIME = 540  # тики до уменьшения показателей
FULL = 100
EMPTY = 0
BG = True
BOT = False
EAT = False
SLEEP = False
DEAD = False
RUN = True
pet = Pet.Pet()
SCREEN = pygame.display.set_mode((576, 275))
