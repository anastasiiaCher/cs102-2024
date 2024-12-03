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

    coin = choice([0, 1])
    pos_col, pos_row = coord[1] + 2, coord[0] - 2

    if coin == 0 and 1 <= pos_row <= len(grid) - 1:
        grid[coord[0] - 1][coord[1]] = " "
    else:
        coin = 1

    if coin == 1 and 1 <= pos_col <= len(grid[0]) - 1:
        grid[coord[0]][coord[1] + 1] = " "
    elif coin == 1 and 1 <= pos_row <= len(grid) - 1:
        grid[coord[0] - 1][coord[1]] = " "

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

    for el in empty_cells:
        remove_wall(grid, el)

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

    for i, row in enumerate(grid):
        if "X" in row:
            exits.append((i, row.index('X')))
            break
    for i, row in enumerate(grid):
        if "X" in row and exits[0] != (i, row.index('X')):
            exits.append((i, row.index('X')))
            break
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    m_row, m_col = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == k:
                if j - 1 >= 0 == grid[i][j - 1]:
                    grid[i][j - 1] = k + 1
                if j + 1 < m_col and grid[i][j + 1] == 0:
                    grid[i][j + 1] = k + 1
                if i - 1 >= 0 and grid[i - 1][j] == 0:
                    grid[i - 1][j] = k + 1
                if i + 1 < m_row and grid[i + 1][j] == 0:
                    grid[i + 1][j] = k + 1
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    needed_len, cur_coord = grid[exit_coord[0]][exit_coord[1]], exit_coord
    path = [exit_coord]
    count = needed_len
    while grid[cur_coord[0]][cur_coord[1]] != 1:
        possible = [
            (cur_coord[0], cur_coord[1] - 1),
            (cur_coord[0], cur_coord[1] + 1),
            (cur_coord[0] - 1, cur_coord[1]),
            (cur_coord[0] + 1, cur_coord[1])
        ]

        for i, j in possible:
            if grid[i][j] == grid[cur_coord[0]][cur_coord[1]] - 1:
                count -= 1
                cur_coord = (i, j)
                path.append(cur_coord)
                break

    if len(path) != needed_len:
        grid[cur_coord[0]][cur_coord[1]] = " "
        shortest_path(grid, exit_coord)
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    row, col = coord

    if row == 0 and grid[row + 1][col] == "■":
        return True
    if col == 0 and grid[row][col + 1] == "■":
        return True
    if row == len(grid) - 1 and grid[row - 1][col] == "■":
        return True
    if col == len(grid[row]) - 1 and grid[row][col - 1] == "■":
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
    if len(exits) < 2:
        return grid, exits

    for el in exits:
        if encircled_exit(grid, el):
            return grid, None
    k = 0
    grid[exits[0][0]][exits[0][1]] = 1
    grid[exits[1][0]][exits[1][1]] = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == " ":
                grid[i][j] = 0

    while grid[exits[1][0]][exits[1][1]] == 0:
        k += 1
        make_step(grid, k)
    path = shortest_path(grid, exits[1])
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
