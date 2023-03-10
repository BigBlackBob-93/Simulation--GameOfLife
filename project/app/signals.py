from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6 import QtGui
from PyQt6.QtCore import QTimer
from copy import deepcopy
import random
from project import config
from project.app.classes import Generation
from project.app.figures import (
    pulsar,
    gosper_gun
)
from project.app.objects import (
    table,
    random_btn,
    reset_btn,
    launch_btn,
    pulsar_btn,
    gosper_gun_btn
)

# ------ global variables ------
G = Generation()
sensor = False
time: QTimer


# ------ functions for signals ------
def set_disable_btn(disable: bool):
    random_btn.setDisabled(disable)
    reset_btn.setDisabled(disable)
    pulsar_btn.setDisabled(disable)
    gosper_gun_btn.setDisabled(disable)


def check_state():
    stop() if sensor else start()


def start():
    set_disable_btn(True)

    global sensor
    sensor = True

    if G.is_empty():
        set_figure()

    timer()


def stop():
    set_disable_btn(False)

    global sensor, time

    sensor = False
    time.stop()
    time.deleteLater()


def timer():
    global time

    time = QTimer()
    time.start()
    time.setInterval(100)
    time.timeout.connect(shot)


def shot():
    create_generation()
    draw_generation()


def create_generation():
    old_G = deepcopy(G)

    for i in range(old_G.len()):
        neighbours = search_neighbours(old_G.generation[i].pos(), old_G)
        if not old_G.generation[i].is_alive():
            if neighbours == 3:
                G.generation[i].birth()
        else:
            if (neighbours < 2) or (neighbours > 3):
                G.generation[i].death()


def search_neighbours(pos: tuple, old_G: Generation) -> int:
    alive_neighbours = 0
    column = pos[0]
    row = pos[1]

    for y in range(row - 1, row + 2):
        for x in range(column - 1, column + 2):
            if not ((x, y) == pos):
                neighbour = old_G.search_cell(pos=(x, y))
                if neighbour is not None:
                    if old_G.generation[neighbour].is_alive():
                        alive_neighbours += 1

    return alive_neighbours


def set_figure(character: tuple = None):
    reset()
    row = 0
    column = 0

    if not character:
        width = config.WIDTH
        height = config.HEIGHT
    else:
        width = character[0]
        height = character[1]

    for cell in range(width * height):
        G.add(state=random.randint(0, 1), pos=(column, row)) if not character else G.add(state=character[2][cell], pos=(column, row))
        column += 1
        if column >= width:
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


def set_pulsar():
    data = pulsar()
    set_figure(data)


def set_gosper_gun():
    data = gosper_gun()
    set_figure(data)


# ------ signals ------
random_btn.clicked.connect(set_figure)
launch_btn.clicked.connect(check_state)
reset_btn.clicked.connect(reset)
pulsar_btn.clicked.connect(set_pulsar)
gosper_gun_btn.clicked.connect(set_gosper_gun)
