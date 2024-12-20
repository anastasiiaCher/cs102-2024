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
        return [[random.randint(0, randomize) for _ in range(self.cols)] for _ in range(self.rows)]

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
        y, x = cell
        return [
            self.curr_generation[i][j]
            for i in range(max(y - 1, 0), min(y + 1, self.rows - 1) + 1)
            for j in range(max(x - 1, 0), min(x + 1, self.cols - 1) + 1)
            if (i, j) != (y, x)
        ]

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        new_grid = self.create_grid()

        for y, row in enumerate(self.curr_generation):
            for x, cell in enumerate(row):
                match cell:
                    case 0:
                        new_grid[y][x] = sum(self.get_neighbours((y, x))) == 3
                    case 1:
                        new_grid[y][x] = sum(self.get_neighbours((y, x))) in (2, 3)
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.generations += 1
        self.prev_generation = [[_ for _ in line] for line in self.curr_generation]
        self.curr_generation = self.get_next_generation()

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= (self.max_generations or float("inf"))

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

        with open(filename, "r") as save_file:
            lines = save_file.readlines()
            pattern = [[int(cell) for cell in line.strip()] for line in lines if line.strip()]

            assert pattern, "Provided with an empty file"

            game = GameOfLife((len(pattern), len(pattern[0])), randomize=False)
            game.curr_generation = pattern
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w+") as save_file:
            save_file.writelines("".join(map(lambda e: str(int(e)), line)) + "\n" for line in self.curr_generation)
