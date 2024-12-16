import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size * 2
        self.speed = speed

        # Вычисляем ширину и высоту окна
        self.width = self.life.cols * self.cell_size
        self.height = self.life.rows * self.cell_size

        # Создаем кнопки паузы и перезапуска
        self.pause_button = pygame.Rect(self.width + 10, 10, 100, 30)
        self.restart_button = pygame.Rect(self.width + 10, self.pause_button.y + 40, 100, 30)

        # Устанавливаем размер окна
        self.screen_size = self.width + 120, self.height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_lines(self) -> None:
        """Отрисовка сетки"""
        for x in range(0, self.width + self.cell_size, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                if self.life.curr_generation[i][j]:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("green"),
                        (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size),
                    )
                else:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("white"),
                        (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size),
                    )

    def draw_buttons(self) -> None:
        """Отрисовать кнопку паузы"""
        pygame.draw.rect(self.screen, pygame.Color("grey"), self.pause_button)
        pygame.draw.rect(self.screen, pygame.Color("grey"), self.restart_button)
        font = pygame.font.SysFont(None, 24)
        text_pause = font.render("Pause", True, pygame.Color("black"))
        text_restart = font.render("Restart", True, pygame.Color("black"))
        self.screen.blit(text_pause, (self.pause_button.x + 25, self.pause_button.y + 8))
        self.screen.blit(text_restart, (self.restart_button.x + 20, self.restart_button.y + 8))

    def show_message(self, message) -> None:
        """Вывод сообщения о завершении игры"""
        font_size = max(10, int(min(self.height, self.width) * 0.1))
        font = pygame.font.Font(None, font_size)
        text = font.render(message, True, pygame.Color("red"))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        running = True
        paused = False

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if self.pause_button.collidepoint(event.pos):
                        paused = not paused
                    elif self.restart_button.collidepoint(event.pos):
                        self.life.curr_generation = self.life.create_grid(randomize=True)
                        self.life.generations = 0
                        self.draw_grid()
                        self.draw_lines()
                    elif paused:
                        # Получаем координаты клика мыши
                        x, y = event.pos
                        # Вычисляем ячейку, внутри которой был клик
                        cell_x = x // self.cell_size
                        cell_y = y // self.cell_size
                        # Если координаты x и y лежат внутри нашей сетки, то изменяем состояние клетки на противоположное
                        if 0 <= cell_x < self.life.cols and 0 <= cell_y < self.life.rows:
                            self.life.curr_generation[cell_y][cell_x] = not self.life.curr_generation[cell_y][cell_x]
                            # Отрисовываем сетку, чтобы изменения отобразились на экране
                            self.draw_grid()
                            self.draw_lines()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        paused = not paused

            # Отрисовка списка клеток и линий
            self.draw_grid()
            self.draw_lines()
            # Отрисовка кнопок паузы и перезапуска
            self.draw_buttons()

            # Выполнение одного шага игры
            if not paused:
                self.life.step()

            # Проверяем условия окончания игры
            if self.life.is_max_generations_exceeded or not self.life.is_changing:
                if self.life.is_max_generations_exceeded:
                    self.show_message("Превышено максимальное количество поколений!")
                if not self.life.is_changing:
                    self.show_message("Получена стабильная комбинация!")
                running = False  # Останавливаем игру

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == "__main__":
    life = GameOfLife((24, 32))
    game = GUI(life)
    game.run()
