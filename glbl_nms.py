import pygame

import Pet

pygame.init()

# random block
RNDM_NAMBER = 0
EVENT_FLAG = {"eat inc": False, "eat dec": False, "bot inc": False,
              "bot dec": False, "sleep inc": False, "sleep dec": False}
RNDM_CHS = [1, 120000]
RNDM_CHANCE_I_EAT = [0, 20]
RNDM_CHANCE_D_EAT = [20, 40]
RNDM_CHANCE_I_BOT = [40, 60]
RNDM_CHANCE_D_BOT = [60, 80]
RNDM_CHANCE_I_SLEEP = [80, 100]
RNDM_CHANCE_D_SLEEP = [100, 120]
RNDM_ORDINARY_DEINC = [1, 10]
RNDM_COUNT = 60
RNDM_COUNT_CONST = 60
RNDM_START_POINT = (150, 75)

EVENT = None
MY_PATH = "save/save.pickle"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ANIM_COUNT = 0  # кадры для анимок
ANIM_COUNT_INCREASE = 1
ANIM_TIME = 150  # тики анимок
ANIM_TIME_CONST = 150
ANIM_C_BG = 2
ANIM_C_EAT = 14
ANIM_C_BOT = 10
ANIM_C_SLEEP_1 = 4
ANIM_C_SLEEP_2 = 20
GAME_TIME = 540  # тики до уменьшения показателей
GAME_TIME_CONST = 540
COEF = 90 * 24

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
FRONT_1 = 15
FRONT_2 = 25

BG_SCREEN = (576, 275)
SCREEN = pygame.display.set_mode(BG_SCREEN)
DEAD_SCREEN = (576, 576)
EAT_SCREEN = (576, 504)
BOT_SCREEN = (576, 324)
SLEEP_SCREEN = (576, 430)
COUNTS = {"bg": 96, "eat": 40, "sleep": 60, "bot": 30, "dead": 22}
START_POINT_1 = (12, 12)
START_POINT_2 = (0, 0)
START_POINT_T_BOT = (12, 22)
START_POINT_T_SLEEP = (12, 32)
SCREEN = pygame.display.set_mode((576, 275))
RECT_BG = (10, 10, 70, 34)
RECT_EAT = (10, 10, 80, 20)
RECT_BOT = (10, 10, 100, 20)
RECT_SLEEP = (10, 10, 100, 20)

BG = True
BOT = False
EAT = False
SLEEP = False
DEAD = False
RUN = True

pet = Pet.Pet()
