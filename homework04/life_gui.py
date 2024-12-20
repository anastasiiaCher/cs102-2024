import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):
    """GUI using pygame lib"""

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size
        self.cell_size = cell_size

        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)

        self.speed = speed

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for row_position, row in enumerate(self.life.curr_generation):
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

    def run(self) -> None:
        """Запустить игру"""
        # pylint: disable=no-member
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        self.life.curr_generation = self.life.create_grid(randomize=True)

        paused = False
        running = True
        while running:
            for event in pygame.event.get():
                # pylint: disable=undefined-variable
                if event.type == QUIT:
                    running = False
                # pylint: disable=undefined-variable
                if event.type == KEYDOWN:
                    # pylint: disable=undefined-variable
                    if event.key == K_SPACE:
                        paused ^= True
                        print("Pause toggled")
                # pylint: disable=undefined-variable
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and paused:
                        x, y = event.pos
                        x //= self.cell_size
                        y //= self.cell_size
                        self.life.curr_generation[y][x] ^= True
                        self.draw_grid()
                        self.draw_lines()
                        pygame.display.flip()
            if paused:
                continue
            self.life.step()
            # Отрисовка списка клеток
            self.draw_grid()
            self.draw_lines()
            # Выполнение одного шага игры (обновление состояния ячеек)

            pygame.display.flip()
            clock.tick(self.speed)
        # pylint: disable=no-member
        pygame.quit()
