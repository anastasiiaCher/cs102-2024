import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.width = self.life.cols * self.cell_size
        self.height = self.life.rows * self.cell_size
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.speed = speed

        self.button = pygame.Rect(0, 0, 150, 50)

        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

        self.status = False

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for i, row in enumerate(self.life.curr_generation):
            for j, val in enumerate(row):
                if val == 1:
                    for x in range(i * self.cell_size, (i + 1) * self.cell_size):
                        pygame.draw.line(
                            self.screen, pygame.Color("purple"), (j * self.cell_size, x), ((j + 1) * self.cell_size, x)
                        )
                else:
                    for x in range(i * self.cell_size, (i + 1) * self.cell_size + 1):
                        pygame.draw.line(
                            self.screen, pygame.Color("white"), (j * self.cell_size, x), ((j + 1) * self.cell_size, x)
                        )

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.button.collidepoint(mouse_pos) and self.status is False:
                    self.status = True
                elif self.button.collidepoint(mouse_pos) and self.status is True:
                    self.status = False

            self.draw_lines()
            if self.status is False:
                self.draw_grid()
                self.draw_lines()
                self.life.step()

                pygame.draw.rect(self.screen, pygame.Color("light gray"), self.button, border_radius=10)
                pause_text = self.font.render("pause", True, pygame.Color("black"))
                self.screen.blit(pause_text, (38, 13))
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    pos_y = mouse_pos[0] // self.cell_size
                    pos_x = mouse_pos[1] // self.cell_size

                    if self.life.curr_generation[pos_x][pos_y] == 1:
                        self.life.curr_generation[pos_x][pos_y] = 0
                    else:
                        self.life.curr_generation[pos_x][pos_y] = 1

                    self.draw_grid()
                    self.draw_lines()

                pygame.draw.rect(self.screen, pygame.Color("dark gray"), self.button, border_radius=10)
                resume_text = self.font.render("resume", True, pygame.Color("black"))
                self.screen.blit(resume_text, (35, 13))

            if self.life.is_max_generations_exceeded:
                error_max_generation = self.font.render("Max generations exceeded", True, pygame.Color("red"))
                self.screen.blit(error_max_generation, (self.width // 4, self.height // 2))
            if not self.life.is_changing:
                error_changing = self.font.render("Nothing changing", True, pygame.Color("red"))
                self.screen.blit(error_changing, (self.width // 4, self.height // 2))

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


life = GameOfLife((24, 80), max_generations=500)
ui = GUI(life)
ui.run()
