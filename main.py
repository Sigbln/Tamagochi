from saver import *
from HUD import *
from make_anims import *

pygame.init()

load()  # загрузка сохранения

clock = pygame.time.Clock()
pygame.display.set_caption("MIPT study")


# проверка показателей на норму
def a_u_ok():
    global dead
    global bg
    if pet.bot > FULL:
        pet.bot = FULL
    if pet.sleep > FULL:
        pet.sleep = FULL
    if pet.sleep < EMPTY:
        pet.hp += pet.sleep
        pet.sleep = EMPTY
    if pet.eat > FULL:
        pet.eat = FULL
    if pet.eat < EMPTY:
        pet.hp += pet.eat
        pet.eat = EMPTY
    if pet.hp <= EMPTY:
        pet.hp = FULL
        pet.eat = FULL
        pet.bot = FULL
        pet.sleep = FULL
        dead = True
        bg = False


def draw_screen():
    global animCount

    if dead:  # отыгровка смерти
        screen = pygame.display.set_mode((576, 576))
        if animCount + 1 > 22:
            animCount = 0
        screen.blit(DEAD[animCount], (0, 0))
        animCount += 1
    elif bg:  # BG
        screen = pygame.display.set_mode((576, 275))
        if animCount + 1 > 96:
            animCount = 0
        screen.blit(BG[animCount // 2], (0, 0))
        pygame.draw.rect(screen, BLACK, (10, 10, 70, 34))
        screen.blit(TEat, (12, 12))
        screen.blit(TBot, (12, 22))
        screen.blit(TSleep, (12, 32))
        animCount += 1
    elif eat:  # Eat
        screen = pygame.display.set_mode((576, 504))
        if animCount + 1 > 40:
            animCount = 0
        screen.blit(EAT1[animCount], (0, 0))
        pygame.draw.rect(screen, BLACK, (10, 10, 80, 20))
        screen.blit(AEat[animCount * 3 // 40], (12, 12))
        animCount += 1
    elif bot:  # Bot
        screen = pygame.display.set_mode((576, 324))
        if animCount + 1 > 30:
            animCount = 0
        screen.blit(BOT1[animCount // 10], (0, 0))
        pygame.draw.rect(screen, BLACK, (10, 10, 100, 20))
        screen.blit(ABot[animCount // 10], (12, 12))
        animCount += 1
    elif sleep:  # Sleep
        screen = pygame.display.set_mode((576, 430))
        if animCount + 1 > 60:
            animCount = 0
        screen.blit(SLEEP1[animCount // 4], (0, 0))
        pygame.draw.rect(screen, BLACK, (10, 10, 100, 20))
        screen.blit(ASleep[animCount // 20], (12, 12))
        animCount += 1

    pygame.display.update()


run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:  # проверка на действия
            if event.key == pygame.K_f and bg:
                bg = False
                eat = True
                pet.eat += 30
                pet.bot -= 5
                pet.sleep -= 5
            if event.key == pygame.K_s and bg:
                bg = False
                sleep = True
                pet.sleep += 50
                pet.eat -= 20
                if pet.bot > 70:
                    pet.bot += 10
            if event.key == pygame.K_b and bg:
                bg = False
                bot = True
                pet.bot += 10
                pet.sleep -= 20
                pet.eat -= 20

    # Уменьшение показателей
    GAME_TIME -= 1
    if GAME_TIME == EMPTY:
        GAME_TIME = 540
        if pet.bot > EMPTY:
            pet.bot -= 1
        if pet.sleep > EMPTY:
            pet.sleep -= 1
        if pet.eat > EMPTY:
            pet.eat -= 1
        if not pet.eat * pet.sleep:
            pet.hp -= 1

    # время выполнения анимок
    if not bg:
        if ANIM_TIME == EMPTY:
            if dead:
                run = False
            bg = True
            eat = False
            sleep = False
            bot = False
            ANIM_TIME = 150
        ANIM_TIME -= 1

    a_u_ok()
    # обновляем выводимые значения
    TEat = font1.render(f'Satiety: {pet.eat}', True, WHITE)
    TBot = font1.render(f'Bot:       {pet.bot}', True, WHITE)
    TSleep = font1.render(f'Sleep:   {pet.sleep}', True, WHITE)

    draw_screen()

save()  # Сохраняем

pygame.quit()
