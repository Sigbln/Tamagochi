import os
import pygame

# Делаю листы для aнимации
BG = [pygame.image.load(f"images/bg/{i}.gif") for i in
      range(len(os.listdir("images/bg")))]
EAT = [pygame.image.load(f"images/eat1/{i}.gif") for i in
       range(len(os.listdir("images/eat1")))]
BOT = [pygame.image.load(f"images/bot/{i}.gif") for i in
       range(len(os.listdir("images/bot")))]
SLEEP = [pygame.image.load(f"images/sleep/{i}.gif") for i in
         range(len(os.listdir("images/sleep")))]
DEAD = [pygame.image.load(f"images/dead/{i}.gif") for i in
        range(len(os.listdir("images/dead")))]

# format I - increase, E - Eat
increase_eat = pygame.image.load("images/rndm/i_e.jpg")
increase_bot = pygame.image.load("images/rndm/i_b.jpg")
increase_sleep = pygame.image.load("images/rndm/i_s.jpg")
decrease_eat = pygame.image.load("images/rndm/d_e.jpg")
decrease_bot = pygame.image.load("images/rndm/d_b.jpg")
decrease_sleep = pygame.image.load("images/rndm/d_s.jpg")
