""" "Game of Life" game implementation based on suggestions from the course """

import pathlib
import random
import typing as tp

import pygame

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    """Creating Game of Life class"""
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        self.cell_size = 10
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        """Creating a grid"""
        if not randomize:
            grid = [[0] * self.cols for _ in range(self.rows)]
        else:
            grid = [[random.randint(0, 1) for _ in range(self.cols)] for _ in range(self.rows)]
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        """Getting the condition of neighbours"""
        x, y = cell
        neib_cells = []
        for i in range(max(0, x - 1), min(self.rows, x + 2)):
            for j in range(max(0, y - 1), min(self.cols, y + 2)):
                if i == x and j == y:
                    continue
                neib_cells.append(self.curr_generation[i][j])
        return neib_cells

    def get_next_generation(self) -> Grid:
        """Getting the next generation"""
        new_grid = [[0] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                neib_cells = self.get_neighbours((i, j))
                alive_neibs = sum(neib_cells)
                if self.curr_generation[i][j] == 0 and alive_neibs == 3:
                    new_grid[i][j] = 1
                elif self.curr_generation[i][j] == 1:
                    if 2 <= alive_neibs <= 3:
                        new_grid[i][j] = 1
        return new_grid

    def step(self) -> None:
        """
        Perform one step of the game.
        """
        if not self.is_max_generations_exceeded:
            self.prev_generation = self.curr_generation
            self.curr_generation = self.get_next_generation()
            if self.is_changing:
                self.generations += 1
        else:
            pygame.quit() # pylint: disable=no-member

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.max_generations is not None and self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, encoding='utf-8') as f:
            grid = [[int(cell) for cell in line] for line in f]
        return GameOfLife((len(grid), len(grid[0])))

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w", encoding='utf-8') as f:
            for line in self.curr_generation:
                f.write("".join(str(cell) for cell in line))
