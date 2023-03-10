from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6 import QtGui
from project.app.classes import Generation
from project.app.objects import (
    table,
    random_btn, reset_btn, launch_btn
)
from project import config
import random

# ------ global variables ------
G = Generation()
sensor = False


# ------ functions for signals ------
def set_disable_btn(disable: bool):
    random_btn.setDisabled(disable)
    reset_btn.setDisabled(disable)


def check_state():
    if sensor:
        stop()
    else:
        start()


def start():
    set_disable_btn(True)

    global sensor
    sensor = True

    if G.is_empty():
        set_rand_state()

    create_generation()
    draw_generation()


def stop():
    set_disable_btn(False)

    global sensor
    sensor = False


def create_generation():
    for i in range(G.len()):
        neighbours = search_neighbours(G.generation[i].pos())
        if not G.generation[i].is_alive():
            if neighbours == 3:
                G.generation[i].birth()
        else:
            if (neighbours < 2) or (neighbours > 3):
                G.generation[i].death()


def search_neighbours(pos: tuple) -> int:
    alive_neighbours = 0
    column = pos[0]
    row = pos[1]

    for y in range(row - 1, row + 2, 1):
        for x in range(column - 1, column + 2, 1):
            if (x == row) and (y == column):
                pass
            else:
                neighbour = G.search_cell(pos=(x, y))
                if neighbour is None:
                    pass
                else:
                    if G.generation[neighbour].is_alive():
                        alive_neighbours += 1

    return alive_neighbours


def set_rand_state():
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


def reset():
    global G

    for i in range(G.len()):
        pos = G.generation[i].pos()
        table.item(pos[1], pos[0]).setBackground(QtGui.QColor('#FFFFFF'))

    if not G.is_empty():
        G.clear()


# ------ signals ------
random_btn.clicked.connect(set_rand_state)
launch_btn.clicked.connect(check_state)
reset_btn.clicked.connect(reset)
