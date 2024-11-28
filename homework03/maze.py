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

    grid[coord[0]][coord[1]] = " "
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

    while empty_cells:
        x, y = choice(empty_cells)
        empty_cells.remove((x, y))
        if choice((True, False)):
            if x - 1 > 0:
                grid = remove_wall(grid, (x - 1, y))
        else:
            if y + 1 < cols - 1:
                grid = remove_wall(grid, (x, y + 1))

    # генерация входа и выхода
    option = choice((True, False))
    if option:
        x_in, x_out = int(input("Enter x_in: ")), int(input("Enter x_out: "))
        y_in = int(input("Enter y_in: ")) if x_in in (0, rows - 1) else int(input("Choose 0 or 14 for y_in: "))
        y_out = int(input("Enter y_out: ")) if x_out in (0, rows - 1) else int(input("Choose 0 or 14 for y_out: "))
    else:
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

    exits = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == "X"]
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """

    entrance, our_exit = get_exits(grid)
    grid[entrance[0]][entrance[1]] = 1
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == " " or grid[x][y] == "X":
                grid[x][y] = "0"
    while grid[our_exit[0]][our_exit[1]] == "0":
        k += 1
        for x, row in enumerate(grid):
            for y, _ in enumerate(row):
                if grid[x][y] == str(k):
                    if grid[x + 1][y] != "■":
                        grid[x + 1][y] = str(k + 1)
                    if grid[x - 1][y] != "■":
                        grid[x - 1][y] = str(k + 1)
                    if grid[x][y + 1] != "■":
                        grid[x][y + 1] = str(k + 1)


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    pass


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """

    if coord[0] in (0, len(grid) - 1) or coord[1] in (0, len(grid[0]) - 1):
        return True
    elif (grid[coord[0] - 1][coord[1]] == "■" and grid[coord[0] + 1][coord[1]] == "■" and grid[coord[0]][coord[1] + 1]) or (grid[coord[0] - 1][coord[1]] == "■" and grid[coord[0] + 1][coord[1]] == "■" and grid[coord[0]][coord[1] - 1]):
        return True
    else:
        return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """

    exits = get_exits(grid)
    if len(exits) > 1:
        if encircled_exit(grid, exits[1]): # продумать ситуацию, если оба окружены стенами/тупиками???
            return grid, shortest_path(grid, exits[0])
        else:
            return grid, shortest_path(grid, exits[1])
    else:
        return grid, shortest_path(grid, exits[0])



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
    print(pd.DataFrame(bin_tree_maze(15, 15, choice((True, False)))))
    GRID = bin_tree_maze(15, 15, choice((True, False)))
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
