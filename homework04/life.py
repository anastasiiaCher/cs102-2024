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
        # Copy from previous assignment
        grid = [[0] * self.cols for _ in range(self.rows)]
        if randomize:
            for i, el in enumerate(grid):
                for j, _ in enumerate(el):
                    grid[i][j] = random.randint(0, 1)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        neighbors_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        grid_of_neighbours = []
        x, y = cell
        for i, j in neighbors_cells:
            cur_x, cur_y = x + i, y + j
            if 0 <= cur_x < len(self.curr_generation) and 0 <= cur_y < len(self.curr_generation[0]):
                grid_of_neighbours.append(self.curr_generation[cur_x][cur_y])
        return grid_of_neighbours

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        new_gid = self.create_grid()
        for i in range(self.rows):
            for j in range(self.cols):
                neighbours = self.get_neighbours((i, j))
                alive_neighbours = sum(neighbours)
                if 2 <= alive_neighbours <= 3 and self.curr_generation[i][j] == 1:
                    new_gid[i][j] = 1
                elif alive_neighbours == 3 and self.curr_generation[i][j] == 0:
                    new_gid[i][j] = 1
        return new_gid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.generations += 1
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations <= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return not self.prev_generation == self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, "r", encoding='utf-8') as f:
            lines = [line.strip() for line in f]
            grid = [[int(cell) for cell in line] for line in lines]

        game = GameOfLife((len(grid), len(grid[0])))
        game.curr_generation = [row for row in grid if row]
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w", encoding='utf-8') as f:
            for line in self.curr_generation:
                f.write("".join(map(str, line)) + "\n")
