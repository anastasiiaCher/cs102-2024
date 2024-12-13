from copy import deepcopy
from random import choice, randint, random
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """
    x, y, len_row = coord[0], coord[1], len(grid[0]) - 1
    directions = ["up", "rt"]
    direction = choice(directions)
    if direction == "up" and 0 < x - 1:
        grid[x - 1][y] = " "
    else:
        direction = "rt"
    if direction == "rt" and y + 1 < len_row:
        grid[x][y + 1] = " "
    elif direction == "rt" and 0 < x - 1:
        grid[x - 1][y] = " "
    return grid


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
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

    for cell in empty_cells:
        x, y = cell[0], cell[1]
        grid = remove_wall(grid, (x, y))

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

    exits = [(x, y) for x, row in enumerate(grid) for y, _ in enumerate(row) if grid[x][y] == "X"]
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """

    coord = [(x, y) for x, row in enumerate(grid) for y, _ in enumerate(row) if grid[x][y] == k]
    k += 1
    for i in coord:
        coordx, coordy = i[0], i[1]
        coord_near = [
            (x, y)
            for x, row in enumerate(grid)
            for y, _ in enumerate(row)
            if ((abs(x - coordx) == 1) and coordy == y) ^ ((abs(y - coordy) == 1) and coordx == x)
        ]
        for cor in coord_near:
            if grid[cor[0]][cor[1]] == 0:
                grid[cor[0]][cor[1]] = k
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    k: int
    currplace, k = exit_coord, int(grid[exit_coord[0]][exit_coord[1]])
    pathlen = k
    path = [currplace]
    while k != 1:
        coord_near = [
            (x, y)
            for x, row in enumerate(grid)
            for y, _ in enumerate(row)
            if ((abs(x - currplace[0]) == 1) and currplace[1] == y)
            ^ ((abs(y - currplace[1]) == 1) and currplace[0] == x)
        ]
        for x, y in coord_near:
            if grid[x][y] == int(k) - 1:
                path.append((x, y))
                currplace = (x, y)
                k -= 1
                break
    if len(path) != pathlen:
        grid[currplace[0]][currplace[1]] = " "
        shortest_path(grid, exit_coord)
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """

    x, y = coord[0], coord[1]
    angles = [(x, y) for x in range(0, len(grid), len(grid) - 1) for y in range(0, len(grid[0]), len(grid[0]) - 1)]
    if (x, y) in angles:
        return True
    if y in [0, len(grid) - 1]:
        if grid[x][abs(y - 1)] != " ":
            return True
    if x in [0, len(grid) - 1]:
        if grid[abs(x - 1)][y] != " ":
            return True
    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """

    exits = get_exits(grid)
    if len(exits) == 1:
        return grid, exits
    if encircled_exit(grid, exits[0]) or encircled_exit(grid, exits[1]):
        return grid, None
    ent, ex = exits[0], exits[1]
    grid[ent[0]][ent[1]] = 1
    k = 0
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == " " or grid[x][y] == "X":
                grid[x][y] = 0
    while grid[ex[0]][ex[1]] == 0:
        k += 1
        make_step(grid, k)
    path = shortest_path(grid, ex)
    return grid, path


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
