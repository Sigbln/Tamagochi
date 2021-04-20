import pygame

import glbl_nms

pygame.init()

font1 = pygame.font.Font(None, glbl_nms.FRONT_1)  # Размер для HUD
font2 = pygame.font.Font(None, glbl_nms.FRONT_2)  # тоже
ABot = [font2.render("Botayem .", True, glbl_nms.WHITE),
        font2.render("Botayem ..", True, glbl_nms.WHITE),
        font2.render("Botayem ...", True, glbl_nms.WHITE)]
AEat = [font2.render("Eating .", True, glbl_nms.WHITE),
        font2.render("Eating ..", True, glbl_nms.WHITE),
        font2.render("Eating ...", True, glbl_nms.WHITE)]
ASleep = [font2.render("Sleeping .", True, glbl_nms.WHITE),
          font2.render("Sleeping ..", True, glbl_nms.WHITE),
          font2.render("Sleeping ...", True, glbl_nms.WHITE)]
