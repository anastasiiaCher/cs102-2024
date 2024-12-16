import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отображение рамки"""
        height, width = self.life.rows + 2, self.life.cols + 2

        # Углы
        screen.addch(0, 0, "/")
        screen.addch(0, width - 1, "\\")
        screen.addch(height - 1, 0, "\\")
        screen.addch(height - 1, width - 1, "/")

        # Горизонтальные линии
        for x in range(1, width - 1):
            screen.addch(0, x, "-")
            screen.addch(height - 1, x, "-")

        # Вертикальные линии
        for y in range(1, height - 1):
            screen.addch(y, 0, "|")
            screen.addch(y, width - 1, "|")
        screen.addstr("\n")

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        grid = self.life.curr_generation
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                if grid[i][j]:
                    screen.addch(i + 1, j + 1, "*")
                else:
                    screen.addch(i + 1, j + 1, " ")

    def run(self) -> None:
        screen = curses.initscr()
        screen.nodelay(True)
        while True:
            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            screen.addstr(self.life.rows + 3, 0, "Press [Q] to quit")
            # Выполняем один шаг игры если еще не получена устойчивая комбинация и не превышено заданное число поколений
            if not self.life.is_max_generations_exceeded and self.life.is_changing:
                self.life.step()
            elif self.life.is_max_generations_exceeded:
                screen.addstr(
                    self.life.rows + 4, 0, "The game has stopped because the number of generations has been exceeded"
                )
            elif not self.life.is_max_generations_exceeded and not self.life.is_changing:
                screen.addstr(self.life.rows + 5, 0, "The game is stopped because a stable combination was obtained")
            try:
                key = screen.getkey()
            except Exception:
                key = None
            if key and key.lower() == "q":
                break

            time.sleep(0.1)
            screen.refresh()


if __name__ == "__main__":
    life = GameOfLife((24, 80), max_generations=50)
    ui = Console(life)
    ui.run()
