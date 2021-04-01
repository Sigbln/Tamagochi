import pygame

import global_names
import HUD
import make_anims

pygame.init()


# проверка показателей на норму
def a_u_ok():
    # stat < 101
    global_names.pet.bot = min(global_names.pet.bot, global_names.FULL)
    global_names.pet.eat = min(global_names.pet.eat, global_names.FULL)
    global_names.pet.sleep = min(global_names.pet.sleep, global_names.FULL)

    # decrease hp if stats < 0
    global_names.pet.hp += min(global_names.pet.eat, global_names.EMPTY)
    global_names.pet.hp += min(global_names.pet.sleep, global_names.EMPTY)

    # stat >= 0
    global_names.pet.bot = max(global_names.pet.bot, global_names.EMPTY)
    global_names.pet.eat = max(global_names.pet.eat, global_names.EMPTY)
    global_names.pet.sleep = max(global_names.pet.sleep, global_names.EMPTY)

    if global_names.pet.hp <= global_names.EMPTY:
        global_names.pet.hp = global_names.FULL
        global_names.pet.eat = global_names.FULL
        global_names.pet.bot = global_names.FULL
        global_names.pet.sleep = global_names.FULL
        global_names.DEAD = True
        global_names.BG = False


# Уменьшение показателей
def stat_decrease():
    global_names.GAME_TIME -= global_names.ORDINARY_DECREASE
    if global_names.GAME_TIME == global_names.EMPTY:
        global_names.GAME_TIME = global_names.GAME_TIME_CONST
        if global_names.pet.bot > global_names.EMPTY:
            global_names.pet.bot -= global_names.ORDINARY_DECREASE
        if global_names.pet.sleep > global_names.EMPTY:
            global_names.pet.sleep -= global_names.ORDINARY_DECREASE
        if global_names.pet.eat > global_names.EMPTY:
            global_names.pet.eat -= global_names.ORDINARY_DECREASE
        if not global_names.pet.eat * global_names.pet.sleep:
            global_names.pet.hp -= global_names.ORDINARY_DECREASE


# время выполнения анимок
def timer():
    if not global_names.BG:
        if global_names.ANIM_TIME == global_names.EMPTY:
            if global_names.DEAD:
                global_names.RUN = False
            global_names.BG = True
            global_names.EAT = False
            global_names.SLEEP = False
            global_names.BOT = False
            global_names.ANIM_TIME = global_names.ANIM_TIME_CONST
        global_names.ANIM_TIME -= global_names.ORDINARY_DECREASE


def key_checker():
    for global_names.EVENT in pygame.event.get():
        if global_names.EVENT.type == pygame.QUIT:
            global_names.RUN = False
        if global_names.EVENT.type == pygame.KEYDOWN:  # проверка на действия
            if global_names.EVENT.key == pygame.K_f and global_names.BG:
                global_names.BG = False
                global_names.EAT = True
                global_names.pet.eat += global_names.EAT_INCREASE
                global_names.pet.bot -= global_names.BOT_DECREASE
                global_names.pet.sleep -= global_names.SLEEP_DECREASE
            if global_names.EVENT.key == pygame.K_s and global_names.BG:
                global_names.BG = False
                global_names.SLEEP = True
                global_names.pet.sleep += global_names.SLEEP_INCREASE
                global_names.pet.eat -= global_names.EAT_DECREASE
                if global_names.pet.bot > global_names.BOARD_BOT:
                    global_names.pet.bot += global_names.BOT_INCREASE
            if global_names.EVENT.key == pygame.K_b and global_names.BG:
                global_names.BG = False
                global_names.BOT = True
                global_names.pet.bot += global_names.BOT_INCREASE
                global_names.pet.sleep -= global_names.SLEEP_DECREASE
                global_names.pet.eat -= global_names.EAT_DECREASE


def draw_screen():
    t_eat = HUD.font1.render(f"Satiety: {global_names.pet.eat}", True,
                             global_names.WHITE)
    t_bot = HUD.font1.render(f"Bot:       {global_names.pet.bot}", True,
                             global_names.WHITE)
    t_sleep = HUD.font1.render(f"Sleep:   {global_names.pet.sleep}", True,
                               global_names.WHITE)

    if global_names.DEAD:  # отыгровка смерти
        screen = pygame.display.set_mode(global_names.DEAD_SCREEN)
        if global_names.ANIM_COUNT + 1 > global_names.DEAD_COUNT:
            global_names.ANIM_COUNT = global_names.EMPTY
        screen.blit(make_anims.DEAD1[global_names.ANIM_COUNT],
                    global_names.START_POINT)
        global_names.ANIM_COUNT += 1

    # BG
    elif global_names.BG:
        screen = pygame.display.set_mode(global_names.BG_SCREEN)
        if global_names.ANIM_COUNT + 1 > global_names.BG_COUNT:
            global_names.ANIM_COUNT = global_names.EMPTY
        screen.blit(make_anims.BG1[global_names.ANIM_COUNT // 2],
                    global_names.START_POINT)
        pygame.draw.rect(screen, global_names.BLACK, (10, 10, 70, 34))
        screen.blit(t_eat, (12, 12))
        screen.blit(t_bot, (12, 22))
        screen.blit(t_sleep, (12, 32))
        global_names.ANIM_COUNT += 1

    # Eat
    elif global_names.EAT:
        screen = pygame.display.set_mode(global_names.EAT_SCREEN)
        if global_names.ANIM_COUNT + 1 > global_names.EAT_COUNT:
            global_names.ANIM_COUNT = global_names.EMPTY
        screen.blit(make_anims.EAT1[global_names.ANIM_COUNT],
                    global_names.START_POINT)
        pygame.draw.rect(screen, global_names.BLACK, (10, 10, 80, 20))
        screen.blit(HUD.AEat[global_names.ANIM_COUNT * 3 // 40], (12, 12))
        global_names.ANIM_COUNT += 1

    # Bot
    elif global_names.BOT:
        screen = pygame.display.set_mode(global_names.BOT_SCREEN)
        if global_names.ANIM_COUNT + 1 > global_names.BOT_COUNT:
            global_names.ANIM_COUNT = global_names.EMPTY
        screen.blit(make_anims.BOT1[global_names.ANIM_COUNT // 10],
                    global_names.START_POINT)
        pygame.draw.rect(screen, global_names.BLACK, (10, 10, 100, 20))
        screen.blit(HUD.ABot[global_names.ANIM_COUNT // 10], (12, 12))
        global_names.ANIM_COUNT += 1

    # Sleep
    elif global_names.SLEEP:
        screen = pygame.display.set_mode(global_names.SLEEP_SCREEN)
        if global_names.ANIM_COUNT + 1 > global_names.SLEEP_COUNT:
            global_names.ANIM_COUNT = global_names.EMPTY
        screen.blit(make_anims.SLEEP1[global_names.ANIM_COUNT // 4],
                    global_names.START_POINT)
        pygame.draw.rect(screen, global_names.BLACK, (10, 10, 100, 20))
        screen.blit(HUD.ASleep[global_names.ANIM_COUNT // 20], (12, 12))
        global_names.ANIM_COUNT += 1

    pygame.display.update()
