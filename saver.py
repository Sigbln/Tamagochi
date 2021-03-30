from global_names import *
import pickle
import os
import time


# проверея существует ли файл с сохранением и загружаю последнее сохранение
def load():
    if os.path.exists(my_path) and os.path.getsize(my_path) > EMPTY:
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


# сохранение
def save():
    with open(my_path, 'wb') as f:
        data = {'eat': pet.eat, 'bot': pet.bot, 'sleep': pet.sleep,
                'hp': pet.hp,
                'time': time.time()}
        pickle.dump(data, f)
