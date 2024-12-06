"""
Модуль для решения лабиринта
"""

from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(
    grid: List[List[Union[str, int]]], coord: Tuple[int, int]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """

    x, y, len_col, len_row = coord[0], coord[1], len(grid) - 1, len(grid[0]) - 1
    directions = ["up", "right"]
    direction = choice(directions)
    if (direction == "up") and ((0 <= x - 2 < len_col) and (0 <= y < len_row)):
        grid[x - 1][y] = " "
    else:
        direction = "right"
    if (direction == "right") and ((0 <= x < len_col) and (0 <= y + 2 < len_row)):
        grid[x][y + 1] = " "
    elif (direction == "right") and ((0 <= x - 2 < len_col) and (0 <= y < len_row)):
        grid[x - 1][y] = " "
    return grid


def bin_tree_maze(
    rows: int = 15, cols: int = 15, random_exit: bool = True
) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    while empty_cells:
        x, y = empty_cells.pop(0)
        remove_wall(grid, (x, y))
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = (
            randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
        )
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """

    return [
        (x, y)
        for x, row in enumerate(grid)
        for y, if_exit in enumerate(row)
        if if_exit == "X"
    ]


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """

    coords = [
        (x, y)
        for x, row in enumerate(grid)
        for y, _ in enumerate(row)
        if grid[x][y] == k
    ]

    k += 1
    for i in coords:
        selected_coord = i
        near_to = [
            (selected_coord[0] - 1, selected_coord[1]),
            (selected_coord[0] + 1, selected_coord[1]),
            (selected_coord[0], selected_coord[1] - 1),
            (selected_coord[0], selected_coord[1] + 1),
        ]
        new_coords = [(x, y) for x, row in enumerate(grid) for y, _ in enumerate(row)]
        for x, y in new_coords:
            if (x, y) in near_to and grid[x][y] == 0:
                grid[x][y] = k
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    selected_coord, k, len_of_path = (
        exit_coord,
        grid[exit_coord[0]][exit_coord[1]],
        grid[exit_coord[0]][exit_coord[1]],
    )
    coords = [(x, y) for x, row in enumerate(grid) for y, _ in enumerate(row)]
    path = [selected_coord]

    while grid[selected_coord[0]][selected_coord[1]] != 1:
        near_to = [
            (selected_coord[0] - 1, selected_coord[1]),
            (selected_coord[0] + 1, selected_coord[1]),
            (selected_coord[0], selected_coord[1] - 1),
            (selected_coord[0], selected_coord[1] + 1),
        ]
        for x, y in near_to:
            if (x, y) in coords and grid[x][y] == int(k) - 1:
                path.append((x, y))
                selected_coord = (x, y)
                k = int(k) - 1
                break
    if len(path) != len_of_path:
        grid[selected_coord[0]][selected_coord[1]] = " "
        shortest_path(grid, exit_coord)
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """

    x, y, len_row, len_col = coord[0], coord[1], len(grid) - 1, len(grid[0]) - 1
    angles = [(0, 0), (0, len_col), (len_row, 0), (len_row, len_col)]
    if coord in angles:
        return True
    if x in [0, len_row]:
        if (
            grid[x][y - 1] == "■"
            and grid[x][y + 1] == "■"
            and grid[abs(x - 1)][y] == "■"
        ):
            return True
    if y in [0, len_col]:
        if (
            grid[x - 1][y] == "■"
            and grid[x + 1][y] == "■"
            and grid[x][abs(y - 1)] == "■"
        ):
            return True
    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[
    List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
]:
    """

    :param grid:
    :return:
    """

    if len(get_exits(grid)) == 1:
        return grid, get_exits(grid)[0]
    exits = get_exits(grid)
    entrance, ex1t = exits[0], exits[1]
    if encircled_exit(grid, entrance) or encircled_exit(grid, ex1t):
        return grid, None
    grid[entrance[0]][entrance[1]] = 1
    k = 0
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == " " or grid[x][y] == "X":
                grid[x][y] = 0
    while grid[ex1t[0]][ex1t[1]] == 0:
        k += 1
        make_step(grid, k)
    path = shortest_path(grid, ex1t)
    return grid, path


def add_path_to_grid(
    grid: List[List[Union[str, int]]],
    path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]],
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
