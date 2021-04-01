import Pet
import pygame

pygame.init()

EVENT = None
MY_PATH = "save/save.pickle"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ANIM_COUNT = 0  # кадры для анимок
ANIM_TIME = 150  # тики анимок
ANIM_TIME_CONST = 150
GAME_TIME = 540  # тики до уменьшения показателей
GAME_TIME_CONST = 540

FULL = 100
EMPTY = 0
ORDINARY_DECREASE = 1
EAT_INCREASE = 30
BOT_INCREASE = 10
SLEEP_INCREASE = 50
EAT_DECREASE = 20
BOT_DECREASE = 20
SLEEP_DECREASE = 20
BOARD_BOT = 70

BG_SCREEN = (576, 275)
DEAD_SCREEN = (576, 576)
EAT_SCREEN = (576, 504)
BOT_SCREEN = (576, 324)
SLEEP_SCREEN = (576, 430)
BG_COUNT = 96
EAT_COUNT = 40
SLEEP_COUNT = 60
BOT_COUNT = 30
DEAD_COUNT = 22
START_POINT = (0, 0)
SCREEN = pygame.display.set_mode((576, 275))

BG = True
BOT = False
EAT = False
SLEEP = False
DEAD = False
RUN = True

pet = Pet.Pet()
