import pygame

# Делаю листы для анимации
BG1 = [pygame.image.load(f"images/bg/{i}.gif") for i in range(48)]
EAT1 = [pygame.image.load(f"images/eat1/{i}.gif") for i in range(40)]
BOT1 = [pygame.image.load(f"images/bot/{i}.gif") for i in range(3)]
SLEEP1 = [pygame.image.load(f"images/sleep/{i}.gif") for i in range(15)]
DEAD1 = [pygame.image.load(f"images/dead/{i}.gif") for i in range(22)]
