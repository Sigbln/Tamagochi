import funcs
import global_names
import pygame
import saver

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("MIPT study")

saver.load()  # загрузка сохранения

while global_names.RUN:
    clock.tick(30)  # FPS

    funcs.key_checker()

    funcs.stat_decrease()

    funcs.timer()  # anim timer

    funcs.a_u_ok()  # checking stats for borders

    funcs.draw_screen()

saver.save()  # Сохраняем

pygame.quit()
