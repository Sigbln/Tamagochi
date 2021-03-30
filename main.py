import os
import pygame
import Pet
import pickle
import time

my_path = "save/save.pickle"

pygame.init()

pet = Pet.Pet()

# проверея существует ли файл с сохранением и загружаю последнее сохранение
if os.path.exists(my_path) and os.path.getsize(my_path) > 0:
    with open(my_path, 'rb') as f:
        data = pickle.load(f)
    kof = int((time.time() - data['time']) / (3600 * 24) * 40)
    pet.eat = data['eat'] - kof
    if pet.eat < 0:
        pet.hp += pet.eat
        pet.eat = 0
    pet.sleep = data['sleep'] - kof
    if pet.sleep < 0:
        pet.hp += pet.sleep
        pet.sleep = 0
    pet.bot = data['bot'] - kof

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# HUD
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

clock = pygame.time.Clock()
pygame.display.set_caption("MIPT study")

# Делаю листы для анимации
bg = True
BG = []
for i in range(48):
    BG.append(pygame.image.load(f"images/bg/{i}.gif"))

eat = False
EAT1 = []
for i in range(40):
    EAT1.append(pygame.image.load(f"images/eat1/{i}.gif"))

bot = False
BOT1 = []
for i in range(3):
    BOT1.append(pygame.image.load(f"images/bot/{i}.gif"))

sleep = False
SLEEP1 = []
for i in range(15):
    SLEEP1.append(pygame.image.load(f"images/sleep/{i}.gif"))

dead = False
DEAD = []
for i in range(22):
    DEAD.append(pygame.image.load(f"images/dead/{i}.gif"))

animCount = 0  # кадры для анимок
ANIM_TIME = 150  # тики анимок
GAME_TIME = 540  # тики до уменьшения показателей


# проверка показателей на норму
def a_u_ok():
    global dead
    global bg
    if pet.bot > 100:
        pet.bot = 100
    if pet.sleep > 100:
        pet.sleep = 100
    if pet.sleep < 0:
        pet.hp += pet.sleep
        pet.sleep = 0
    if pet.eat > 100:
        pet.eat = 100
    if pet.eat < 0:
        pet.hp += pet.eat
        pet.eat = 0
    if pet.hp < 1:
        pet.hp = 100
        pet.eat = 100
        pet.bot = 100
        pet.sleep = 100
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
    if GAME_TIME == 0:
        GAME_TIME = 540
        if pet.bot > 0:
            pet.bot -= 1
        if pet.sleep > 0:
            pet.sleep -= 1
        if pet.eat > 0:
            pet.eat -= 1
        if not pet.eat * pet.sleep:
            pet.hp -= 1

    # время выполнения анимок
    if not bg:
        if ANIM_TIME == 0:
            if dead:
                run = False
            bg = True
            eat = False
            sleep = False
            bot = False
            ANIM_TIME = 150
        ANIM_TIME -= 1

    a_u_ok()

    TEat = font1.render(f'Satiety: {pet.eat}', True, WHITE)
    TBot = font1.render(f'Bot:       {pet.bot}', True, WHITE)
    TSleep = font1.render(f'Sleep:   {pet.sleep}', True, WHITE)

    draw_screen()

# сохранение
with open(my_path, 'wb') as f:
    data = {'eat': pet.eat, 'bot': pet.bot, 'sleep': pet.sleep, 'hp': pet.hp,
            'time': time.time()}
    pickle.dump(data, f)

pygame.quit()
