import pygame

import global_names

pygame.init()

font1 = pygame.font.Font(None, 15)  # Размер для HUD
font2 = pygame.font.Font(None, 25)  # тоже
ABot = [font2.render("Botayem .", True, global_names.WHITE),
        font2.render("Botayem ..", True, global_names.WHITE),
        font2.render("Botayem ...", True, global_names.WHITE)]
AEat = [font2.render("Eating .", True, global_names.WHITE),
        font2.render("Eating ..", True, global_names.WHITE),
        font2.render("Eating ...", True, global_names.WHITE)]
ASleep = [font2.render("Sleeping .", True, global_names.WHITE),
          font2.render("Sleeping ..", True, global_names.WHITE),
          font2.render("Sleeping ...", True, global_names.WHITE)]
