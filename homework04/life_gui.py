"""Creating GUI interface"""

import sys

import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    """GUI class creation"""

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.width = self.life.cols * self.cell_size
        self.height = self.life.rows * self.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height + 50))
        self.speed = speed
        self.paused = False

        self.pause_button = pygame.Rect(10, self.height + 10, 70, 30)
        self.resume_button = pygame.Rect(90, self.height + 10, 70, 30)

        pygame.font.init()
        self.font = pygame.font.SysFont("Consolas", 16)

    def draw_lines(self) -> None:
        """Draw the grid"""
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

    def draw_console(self) -> None:
        """Draw the buttons with text"""
        pygame.draw.rect(self.screen, pygame.Color("light gray"), self.pause_button, border_radius=10)
        pygame.draw.rect(self.screen, pygame.Color("light gray"), self.resume_button, border_radius=10)

        pause_text = self.font.render("pause", True, pygame.Color("black"))
        resume_text = self.font.render("resume", True, pygame.Color("black"))
        text_surface = self.font.render(f"Generation: {self.life.generations}", True, pygame.Color("Purple"))
        text_instr = self.font.render("press [q] to exit", True, pygame.Color("Red"))

        self.screen.blit(pause_text, (self.pause_button.x + 10, self.pause_button.y + 5))
        self.screen.blit(resume_text, (self.resume_button.x + 5, self.resume_button.y + 5))
        self.screen.blit(text_surface, (self.width - 200, self.height + 10))
        self.screen.blit(text_instr, (self.width - 200, self.height + 30))

    def draw_caution(self, caut_text) -> None:
        """Draw the caution text"""
        caution_text = self.font.render(caut_text, True, pygame.Color("maroon"))
        text_rect = caution_text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(caution_text, text_rect)

    def run(self) -> None:
        """Run the game"""
        pygame.init()  # pylint: disable=no-member
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    running = False
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    self.paused = not self.paused
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    j = x // self.cell_size
                    i = y // self.cell_size
                    if self.pause_button.collidepoint(x, y):
                        self.paused = True
                    elif self.resume_button.collidepoint(x, y):
                        self.paused = False
                    else:
                        self.life.curr_generation[i][j] = 1 if self.life.curr_generation[i][j] == 0 else 0

            self.screen.fill(pygame.Color("white"))
            self.draw_grid()
            self.draw_lines()
            self.draw_console()
            if self.life.is_max_generations_exceeded:
                self.draw_caution("Max generations exceeded")
                self.paused = True
            elif not self.life.is_changing:
                self.draw_caution("No changes in generations")
                self.paused = True
            pygame.display.flip()

            if not self.paused:
                self.life.step()

            clock.tick(self.speed)

        pygame.quit()  # pylint: disable=no-member
        sys.exit()
