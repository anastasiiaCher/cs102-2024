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
            key = screen.getch()
            if key == ord("q"):
                running = False
                break
            if self.life.generations == self.life.max_generations:
                running = False
                break
        curses.endwin()
