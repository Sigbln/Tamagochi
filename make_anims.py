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
