import pygame

# Делаю листы для анимации
BG = []
for i in range(48):
    BG.append(pygame.image.load(f"images/bg/{i}.gif"))

EAT1 = []
for i in range(40):
    EAT1.append(pygame.image.load(f"images/eat1/{i}.gif"))

BOT1 = []
for i in range(3):
    BOT1.append(pygame.image.load(f"images/bot/{i}.gif"))

SLEEP1 = []
for i in range(15):
    SLEEP1.append(pygame.image.load(f"images/sleep/{i}.gif"))

DEAD = []
for i in range(22):
    DEAD.append(pygame.image.load(f"images/dead/{i}.gif"))
