""" Module containing class for handling GameOfLife """

import random
import typing as tp

import pygame

# pylint: disable=wildcard-import
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


# pylint: disable=too-many-instance-attributes
class GameOfLife:
    """Class that handles Game of Life processes"""

    # pylint: disable=line-too-long
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid: Grid

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру"""
        # pylint: disable=no-member
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        self.grid = self.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Отрисовка списка клеток
            self.draw_grid()
            self.draw_lines()
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.grid = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        # pylint: disable=no-member
        pygame.quit()

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
        # pylint: disable=line-too-long
        return [[random.randint(0, randomize) for _ in range(self.cell_width)] for _ in range(self.cell_height)]

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """

        for row_position, row in enumerate(self.grid):
            for element_position, element in enumerate(row):
                pygame.draw.rect(
                    self.screen,
                    Color("green" if element else "white"),
                    Rect(
                        element_position * self.cell_size,
                        row_position * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )

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
            Список соседних клеток, в котором каждая позиция – 0 или 1.
        """
        y, x = cell
        return [
            self.grid[i][j]
            for i in range(max(y - 1, 0), min(y + 1, self.cell_height - 1) + 1)
            for j in range(max(x - 1, 0), min(x + 1, self.cell_width - 1) + 1)
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

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                match cell:
                    case 0:
                        new_grid[y][x] = sum(self.get_neighbours((y, x))) == 3
                    case 1:
                        new_grid[y][x] = sum(self.get_neighbours((y, x))) in (2, 3)
        return new_grid
