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

    direction = randint(0,1)

    if(coord[0] == 1 and coord[1] == len(grid[0]) - 2):
        return grid
    
    if(coord[0] == 1):
        direction = 1
    if(coord[1] == len(grid[0]) - 2):
        direction = 0
    
    if(direction == 0):
        grid[coord[0] - 1][coord[1]] = " "
    else: grid[coord[0]][coord[1] + 1] = " "
    
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

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

    for x in range (1, len(grid), 2):
        for y in range(1, len(grid[0]),2):
            grid = remove_wall(grid, [x,y])

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

    exits = []

    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val == 'X':
                exits.append((x,y))
    
    return exits



def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """

    
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if (val == k):
                try:
                    if (grid[x][y + 1] == 0):
                        grid[x][y + 1] = k + 1
                except Exception: pass
                try:
                    if (grid[x][y - 1] == 0):
                        grid[x][y - 1] = k + 1
                except Exception: pass
                try:
                    if (grid[x + 1][y] == 0):
                        grid[x + 1][y] = k + 1
                except Exception: pass
                try:
                    if (grid[x - 1][y] == 0):
                        grid[x - 1][y] = k + 1
                except Exception: pass
                

    return grid

def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """

    x, y = exit_coord
    k = grid[x][y]
    exit_path = []
    exit_path.append(exit_coord)

    while(k > 1):
        try:
            if (grid[x + 1][y] == k - 1):
                x = x + 1
                k = k - 1
                exit_path.append((x,y))
                continue
        except Exception: pass
        try:
            if (grid[x - 1][y] == k - 1):
                x = x - 1
                k = k - 1
                exit_path.append((x,y))
                continue
        except Exception: pass
        try:
            if (grid[x][y + 1] == k - 1):
                y = y + 1
                k = k - 1
                exit_path.append((x,y))
                continue
        except Exception: pass
        try:
            if (grid[x][y - 1] == k - 1):
                y = y - 1
                k = k - 1
                exit_path.append((x,y))
                continue
        except Exception: pass

    return exit_path

def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """

    x, y = coord
    try:
        if ( grid[x][y + 1] != '■'):
            return False
    except Exception: pass
    try:
        if ( grid[x][y - 1] != '■'):
            return False
    except Exception: pass
    try:
        if ( grid[x + 1][y] != '■'):
            return False
    except Exception: pass
    try:
        if ( grid[x - 1][y] != '■'):
            return False
    except Exception: pass
    
    if (x != 0 and x != len(grid) - 1 and y != 0 and y != len(grid[0]) - 1):
        return False
    else:
        return True

def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """

    exits = get_exits(grid)

    if (len(exits) == 1):
        return grid, exits[0]
    
    for exit in exits:
        if encircled_exit(grid, exit):
            return grid, None
        
    
    new_grid = deepcopy(grid)

    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if (val == ' '):
                new_grid[x][y] = 0

    in_x, in_y = exits[0]
    out_x, out_y = exits[1]

    new_grid[in_x][in_y] = 1
    new_grid[out_x][out_y] = 0
    k = 1

    while (new_grid[out_x][out_y] == 0):
        new_grid = make_step(new_grid, k)
        k += 1

    exit_path = shortest_path(new_grid, exits[1])

    return grid, exit_path

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
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
