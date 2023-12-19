from typing import Union

DEAD = 0
ALIVE = 1


class Cell:
    def __init__(self, state: int = DEAD, x: int = 0, y: int = 0):
        self.state: int = state
        self.x: int = x
        self.y: int = y

    def death(self) -> None:
        self.state = DEAD

    def birth(self) -> None:
        self.state = ALIVE

    def pos(self) -> tuple[int, int]:
        return self.x, self.y

    def is_alive(self) -> bool:
        return bool(self.state)


class Generation:
    def __init__(self):
        self.generation: list[Cell] | None = None

    def add(self, state: int, pos: tuple):
        cell = Cell(state=state, x=pos[0], y=pos[1])
        if self.generation is None:
            self.generation = [cell]
        else:
            self.generation.append(cell)

    def clear(self):
        self.generation.clear()

    @property
    def is_empty(self) -> bool:
        return not bool(self.generation)

    def get_cell(self, pos: tuple) -> Union[None, int]:
        for index, cell in enumerate(self.generation):
            if cell.pos() == pos:
                return index
        return None
