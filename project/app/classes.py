from typing import Union

DEAD = 0
ALIVE = 1


class Cell:
    def __init__(self, state=DEAD, x=0, y=0):
        self.state = state
        self.x = x
        self.y = y

    def death(self):
        self.state = DEAD

    def birth(self):
        self.state = ALIVE

    def pos(self):
        return self.x, self.y

    def is_alive(self) -> bool:
        if self.state == ALIVE:
            return True
        return False


class Generation:
    def __init__(self):
        self.generation: list[Cell] = []

    def add(self, state: int, pos: tuple):
        cell = Cell(state=state, x=pos[0], y=pos[1])
        self.generation.append(cell)

    def clear(self):
        self.generation.clear()

    def len(self) -> int:
        return len(self.generation)

    def is_empty(self) -> bool:
        if len(self.generation) == 0:
            return True
        return False

    def search_cell(self, pos: tuple) -> Union[None, int]:
        index = 0
        for cell in self.generation:
            if cell.pos() == pos:
                return index
            index += 1
        return None
