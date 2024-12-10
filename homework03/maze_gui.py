import tkinter as tk
from tkinter import messagebox, ttk
from typing import List, Union

from maze import (add_path_to_grid, bin_tree_maze, encircled_exit, get_exits,
                  solve_maze)


# pylint: disable=possibly-used-before-assignment
def draw_cell(x, y, color, size: int = 10):
    """Draws a single cell"""
    x *= size
    y *= size
    x1 = x + size
    y1 = y + size
    canvas.create_rectangle(x, y, x1, y1, fill=color)


# pylint: disable=possibly-used-before-assignment
def draw_maze(grid: List[List[Union[str, int]]], size: int = 10):
    """Draws a cell field based on grid"""
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell in (" ", 0):
                color = "White"
            elif cell == "■":
                color = "black"
            elif cell == "X":
                color = "teal"
            draw_cell(y, x, color, size)


def show_solution():
    """Display the found solution on the canvas"""
    maze, path = solve_maze(GRID)
    maze = add_path_to_grid(GRID, path)
    if path:
        draw_maze(maze, CELL_SIZE)
    else:
        messagebox.showinfo("Message", "No solutions")


if __name__ == "__main__":
    global GRID, CELL_SIZE
    N, M = 51, 77

    CELL_SIZE = 10
    GRID = bin_tree_maze(N, M)

    while any(encircled_exit(GRID, e) for e in get_exits(GRID)):
        GRID = bin_tree_maze(N, M)

    window = tk.Tk()
    window.title("Maze")
    window.geometry("%dx%d" % (M * CELL_SIZE + 100, N * CELL_SIZE + 100))

    canvas = tk.Canvas(window, width=M * CELL_SIZE, height=N * CELL_SIZE)
    canvas.pack()

    draw_maze(GRID, CELL_SIZE)
    ttk.Button(window, text="Solve", command=show_solution).pack(pady=20)

    window.mainloop()
