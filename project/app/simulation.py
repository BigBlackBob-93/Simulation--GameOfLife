from random import randint
from copy import deepcopy

from project import constants
from project.app.window import MainWindow
from project.app.table import Table
from project.app.timer import Timer
from project.app.generation import Generation
from project.app.figures import (
    pulsar,
    gosper_gun,
)


class Simulation:
    def __init__(self):
        self.window: MainWindow = MainWindow()
        self.table: Table = Table()

        self.G = Generation()
        self.sensor: bool = False
        self.timer: Timer = Timer()

    def simulate(self) -> None:
        functions: tuple = (
            self.set_rand_figure,
            self.set_pulsar,
            self.set_gosper_gun,
            self.reset,
            self.check_state,
        )
        for index, function in enumerate(functions):
            self.window.set_btn_click(
                btn_index=index,
                function=function,
            )
        self.window.show()
        self.table.table.show()

    def check_state(self) -> None:
        if self.sensor:
            self.sensor = False
            self.stop()
        else:
            self.sensor = True
            self.start()

    def start(self) -> None:
        self.window.set_disable_btn(True)
        if self.G.is_empty:
            self.set_rand_figure()

        self.timer.start(self.shot)

    def stop(self) -> None:
        self.window.set_disable_btn(False)
        self.timer.stop()

    def shot(self) -> None:
        self.create_generation()
        self.draw_generation()

    def create_generation(self) -> None:
        old_g: Generation = deepcopy(self.G)

        for old_cell, cell in zip(old_g.generation, self.G.generation):
            neighbours = self.search_neighbours(pos=old_cell.pos(), old_g=old_g)
            if not old_cell.is_alive() and neighbours == 3:
                cell.birth()
            elif (neighbours < 2) or (neighbours > 3):
                cell.death()

    @staticmethod
    def search_neighbours(pos: tuple, old_g: Generation) -> int:
        alive_neighbours = 0
        column = pos[0]
        row = pos[1]

        for y in range(row - 1, row + 2):
            for x in range(column - 1, column + 2):
                if not ((x, y) == pos):
                    neighbour = old_g.get_cell(pos=(x, y))
                    if neighbour is not None and old_g.generation[neighbour].is_alive():
                        alive_neighbours += 1

        return alive_neighbours

    def draw_generation(self) -> None:
        for cell in self.G.generation:
            position: tuple = cell.pos()
            self.table.set_item(position=position)
            if cell.is_alive():
                self.table.set_color(position=position)

    def reset(self) -> None:
        if not self.G.is_empty:
            for cell in self.G.generation:
                self.table.set_color(
                    position=cell.pos(),
                    color='#FFFFFF',
                )
            self.G.clear()

    def set_rand_figure(self) -> None:
        self.reset()
        row: int = 0
        column: int = 0

        for cell in range(constants.FIGURE_WIDTH * constants.FIGURE_HEIGHT):
            self.G.add(
                state=randint(a=0, b=1),
                pos=(column, row),
            )
            column += 1
            if column >= constants.FIGURE_WIDTH:
                row += 1
                column = 0
        self.draw_generation()

    def set_figure(self, character: tuple) -> None:
        self.reset()
        row: int = 0
        column: int = 0

        for cell in range(character[0] * character[1]):
            self.G.add(
                state=character[2][cell],
                pos=(column, row),
            )
            column += 1
            if column >= character[0]:
                row += 1
                column = 0

        self.draw_generation()

    def set_pulsar(self):
        self.set_figure(
            character=pulsar(),
        )

    def set_gosper_gun(self):
        self.set_figure(
            character=gosper_gun(),
        )
