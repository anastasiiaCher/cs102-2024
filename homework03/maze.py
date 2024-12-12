"""MAZE"""

from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    """Create a grid filled with walls."""
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> None:
    """Remove wall between two cells."""
    x, y = coord
    grid[x][y] = " "


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
    """Generate a maze using the Binary Tree algorithm."""
    grid = create_grid(rows, cols)
    empty_cells = []
    for x in range(rows):
        for y in range(cols):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))
                if x + 1 < rows:
                    if choice([True, False]):
                        remove_wall(grid, (x + 1, y))
                if y + 1 < cols:
                    if choice([True, False]):
                        remove_wall(grid, (x, y + 1))
    if random_exit:
        x_in, y_in = 0, randint(1, cols - 2)
        x_out, y_out = rows - 1, randint(1, cols - 2)
    else:
        x_in, y_in = 0, cols // 2
        x_out, y_out = rows - 1, cols // 2
    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"
    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """Get all exit points from the maze."""
    exits = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                exits.append((i, j))
    return exits


def shortest_path(
    grid: List[List[Union[str, int]]], start: Tuple[int, int], exit_coord: Tuple[int, int]
) -> Optional[List[Tuple[int, int]]]:
    """Find the shortest path using BFS."""
    from collections import deque

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == exit_coord:
            return path

        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "■" and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None


def solve_maze(
    grid: List[List[Union[str, int]]]
) -> Tuple[List[List[Union[str, int]]], Optional[List[Tuple[int, int]]]]:
    """Solve the maze."""
    starts = [(0, y) for y in range(len(grid[0])) if grid[0][y] == "X"]
    exits = get_exits(grid)
    if not starts or not exits:
        return grid, None
    for start in starts:
        for exit_coord in exits:
            if start != exit_coord:
                path = shortest_path(grid, start, exit_coord)
                if path:
                    return add_path_to_grid(grid, path), path
    return grid, None


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[List[Tuple[int, int]]]
) -> List[List[Union[str, int]]]:
    """Add the path to the grid."""
    if path:
        for i, j in path:
            grid[i][j] = "."
    return grid


if __name__ == "__main__":
    GRID = bin_tree_maze(15, 15)
    print("Unsolved Maze:")
    print(pd.DataFrame(GRID))
    SOLVED_GRID, PATH = solve_maze(GRID)
    print("\nSolved Maze:")
    MAZE = add_path_to_grid(deepcopy(GRID), PATH)
    print(pd.DataFrame(MAZE))
