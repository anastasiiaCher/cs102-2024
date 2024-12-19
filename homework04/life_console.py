import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.addstr(0, 0, "o" + "-" * self.life.cols + "o")
        screen.addstr(self.life.rows + 1, 0, "o" + "-" * self.life.cols + "o")

        for i in range(1, self.life.rows + 1):
            screen.addstr(i, 0, "|")
            screen.addstr(i, self.life.cols + 1, "|")

        screen.addstr(self.life.rows + 3, 0, "Press 'q' to quit")

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for row in range(self.life.rows):
            for col in range(self.life.cols):
                if self.life.curr_generation[row][col] == 1:
                    screen.addch(row + 1, col + 1, "@")
                else:
                    screen.addch(row + 1, col + 1, " ")

    def wait_for_key(self, screen, message):
        """Ожидание кнопки выхода."""
        screen.addstr(self.life.rows + 5, 0, message)
        while True:
            try:
                key = screen.getkey()
                if key and key.lower() == "q":
                    curses.endwin()
                    break
            except curses.error:
                continue

    def run(self) -> None:
        screen = curses.initscr()
        curses.curs_set(0)
        screen.timeout(100)

        try:
            running = True
            while running:
                screen.clear()
                self.draw_borders(screen)
                self.draw_grid(screen)
                screen.refresh()
                self.life.step()

                screen.addstr(3, self.life.cols + 4, f"Current generation: {self.life.generations}")
                screen.addstr(4, self.life.cols + 4, f"Max generations: {self.life.max_generations}")

                if self.life.is_max_generations_exceeded and not self.life.is_changing:
                    self.wait_for_key(
                        screen, "The Life came to its logical end. Max generations is reached and nothing is changing."
                    )
                    running = False
                elif self.life.is_max_generations_exceeded:
                    self.wait_for_key(screen, "This Life could last much longer... Max generations is reached.")
                    running = False
                elif not self.life.is_changing:
                    self.wait_for_key(screen, "This Life was weak. Nothing is changing.")
                    running = False

                try:
                    key = screen.getkey()
                except curses.error:
                    key = None
                except Exception as e:
                    curses.endwin()
                    print(f"ERROR: {e}")
                    return

                if key and key.lower() == "q":
                    running = False

                time.sleep(0.05)
        finally:
            curses.endwin()


if __name__ == "__main__":
    life_game = GameOfLife((20, 20), max_generations=50)
    ui = Console(life_game)
    ui.run()
