from copy import deepcopy
import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        
        
        grid = [[0 for _ in range(self.cols)] for _ in range (self.rows)]

        if randomize:
            for x, row in enumerate(grid):
                for y, _ in enumerate(row):        
                    if (random.choice((False, True))):
                        grid[x][y] = 1

        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """

        x, y = cell
        neighbours = []
        
        if (x > 0 and y > 0): 
            neighbours.append(self.curr_generation[x - 1][y - 1])
        if (x > 0): 
            neighbours.append(self.curr_generation[x - 1][y])
        if (x > 0 and y < self.cols - 1): 
            neighbours.append(self.curr_generation[x - 1][y + 1])
        if (y > 0): 
            neighbours.append(self.curr_generation[x][y - 1])
        if (y < self.cols - 1): 
            neighbours.append(self.curr_generation[x][y + 1])
        if (x < self.rows - 1 and y > 0): 
            neighbours.append(self.curr_generation[x + 1][y - 1])
        if(x < self.rows - 1):
            neighbours.append(self.curr_generation[x + 1][y])
        if (x < self.rows - 1 and y < self.cols - 1):
            neighbours.append(self.curr_generation[x + 1][y + 1])

        return neighbours
     
    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        next_grid = [[0 for _ in range(self.cols)] for _ in range (self.rows)]

        for x, row in enumerate(self.curr_generation):
            for y, val in enumerate(row):
                neighbours = self.get_neighbours((x,y))
                if (val == 1):
                    if (1 < sum(neighbours) < 4):
                        next_grid[x][y] = 1
                else:
                    if (sum(neighbours) == 3):
                        next_grid[x][y] = 1

        return next_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = deepcopy(self.curr_generation)

        self.curr_generation = self.get_next_generation()

        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= self.max_generations


    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        if filename.is_file():
            with filename.open('r'):
                game = GameOfLife(size = (len(filename), len(filename[0])), randomize=False)
                for x, line in enumerate(filename):
                    for y, val in enumerate(line):
                        game.curr_generation[x][y] = val




    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        for x, row in enumerate(self.curr_generation):
            for y, val in enumerate(row):
                filename.write_text(val)
            filename.write_text('\n')
