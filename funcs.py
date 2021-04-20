import pygame
import random

import glbl_nms
import HUD
import make_anims

pygame.init()


# проверка показателей на норму
def a_u_ok():
    # stat < 101
    glbl_nms.pet.bot = min(glbl_nms.pet.bot,
                           glbl_nms.FULL)
    glbl_nms.pet.eat = min(glbl_nms.pet.eat, glbl_nms.FULL)
    glbl_nms.pet.sleep = min(glbl_nms.pet.sleep, glbl_nms.FULL)

    # decrease hp if stats < 0
    glbl_nms.pet.hp += min(glbl_nms.pet.eat, glbl_nms.EMPTY)
    glbl_nms.pet.hp += min(glbl_nms.pet.sleep, glbl_nms.EMPTY)

    # stat >= 0
    glbl_nms.pet.bot = max(glbl_nms.pet.bot, glbl_nms.EMPTY)
    glbl_nms.pet.eat = max(glbl_nms.pet.eat, glbl_nms.EMPTY)
    glbl_nms.pet.sleep = max(glbl_nms.pet.sleep, glbl_nms.EMPTY)

    if glbl_nms.pet.hp <= glbl_nms.EMPTY:
        glbl_nms.pet.hp = glbl_nms.FULL
        glbl_nms.pet.eat = glbl_nms.FULL
        glbl_nms.pet.bot = glbl_nms.FULL
        glbl_nms.pet.sleep = glbl_nms.FULL
        glbl_nms.DEAD = True
        glbl_nms.BG = False


# Уменьшение показателей
def stat_decrease():
    glbl_nms.GAME_TIME -= glbl_nms.ORDINARY_DECREASE
    if glbl_nms.GAME_TIME == glbl_nms.EMPTY:
        glbl_nms.GAME_TIME = glbl_nms.GAME_TIME_CONST
        if glbl_nms.pet.bot > glbl_nms.EMPTY:
            glbl_nms.pet.bot -= glbl_nms.ORDINARY_DECREASE
        if glbl_nms.pet.sleep > glbl_nms.EMPTY:
            glbl_nms.pet.sleep -= glbl_nms.ORDINARY_DECREASE
        if glbl_nms.pet.eat > glbl_nms.EMPTY:
            glbl_nms.pet.eat -= glbl_nms.ORDINARY_DECREASE
        if not glbl_nms.pet.eat * glbl_nms.pet.sleep:
            glbl_nms.pet.hp -= glbl_nms.ORDINARY_DECREASE


# время выполнения анимок
def timer():
    if not glbl_nms.BG:
        if glbl_nms.ANIM_TIME == glbl_nms.EMPTY:
            if glbl_nms.DEAD:
                glbl_nms.RUN = False
            glbl_nms.BG = True
            glbl_nms.EAT = False
            glbl_nms.SLEEP = False
            glbl_nms.BOT = False
            glbl_nms.ANIM_TIME = glbl_nms.ANIM_TIME_CONST
        glbl_nms.ANIM_TIME -= glbl_nms.ORDINARY_DECREASE


def key_checker():
    for glbl_nms.EVENT in pygame.event.get():
        if glbl_nms.EVENT.type == pygame.QUIT:
            glbl_nms.RUN = False
        if glbl_nms.EVENT.type == pygame.KEYDOWN:  # проверка на действия
            if glbl_nms.EVENT.key == pygame.K_f and glbl_nms.BG:
                glbl_nms.BG = False
                glbl_nms.EAT = True
                glbl_nms.pet.eat += glbl_nms.EAT_INCREASE
                glbl_nms.pet.bot -= glbl_nms.BOT_DECREASE
                glbl_nms.pet.sleep -= glbl_nms.SLEEP_DECREASE
            if glbl_nms.EVENT.key == pygame.K_s and glbl_nms.BG:
                glbl_nms.BG = False
                glbl_nms.SLEEP = True
                glbl_nms.pet.sleep += glbl_nms.SLEEP_INCREASE
                glbl_nms.pet.eat -= glbl_nms.EAT_DECREASE
                if glbl_nms.pet.bot > glbl_nms.BOARD_BOT:
                    glbl_nms.pet.bot += glbl_nms.BOT_INCREASE
            if glbl_nms.EVENT.key == pygame.K_b and glbl_nms.BG:
                glbl_nms.BG = False
                glbl_nms.BOT = True
                glbl_nms.pet.bot += glbl_nms.BOT_INCREASE
                glbl_nms.pet.sleep -= glbl_nms.SLEEP_DECREASE
                glbl_nms.pet.eat -= glbl_nms.EAT_DECREASE


# по воле случая изменяет показатели
def rndm_events():
    glbl_nms.RNDM_NAMBER = random.randint(glbl_nms.RNDM_CHS[0],
                                          glbl_nms.RNDM_CHS[1])
    # incr eat
    if glbl_nms.RNDM_NAMBER in range(glbl_nms.RNDM_CHANCE_I_EAT[0],
                                     glbl_nms.RNDM_CHANCE_I_EAT[1]):
        glbl_nms.pet.eat += random.randint(glbl_nms.RNDM_ORDINARY_DEINC[0],
                                           glbl_nms.RNDM_ORDINARY_DEINC[1])
        glbl_nms.EVENT_FLAG["eat inc"] = True
    # decr eat
    elif glbl_nms.RNDM_NAMBER in range(glbl_nms.RNDM_CHANCE_D_EAT[0],
                                       glbl_nms.RNDM_CHANCE_D_EAT[1]):
        glbl_nms.pet.eat -= random.randint(glbl_nms.RNDM_ORDINARY_DEINC[0],
                                           glbl_nms.RNDM_ORDINARY_DEINC[1])
        glbl_nms.EVENT_FLAG["eat dec"] = True
    # incr bot
    elif glbl_nms.RNDM_NAMBER in range(glbl_nms.RNDM_CHANCE_I_BOT[0],
                                       glbl_nms.RNDM_CHANCE_I_BOT[1]):
        glbl_nms.pet.bot += random.randint(glbl_nms.RNDM_ORDINARY_DEINC[0],
                                           glbl_nms.RNDM_ORDINARY_DEINC[1])
        glbl_nms.EVENT_FLAG["bot inc"] = True
    # decr bot
    elif glbl_nms.RNDM_NAMBER in range(glbl_nms.RNDM_CHANCE_D_BOT[0],
                                       glbl_nms.RNDM_CHANCE_D_BOT[1]):
        glbl_nms.pet.bot -= random.randint(glbl_nms.RNDM_ORDINARY_DEINC[0],
                                           glbl_nms.RNDM_ORDINARY_DEINC[1])
        glbl_nms.EVENT_FLAG["bot dec"] = True
    # incr sleep
    elif glbl_nms.RNDM_NAMBER in range(glbl_nms.RNDM_CHANCE_I_SLEEP[0],
                                       glbl_nms.RNDM_CHANCE_I_SLEEP[1]):
        glbl_nms.pet.sleep += random.randint(glbl_nms.RNDM_ORDINARY_DEINC[0],
                                             glbl_nms.RNDM_ORDINARY_DEINC[1])
        glbl_nms.EVENT_FLAG["sleep inc"] = True
    # decr sleep
    elif glbl_nms.RNDM_NAMBER in range(glbl_nms.RNDM_CHANCE_D_SLEEP[0],
                                       glbl_nms.RNDM_CHANCE_D_SLEEP[1]):
        glbl_nms.pet.sleep -= random.randint(glbl_nms.RNDM_ORDINARY_DEINC[0],
                                             glbl_nms.RNDM_ORDINARY_DEINC[1])
        glbl_nms.EVENT_FLAG["sleep dec"] = True


def event_time(n):
    if glbl_nms.RNDM_COUNT == glbl_nms.EMPTY:
        glbl_nms.EVENT_FLAG[n] = False
        glbl_nms.RNDM_COUNT = glbl_nms.RNDM_COUNT_CONST


# рисует таблички с информацией о рандомном событии
def draw_rndm_events():
    if glbl_nms.EVENT_FLAG["bot inc"]:
        event_time("bot inc")
        glbl_nms.RNDM_COUNT -= glbl_nms.ORDINARY_DECREASE
        glbl_nms.SCREEN.blit(make_anims.increase_bot,
                             glbl_nms.RNDM_START_POINT)
    elif glbl_nms.EVENT_FLAG["bot dec"]:
        event_time("bot dec")
        glbl_nms.RNDM_COUNT -= glbl_nms.ORDINARY_DECREASE
        glbl_nms.SCREEN.blit(make_anims.decrease_bot,
                             glbl_nms.RNDM_START_POINT)
    elif glbl_nms.EVENT_FLAG["eat inc"]:
        event_time("eat inc")
        glbl_nms.RNDM_COUNT -= glbl_nms.ORDINARY_DECREASE
        glbl_nms.SCREEN.blit(make_anims.increase_eat,
                             glbl_nms.RNDM_START_POINT)
    elif glbl_nms.EVENT_FLAG["eat dec"]:
        event_time("eat dec")
        glbl_nms.RNDM_COUNT -= glbl_nms.ORDINARY_DECREASE
        glbl_nms.SCREEN.blit(make_anims.decrease_eat,
                             glbl_nms.RNDM_START_POINT)
    elif glbl_nms.EVENT_FLAG["sleep inc"]:
        event_time("sleep inc")
        glbl_nms.RNDM_COUNT -= glbl_nms.ORDINARY_DECREASE
        glbl_nms.SCREEN.blit(make_anims.increase_sleep,
                             glbl_nms.RNDM_START_POINT)
    elif glbl_nms.EVENT_FLAG["sleep dec"]:
        event_time("sleep inc")
        glbl_nms.RNDM_COUNT -= glbl_nms.ORDINARY_DECREASE
        glbl_nms.SCREEN.blit(make_anims.decrease_sleep,
                             glbl_nms.RNDM_START_POINT)


def draw_screen():
    t_eat = HUD.font1.render(f"Satiety: {glbl_nms.pet.eat}", True,
                             glbl_nms.WHITE)
    t_bot = HUD.font1.render(f"Bot:       {glbl_nms.pet.bot}", True,
                             glbl_nms.WHITE)
    t_sleep = HUD.font1.render(f"Sleep:   {glbl_nms.pet.sleep}", True,
                               glbl_nms.WHITE)

    if glbl_nms.DEAD:  # отыгровка смерти
        glbl_nms.SCREEN = pygame.display.set_mode(glbl_nms.DEAD_SCREEN)
        if glbl_nms.ANIM_COUNT >= glbl_nms.DEAD_COUNT:
            glbl_nms.ANIM_COUNT = glbl_nms.EMPTY
        glbl_nms.SCREEN.blit(make_anims.DEAD[glbl_nms.ANIM_COUNT],
                             glbl_nms.START_POINT_2)
        glbl_nms.ANIM_COUNT += glbl_nms.ANIM_COUNT_INCREASE

    # BG
    elif glbl_nms.BG:
        glbl_nms.SCREEN = pygame.display.set_mode(glbl_nms.BG_SCREEN)
        if glbl_nms.ANIM_COUNT >= glbl_nms.BG_COUNT:
            glbl_nms.ANIM_COUNT = glbl_nms.EMPTY
        glbl_nms.SCREEN.blit(make_anims.BG[
                                 glbl_nms.ANIM_COUNT // glbl_nms.ANIM_C_BG],
                             glbl_nms.START_POINT_2)
        pygame.draw.rect(glbl_nms.SCREEN, glbl_nms.BLACK, glbl_nms.RECT_BG)
        glbl_nms.SCREEN.blit(t_eat, glbl_nms.START_POINT_1)
        glbl_nms.SCREEN.blit(t_bot, glbl_nms.START_POINT_T_BOT)
        glbl_nms.SCREEN.blit(t_sleep, glbl_nms.START_POINT_T_SLEEP)
        draw_rndm_events()
        glbl_nms.ANIM_COUNT += glbl_nms.ANIM_COUNT_INCREASE

    # Eat
    elif glbl_nms.EAT:
        glbl_nms.SCREEN = pygame.display.set_mode(glbl_nms.EAT_SCREEN)
        if glbl_nms.ANIM_COUNT >= glbl_nms.EAT_COUNT:
            glbl_nms.ANIM_COUNT = glbl_nms.EMPTY
        glbl_nms.SCREEN.blit(make_anims.EAT[glbl_nms.ANIM_COUNT],
                             glbl_nms.START_POINT_2)
        pygame.draw.rect(glbl_nms.SCREEN, glbl_nms.BLACK, glbl_nms.RECT_EAT)
        glbl_nms.SCREEN.blit(
            HUD.AEat[glbl_nms.ANIM_COUNT // glbl_nms.ANIM_C_EAT],
            glbl_nms.START_POINT_1)
        glbl_nms.ANIM_COUNT += glbl_nms.ANIM_COUNT_INCREASE

    # Bot
    elif glbl_nms.BOT:
        glbl_nms.SCREEN = pygame.display.set_mode(glbl_nms.BOT_SCREEN)
        if glbl_nms.ANIM_COUNT >= glbl_nms.BOT_COUNT:
            glbl_nms.ANIM_COUNT = glbl_nms.EMPTY
        glbl_nms.SCREEN.blit(make_anims.BOT[
                                 glbl_nms.ANIM_COUNT // glbl_nms.ANIM_C_BOT],
                             glbl_nms.START_POINT_2)
        pygame.draw.rect(glbl_nms.SCREEN, glbl_nms.BLACK, glbl_nms.RECT_BOT)
        glbl_nms.SCREEN.blit(
            HUD.ABot[glbl_nms.ANIM_COUNT // glbl_nms.ANIM_C_BOT],
            glbl_nms.START_POINT_1)
        glbl_nms.ANIM_COUNT += glbl_nms.ANIM_COUNT_INCREASE

    # Sleep
    elif glbl_nms.SLEEP:
        glbl_nms.SCREEN = pygame.display.set_mode(glbl_nms.SLEEP_SCREEN)
        if glbl_nms.ANIM_COUNT >= glbl_nms.SLEEP_COUNT:
            glbl_nms.ANIM_COUNT = glbl_nms.EMPTY
        glbl_nms.SCREEN.blit(
            make_anims.SLEEP[
                glbl_nms.ANIM_COUNT // glbl_nms.ANIM_C_SLEEP_1],
            glbl_nms.START_POINT_2)
        pygame.draw.rect(glbl_nms.SCREEN, glbl_nms.BLACK, glbl_nms.RECT_SLEEP)
        glbl_nms.SCREEN.blit(
            HUD.ASleep[
                glbl_nms.ANIM_COUNT // glbl_nms.ANIM_C_SLEEP_2],
            glbl_nms.START_POINT_1)
        glbl_nms.ANIM_COUNT += glbl_nms.ANIM_COUNT_INCREASE

    pygame.display.update()
