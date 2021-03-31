import global_names
import HUD
import make_anims
import pygame

pygame.init()


# проверка показателей на норму
def a_u_ok():
    if global_names.pet.bot > global_names.FULL:
        global_names.pet.bot = global_names.FULL
    if global_names.pet.sleep > global_names.FULL:
        global_names.pet.sleep = global_names.FULL
    if global_names.pet.sleep < global_names.EMPTY:
        global_names.pet.hp += global_names.pet.sleep
        global_names.pet.sleep = global_names.EMPTY
    if global_names.pet.eat > global_names.FULL:
        global_names.pet.eat = global_names.FULL
    if global_names.pet.eat < global_names.EMPTY:
        global_names.pet.hp += global_names.pet.eat
        global_names.pet.eat = global_names.EMPTY
    if global_names.pet.hp <= global_names.EMPTY:
        global_names.pet.hp = global_names.FULL
        global_names.pet.eat = global_names.FULL
        global_names.pet.bot = global_names.FULL
        global_names.pet.sleep = global_names.FULL
        global_names.DEAD = True
        global_names.BG = False


# Уменьшение показателей
def stat_decrease():
    global_names.GAME_TIME -= 1
    if global_names.GAME_TIME == global_names.EMPTY:
        global_names.GAME_TIME = 540
        if global_names.pet.bot > global_names.EMPTY:
            global_names.pet.bot -= 1
        if global_names.pet.sleep > global_names.EMPTY:
            global_names.pet.sleep -= 1
        if global_names.pet.eat > global_names.EMPTY:
            global_names.pet.eat -= 1
        if not global_names.pet.eat * global_names.pet.sleep:
            global_names.pet.hp -= 1


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
            global_names.ANIM_TIME = 150
        global_names.ANIM_TIME -= 1


def key_checker():
    for global_names.EVENT in pygame.event.get():
        if global_names.EVENT.type == pygame.QUIT:
            global_names.RUN = False
        if global_names.EVENT.type == pygame.KEYDOWN:  # проверка на действия
            if global_names.EVENT.key == pygame.K_f and global_names.BG:
                global_names.BG = False
                global_names.EAT = True
                global_names.pet.eat += 30
                global_names.pet.bot -= 5
                global_names.pet.sleep -= 5
            if global_names.EVENT.key == pygame.K_s and global_names.BG:
                global_names.BG = False
                global_names.SLEEP = True
                global_names.pet.sleep += 50
                global_names.pet.eat -= 20
                if global_names.pet.bot > 70:
                    global_names.pet.bot += 10
            if global_names.EVENT.key == pygame.K_b and global_names.BG:
                global_names.BG = False
                global_names.BOT = True
                global_names.pet.bot += 10
                global_names.pet.sleep -= 20
                global_names.pet.eat -= 20


def draw_screen():
    TEat = HUD.font1.render(f'Satiety: {global_names.pet.eat}', True,
                            global_names.WHITE)
    TBot = HUD.font1.render(f'Bot:       {global_names.pet.bot}', True,
                            global_names.WHITE)
    TSleep = HUD.font1.render(f'Sleep:   {global_names.pet.sleep}', True,
                              global_names.WHITE)
    if global_names.DEAD:  # отыгровка смерти
        screen = pygame.display.set_mode((576, 576))
        if global_names.ANIM_COUNT + 1 > 22:
            global_names.ANIM_COUNT = 0
        screen.blit(make_anims.DEAD1[global_names.ANIM_COUNT], (0, 0))
        global_names.ANIM_COUNT += 1
    elif global_names.BG:  #
        screen = pygame.display.set_mode((576, 275))
        if global_names.ANIM_COUNT + 1 > 96:
            global_names.ANIM_COUNT = 0
        screen.blit(make_anims.BG1[global_names.ANIM_COUNT // 2],
                    (0, 0))
        pygame.draw.rect(screen, global_names.BLACK, (10, 10, 70, 34))
        screen.blit(TEat, (12, 12))
        screen.blit(TBot, (12, 22))
        screen.blit(TSleep, (12, 32))
        global_names.ANIM_COUNT += 1
    elif global_names.EAT:  # Eat
        screen = pygame.display.set_mode((576, 504))
        if global_names.ANIM_COUNT + 1 > 40:
            global_names.ANIM_COUNT = 0
        screen.blit(make_anims.EAT1[global_names.ANIM_COUNT], (0, 0))
        pygame.draw.rect(screen, global_names.BLACK, (10, 10, 80, 20))
        screen.blit(HUD.AEat[global_names.ANIM_COUNT * 3 // 40], (12, 12))
        global_names.ANIM_COUNT += 1
    elif global_names.BOT:  # Bot
        screen = pygame.display.set_mode((576, 324))
        if global_names.ANIM_COUNT + 1 > 30:
            global_names.ANIM_COUNT = 0
        screen.blit(make_anims.BOT1[global_names.ANIM_COUNT // 10], (0, 0))
        pygame.draw.rect(screen, global_names.BLACK, (10, 10, 100, 20))
        screen.blit(HUD.ABot[global_names.ANIM_COUNT // 10], (12, 12))
        global_names.ANIM_COUNT += 1
    elif global_names.SLEEP:  # Sleep
        screen = pygame.display.set_mode((576, 430))
        if global_names.ANIM_COUNT + 1 > 60:
            global_names.ANIM_COUNT = 0
        screen.blit(make_anims.SLEEP1[global_names.ANIM_COUNT // 4], (0, 0))
        pygame.draw.rect(screen, global_names.BLACK, (10, 10, 100, 20))
        screen.blit(HUD.ASleep[global_names.ANIM_COUNT // 20], (12, 12))
        global_names.ANIM_COUNT += 1

    pygame.display.update()
