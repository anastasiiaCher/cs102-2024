"""Creating console interface"""

import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    """Console creation"""

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border(0)

    def draw_grid(self, screen) -> None:
        """Show the state of cells"""
        max_y, max_x = screen.getmaxyx()
        for i, row in enumerate(self.life.curr_generation):
            for j, cell in enumerate(row):
                if i < max_y and j < max_x:
                    char = "O" if cell else " "
                    screen.addch(i, j, char)

    def run(self) -> None:
        """Run the game"""
        screen = curses.initscr()
        curses.curs_set(0)
        screen.nodelay(True)
        screen.timeout(100)

        try:
            while True:
                screen.clear()
                self.draw_borders(screen)
                self.draw_grid(screen)
                screen.refresh()

                self.life.step()

                key = screen.getch()
                if key == ord("q"):  # Press 'q' to exit
                    break
        finally:
            curses.endwin()
