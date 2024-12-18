import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.width = life.cols * cell_size
        self.height = life.rows * cell_size
        self.cell_size = cell_size
        self.speed = speed

        # Устанавливаем размер окна
        self.screen_size = self.width, self.height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for x, row in enumerate(self.life.curr_generation):
            for y, val in enumerate(row):
                if val == 1:
                    pygame.draw.rect(self.screen, pygame.Color("green"),(y * self.cell_size + 1, x * self.cell_size + 1, self.cell_size - 1,  self.cell_size - 1))
                else: 
                    pygame.draw.rect(self.screen, pygame.Color("white"),(y * self.cell_size + 1, x * self.cell_size + 1, self.cell_size - 1,  self.cell_size - 1))
    
    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        is_paused = False

        # Создание списка клеток
        self.life.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                if event.type == KEYDOWN:
                    if event.key == K_p or event.key == K_SPACE:
                        is_paused = not is_paused
                    if event.key == K_ESCAPE or event.key == K_q:
                        running = False
                    if event.key == K_s:
                        self.life.save("save")
                    if event.key == K_l:
                        self.life = self.life.from_file("save")

                if event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    row = mouse_y // self.cell_size
                    col = mouse_x // self.cell_size

                    self.life.curr_generation[row][col] = 1 - self.life.curr_generation[row][col]
                    self.draw_grid()
                    pygame.display.flip()

            if is_paused:
                continue

            self.draw_lines()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)

            self.life.step()
            self.draw_grid()

            if self.life.is_max_generations_exceeded or not self.life.is_changing:
                break

            pygame.display.flip()
            clock.tick(self.speed)


        pygame.quit()
