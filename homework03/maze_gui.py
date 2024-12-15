import tkinter as tk
from copy import deepcopy
from tkinter import ttk
from typing import List

from maze import add_path_to_grid, bin_tree_maze, solve_maze


def draw_cell(x, y, color, size: int = 10):
    x *= size
    y *= size
    x1 = x + size
    y1 = y + size
    canvas.create_rectangle(x, y, x1, y1, fill=color)


def draw_maze(grid: List[List[str | int]], size: int = 10):
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == " ":
                color = "White"
            elif cell == "■":
                color = "black"
            elif cell == "X":
                color = "#7FFFD4"
            draw_cell(y, x, color, size)


def show_solution():
    new_grid = deepcopy(GRID)
    new_grid, path = solve_maze(new_grid)
    maze = add_path_to_grid(new_grid, path)
    draw_maze(maze, CELL_SIZE)


def solvable_maze(grid: List[List[str | int]]) -> bool:
    new_grid = deepcopy(grid)
    _, path = solve_maze(new_grid)
    return bool(path)


if __name__ == "__main__":
    global GRID, CELL_SIZE
    N, M = 51, 77

    CELL_SIZE = 10
    GRID = bin_tree_maze(N, M)

    if not solvable_maze(GRID):
        print("Maze is not solvable, so let's regenerate it")
        GRID = bin_tree_maze(N, M)

    print("Maze is solvable")

    window = tk.Tk()
    window.title("Maze")
    window.geometry("%dx%d" % (M * CELL_SIZE + 100, N * CELL_SIZE + 100))

    canvas = tk.Canvas(window, width=M * CELL_SIZE, height=N * CELL_SIZE)
    canvas.pack()

    draw_maze(GRID, CELL_SIZE)
    ttk.Button(window, text="Solve", command=show_solution).pack(pady=20)

    window.mainloop()
