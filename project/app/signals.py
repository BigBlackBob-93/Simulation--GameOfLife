from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6 import QtGui
from project.app.classes import Generation
from project.app.objects import (
    table,
    random_btn
)
from project import config
import random

# ------ global variables ------
G = Generation()


# ------ functions for signals ------
def set_rand_state():
    global G

    reset()
    row = 0
    column = 0

    for cell in range(config.WIDTH * config.HEIGHT):
        state = random.randint(0, 1)
        G.add(state=state, pos=(column, row))
        column += 1
        if column >= config.WIDTH:
            row += 1
            column = 0

    draw_generation()


def draw_generation():
    for i in range(G.len()):
        pos = G.generation[i].pos()
        table.setItem(pos[1], pos[0], QTableWidgetItem(' '))

        if G.generation[i].is_alive():
            table.item(pos[1], pos[0]).setBackground(QtGui.QColor(config.ALIVE_col))
        else:
            table.item(pos[1], pos[0]).setBackground(QtGui.QColor(config.DEAD_col))


def reset():
    if not G.is_empty():
        G.clear()


# ------ signals ------
random_btn.clicked.connect(set_rand_state)
