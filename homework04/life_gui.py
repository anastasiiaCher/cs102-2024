"""Creating GUI interface"""

import sys

import pygame
from pygame.locals import K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT

from life import GameOfLife
from ui import UI


class GUI(UI):
    """GUI class creation"""

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.width = self.life.cols * self.cell_size
        self.height = self.life.rows * self.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.speed = speed
        self.paused = False

    def draw_lines(self) -> None:
        """Draw the greed"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("gray"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("gray"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """Draw the state of cells"""
        for i, row in enumerate(self.life.curr_generation):
            for j, cell in enumerate(row):
                color = pygame.Color("green") if cell else pygame.Color("white")
                pygame.draw.rect(
                    self.screen, color, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                )

    def run(self) -> None:
        """Run the game"""
        pygame.init()  # pylint: disable=no-member
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        running = True
        try:
            while running:
                for event in pygame.event.get():
                    if event.type == QUIT:  # pylint: disable=no-name-in-module
                        running = False
                    elif event.type == KEYDOWN and event.key == K_SPACE:  # pylint: disable=no-name-in-module
                        self.paused = not self.paused
                    elif event.type == MOUSEBUTTONDOWN:  # pylint: disable=no-name-in-module
                        x, y = event.pos
                        j = x // self.cell_size
                        i = y // self.cell_size
                        self.life.curr_generation[i][j] = 1 if self.life.curr_generation[i][j] == 0 else 0

                self.screen.fill(pygame.Color("white"))
                self.draw_grid()
                self.draw_lines()
                pygame.display.flip()

                if not self.paused:
                    self.life.step()

                clock.tick(self.speed)
        finally:
            pygame.quit()  # pylint: disable=no-member
            sys.exit()
