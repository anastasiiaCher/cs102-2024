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
    grid = deepcopy(grid)
    rows, cols = len(grid), len(max(grid, key=len))
    x, y = coord

    right = randint(0,1)
    up = not right
    can_go_up = (x-2 >= 0)
    can_go_right = (y+2 < cols-1)

    match (up, right, can_go_up, can_go_right):
        case (1, 0, 1, _):
            grid[x-1][y] = " "
        case (1, 0, 0, 1):
            grid[x][y+1] = " "
        case (0, 1, _, 1):
            grid[x][y+1] = " "
        case (0, 1, 1, 0):
            grid[x-1][y] = " "
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

    for cell in empty_cells:
        grid = remove_wall(grid, cell)

    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
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
    """
    >>> get_exits([[".", ".", "X"], [".", ".", "."], [".", "X", "."]])
    [(0, 2), (2, 1)]
    """

    return [(x, y.index('X')) for x, y in enumerate(grid) if 'X' in y] 


def get_neighbors(
    grid: List[List[Union[str, int]]], 
    pos: Tuple[int, int]
) -> List[Tuple[int, int]]:
    """ 
    >>> get_neighbors([[".", ".", "."],[".", ".", "."],[".", ".", "."]], (1,0))
    [(0, 0), (1, 1), (2, 0)]
    """
    rows, cols = len(grid), len(max(grid, key=len))
    positions = []
    x, y = pos[0], pos[1]
    if x > 0:
        positions.append((x-1, y))
    if x < rows-1:
        positions.append((x+1, y))
    if y > 0:
       positions.append((x, y-1))
    if y < cols-1:
        positions.append((x, y+1))
    return sorted(positions)


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    grid = deepcopy(grid)
    rows, cols = len(grid), len(max(grid, key=len))
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == k:
                for i, j in get_neighbors(grid, (x, y)):
                    if grid[i][j] == 0:
                        grid[i][j] = k + 1
    return grid

def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    path = []
    cursor = exit_coord
    
    while True:
        path.append(cursor)
        cells = [
            c for c in get_neighbors(grid, cursor) 
            if isinstance(grid[c[0]][c[1]], int)
            and grid[c[0]][c[1]] == grid[cursor[0]][cursor[1]] - 1
        ]
        if not cells:
            break
        cursor = cells[0]

    if len(path) != grid[exit_coord[0]][exit_coord[1]]:
        grid[path[1][0]][path[1][1]] = " "
        return shortest_path(grid, exit_coord)
    
    return path #or cursor


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    rows, cols = len(grid), len(max(grid, key=len))
    return not (any(grid[x][y] in " X" for x, y in get_neighbors(grid, coord)) or grid[coord[0]][coord[1]] == " ")


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """
    exits = get_exits(grid)
    if len(exits) == 1:
        return (grid, exits[0])
    if encircled_exit(grid, exits[0]) or encircled_exit(grid, exits[1]):
        return (grid, None)
    
    for x, _ in enumerate(grid):
        for y, v in enumerate(_):
            if v in " X":
                grid[x][y] = 0
    grid[exits[0][0]][exits[0][1]] = 1

    k = 1
    while grid[exits[1][0]][exits[1][1]] == 0:
        grid = make_step(grid, k)
        k += 1

    return (grid, shortest_path(grid, exits[1]))
    

def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
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
                    grid[i][j] = "#"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
