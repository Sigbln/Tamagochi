import os
import pickle
import time

import glbl_nms

"""
проверяет существует ли файл с сохранением и загружаю последнее сохранение
сoef_decrease - значение на которое я буду уменьшать показатели после какого-то
времени в не игры, за 12 часов вне игры показатели падают на 40 пунктов
"""


# загружаем сохранение и уменьшаем показатели
def load():
    if os.path.exists(glbl_nms.MY_PATH) and os.path.getsize(
            glbl_nms.MY_PATH) > glbl_nms.EMPTY:
        with open(glbl_nms.MY_PATH, "rb") as f:
            data = pickle.load(f)
        coef_decrease = int((time.time() - data["time"]) / glbl_nms.COEF)
        glbl_nms.pet.eat = data["eat"] - coef_decrease
        if glbl_nms.pet.eat < glbl_nms.EMPTY:
            glbl_nms.pet.hp += glbl_nms.pet.eat
            glbl_nms.pet.eat = glbl_nms.EMPTY
        glbl_nms.pet.sleep = data["sleep"] - coef_decrease
        if glbl_nms.pet.sleep < glbl_nms.EMPTY:
            glbl_nms.pet.hp += glbl_nms.pet.sleep
            glbl_nms.pet.sleep = glbl_nms.EMPTY
        glbl_nms.pet.bot = data["bot"] - coef_decrease


# сохранение
def save():
    with open(glbl_nms.MY_PATH, "wb") as f:
        data = {"eat": glbl_nms.pet.eat, "bot": glbl_nms.pet.bot,
                "sleep": glbl_nms.pet.sleep,
                "hp": glbl_nms.pet.hp,
                "time": time.time()}
        pickle.dump(data, f)
