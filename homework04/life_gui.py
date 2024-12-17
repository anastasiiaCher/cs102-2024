"""GameOfLife GUI version"""

import pygame
from pygame import QUIT

from life import GameOfLife
from ui import UI


class GUI(UI):
    """The Game of Life"""

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)

        self.speed = speed
        self.cell_size = cell_size
        self.cell_width = self.life.cols
        self.cell_height = self.life.rows
        self.width = self.cell_size * self.cell_width
        self.height = self.cell_size * self.cell_height
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.grid = self.life.curr_generation

    def draw_lines(self) -> None:
        """Draw lines"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """Draw grid"""
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                x, y = j * self.cell_size + 1, i * self.cell_size + 1
                rect_cor = (x, y, self.cell_size - 1, self.cell_size - 1)
                if self.life.curr_generation[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 255, 0), rect_cor)
                if self.life.curr_generation[i][j] == 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), rect_cor)

    def run(self) -> None:
        """The running game"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        paused = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # pylint: disable=no-member
                    running = False
                if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                    if event.key == pygame.K_p:  # Pausing  # pylint: disable=no-member
                        paused = True
                    if event.key == pygame.K_u:  # Unpausing    # pylint: disable=no-member
                        paused = False
                mouse_pos = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if click != (0, 0, 0) and paused:
                    x, y = mouse_pos[0] // self.cell_size, mouse_pos[1] // self.cell_size
                    if self.life.curr_generation[y][x] == 1:
                        self.life.curr_generation[y][x] = 0
                    else:
                        self.life.curr_generation[y][x] = 1

            self.draw_grid()
            self.draw_lines()
            if not paused:
                self.life.step()
                clock.tick(self.speed)
            pygame.display.flip()

        pygame.quit()  # pylint: disable=no-member


if __name__ == "__main__":
    game_of_life = GameOfLife(size=(50, 90), randomize=True)
    ui = GUI(game_of_life, cell_size=15, speed=10)
    ui.run()
