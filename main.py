import pygame

import funcs
import glbl_nms
import saver

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("MIPT study")

saver.load()  # загрузка сохранения

while glbl_nms.RUN:
    clock.tick(30)  # FPS
    funcs.rndm_events()
    funcs.key_checker()
    funcs.stat_decrease()  # decrease stats
    funcs.timer()  # anim timer
    funcs.a_u_ok()  # checking stats for borders
    funcs.draw_screen()

saver.save()  # Сохраняем

pygame.quit()
