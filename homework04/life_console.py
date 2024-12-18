import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.border()
        screen.refresh()

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for x, row in enumerate(self.life.curr_generation):
            for y, val in enumerate(row):
                if val == 1:
                    screen.addch(x + 1, y + 1, "■")
        screen.refresh()

    def run(self) -> None:
        screen = curses.initscr()
        x,y = screen.getmaxyx()
        win = curses.newwin(self.life.rows + 2, self.life.cols + 2, (x - self.life.rows) // 2 - 1, (y - self.life.cols) // 2 - 1)

        win.nodelay(True)
        curses.noecho()

        self.draw_borders(win)

        key = 0
        is_paused = False

        while True: 
            key = win.getch()

            if key == ord('q'):
                break
            if key == ord('p'):
                is_paused = not is_paused
            if key == ord('s'):
                self.life.save("save")
            if key == ord('l'):
                self.life = self.life.from_file("save")

            curses.napms(100)

            if is_paused: continue
            if self.life.is_max_generations_exceeded: break
            if not self.life.is_changing: break

            self.life.step()

            win.clear()
            self.draw_borders(win)
            self.draw_grid(win)



        curses.endwin()
