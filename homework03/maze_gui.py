"""Visualisation of maze"""

import tkinter as tk
from copy import deepcopy
from tkinter import messagebox, ttk
from typing import List

from maze import add_path_to_grid, bin_tree_maze, solve_maze


def draw_cell(x, y, color, size: int = 10):
    """Draw cell"""
    x *= size
    y *= size
    x1 = x + size
    y1 = y + size
    canvas.create_rectangle(x, y, x1, y1, fill=color)


def draw_maze(grid: List[List[str]], size: int = 10):
    """Draw maze"""
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == " ":
                color = "White"
            elif cell == "■":
                color = "black"
            elif cell == "X":
                color = "blue"
            draw_cell(y, x, color, size)


def show_solution():
    """Show solution"""
    maze, path = solve_maze(GRID)
    maze = add_path_to_grid(GRID, path)
    if path:
        draw_maze(maze, CELL_SIZE)
    else:
        tk.messagebox.showinfo("Message", "No solutions")


def is_solvable(n: int, m: int):
    """Generating solvable grid"""
    while True:
        grid = bin_tree_maze(n, m)
        copied_greed = deepcopy(grid)
        _, path = solve_maze(copied_greed)
        if path:
            return grid


if __name__ == "__main__":
    global GRID, CELL_SIZE
    N, M = 51, 77

    CELL_SIZE = 10
    GRID = is_solvable(N, M)

    window = tk.Tk()
    window.title("Maze")
    window.geometry("%dx%d" % (M * CELL_SIZE + 100, N * CELL_SIZE + 100))

    canvas = tk.Canvas(window, width=M * CELL_SIZE, height=N * CELL_SIZE)
    canvas.pack()

    draw_maze(GRID, CELL_SIZE)
    ttk.Button(window, text="Solve", command=show_solution).pack(pady=20)

    window.mainloop()
