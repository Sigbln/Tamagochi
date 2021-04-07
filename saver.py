import os
import time

import global_names
import pickle

"""
проверяет существует ли файл с сохранением и загружаю последнее сохранение

сoef_decrease - значение на которое я буду уменьшать показатели после какого-то времени
в не игры, за 12 часов вне игры показатели падают на 40 пунктов
"""

# загружаем сохранение и уменьшаем показатели
def load():
    if os.path.exists(global_names.MY_PATH) and os.path.getsize(
            global_names.MY_PATH) > global_names.EMPTY:
        with open(global_names.MY_PATH, "rb") as f:
            data = pickle.load(f)
        coef_decrease = int((time.time() - data["time"]) / global_names.COEF)
        global_names.pet.eat = data["eat"] - coef_decrease
        if global_names.pet.eat < global_names.EMPTY:
            global_names.pet.hp += global_names.pet.eat
            global_names.pet.eat = global_names.EMPTY
        global_names.pet.sleep = data["sleep"] - coef_decrease
        if global_names.pet.sleep < global_names.EMPTY:
            global_names.pet.hp += global_names.pet.sleep
            global_names.pet.sleep = global_names.EMPTY
        global_names.pet.bot = data["bot"] - coef_decrease


# сохранение
def save():
    with open(global_names.MY_PATH, "wb") as f:
        data = {"eat": global_names.pet.eat, "bot": global_names.pet.bot,
                "sleep": global_names.pet.sleep,
                "hp": global_names.pet.hp,
                "time": time.time()}
        pickle.dump(data, f)
