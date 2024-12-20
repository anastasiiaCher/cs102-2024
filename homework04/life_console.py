import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.border(0)

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        max_y, max_x = screen.getmaxyx()
        for y, row in enumerate(self.life.curr_generation):
            for x, cell in enumerate(row):
                if y < max_y and x < max_x:
                    screen.addch(y, x, "#" if cell else ".")

    def run(self) -> None:
        screen = curses.initscr()
        screen.nodelay(True)

        while self.life.is_changing and not self.life.is_max_generations_exceeded:

            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            screen.refresh()

            self.life.step()
            
            key = screen.getch()
            if key == ord("q"):
                break
            
        curses.endwin()
