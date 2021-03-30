import pygame
from global_names import *

pygame.init()

font1 = pygame.font.Font(None, 15)  # Размер для HUD
font2 = pygame.font.Font(None, 25)
ABot = [font2.render('Botayem .', True, WHITE),
        font2.render('Botayem ..', True, WHITE),
        font2.render('Botayem ...', True, WHITE)]
AEat = [font2.render('Eating .', True, WHITE),
        font2.render('Eating ..', True, WHITE),
        font2.render('Eating ...', True, WHITE)]
ASleep = [font2.render('Sleeping .', True, WHITE),
          font2.render('Sleeping ..', True, WHITE),
          font2.render('Sleeping ...', True, WHITE)]
