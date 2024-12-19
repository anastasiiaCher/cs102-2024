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
        self.rows, self.cols = size
        self.prev_generation = self.create_grid()
        self.curr_generation = self.create_grid(randomize=randomize)
        self.max_generations = max_generations
        self.generations = 1

        self.size = size

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = [[0] * self.cols for i in range(self.rows)]
        if randomize:
            for i, row in enumerate(grid):
                for j, _ in enumerate(row):
                    grid[i][j] = random.randint(0, 1)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        pos_row, pos_col = cell
        for i in range(pos_row - 1, pos_row + 2):
            for j in range(pos_col - 1, pos_col + 2):
                if 0 <= i < self.rows and 0 <= j < self.cols and (pos_row, pos_col) != (i, j):
                    neighbours.append(self.curr_generation[i][j])
        return neighbours

    def get_next_generation(self) -> Grid:
        next_generation = self.create_grid()
        for i, row in enumerate(next_generation):
            for j, _ in enumerate(row):
                neighbours = self.get_neighbours((i, j))
                sum_neigh = sum(neighbours)
                if self.curr_generation[i][j] == 1:
                    if sum_neigh == 2 or sum_neigh == 3:
                        next_generation[i][j] = 1
                    else:
                        next_generation[i][j] = 0
                else:
                    if sum_neigh == 3:
                        next_generation[i][j] = 1
        return next_generation

    def step(self) -> None:
        if not self.is_max_generations_exceeded and self.is_changing:
            self.prev_generation = self.curr_generation
            self.curr_generation = self.get_next_generation()
            self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        return self.max_generations is not None and self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        with open(filename, "rb") as f:
            file = f.readlines()
            grid = []
            for _, row in enumerate(file):
                if (49 in row) or (48 in row):
                    rw = []
                for _, val in enumerate(row):
                    if val == 49 or val == 48:
                        rw.append(int(chr(val)))
                grid.append(rw)
            print(grid)
            game = GameOfLife((len(grid), len(grid[0])), randomize=False)
            game.curr_generation = grid
            return game
        f.close()

    def save(self, filename: pathlib.Path) -> None:
        try:
            with open(filename, "w") as f:
                for _, row in enumerate(self.curr_generation):
                    for _, val in enumerate(row):
                        f.write(str(val) + " ")
                    f.write("\n")
            f.close()
        except Exception as e:
            print("Error saving file", e)
