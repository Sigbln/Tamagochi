import os
import pygame

# Делаю листы для aнимации
BG1 = [pygame.image.load(f"images/bg/{i}.gif") for i in
       range(len(os.listdir("images/bg")))]
EAT1 = [pygame.image.load(f"images/eat1/{i}.gif") for i in
        range(len(os.listdir("images/eat1")))]
BOT1 = [pygame.image.load(f"images/bot/{i}.gif") for i in
        range(len(os.listdir("images/bot")))]
SLEEP1 = [pygame.image.load(f"images/sleep/{i}.gif") for i in
          range(len(os.listdir("images/sleep")))]
DEAD1 = [pygame.image.load(f"images/dead/{i}.gif") for i in
         range(len(os.listdir("images/dead")))]

# format I - increase, E - Eat
I_E = pygame.image.load("images/rndm/i_e.jpg")
I_B = pygame.image.load("images/rndm/i_b.jpg")
I_S = pygame.image.load("images/rndm/i_s.jpg")
D_E = pygame.image.load("images/rndm/d_e.jpg")
D_B = pygame.image.load("images/rndm/d_b.jpg")
D_S = pygame.image.load("images/rndm/d_s.jpg")
