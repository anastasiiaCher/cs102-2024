"""Console version of the game LIFE"""

import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border(0)

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        height, width = screen.getmaxyx()
        for i, row in enumerate(self.life.curr_generation):
            for j, val in enumerate(row):
                if 0 < i < height - 1 and 0 < j < width - 1:
                    ch = " "
                    if val == 1:
                        ch = "1"
                    screen.addch(i, j, ch)

    def run(self) -> None:
        screen = curses.initscr()
        curses.curs_set(0)
        running = True
        while running == True:
            screen.clear()

            self.draw_borders(screen)
            self.draw_grid(screen)
            screen.refresh()

            self.life.step()

            if self.life.is_max_generations_exceeded:
                screen.addstr(0, 0, "Max generations exceeded")
                screen.refresh()
            if not self.life.is_changing:
                screen.addstr(0, 0, "Nothing changing")
                screen.refresh()

            key = screen.getch()

            if key == ord("q"):
                running = False
                break
        curses.endwin()


life = GameOfLife((24, 80), max_generations=50)
ui = Console(life)
ui.run()
