from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]],
    coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """
    x, y = coord[0], coord[1]
    directions = ["up", "right"]
    direction = choice(directions)
    if direction == "up":
        if x > 1:
            grid[x - 1][y] = " "
        elif y < len(grid[0]) - 2:
            grid[x][y + 1] = " "
    else:
        if y < len(grid[0]) - 2:
            grid[x][y + 1] = " "
        elif x > 1:
            grid[x - 1][y] = " "

    return grid


def bin_tree_maze(rows: int = 15, cols: int = 15, 
random_exit: bool = True) -> List[List[Union[str, int]]]:
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
    for _, val in enumerate(empty_cells):
        grid = remove_wall(grid, (val))
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
        for j, val in enumerate(row):
            if val == "X":
                exits.append((i, j))
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == k:
                if i > 0 and grid[i - 1][j] == 0:
                    grid[i - 1][j] = k + 1
                if i < len(grid) - 1 and grid[i + 1][j] == 0:
                    grid[i + 1][j] = k + 1
                if j > 0 and grid[i][j - 1] == 0:
                    grid[i][j - 1] = k + 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 0:
                    grid[i][j + 1] = k + 1
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
    k = int(grid[exit_coord[0]][exit_coord[1]])
    path: List[Tuple[int, int]] = []
    while len(path) + 1 != grid[exit_coord[0]][exit_coord[1]]:
        if x > 0 and grid[x - 1][y] == k - 1:
            path.append((x, y))
            k -= 1
            x -= 1
            continue
        if x < len(grid) - 1 and grid[x + 1][y] == k - 1:
            path.append((x, y))
            k -= 1
            x += 1
            continue
        if y > 0 and grid[x][y - 1] == k - 1:
            path.append((x, y))
            k -= 1
            y -= 1
            continue
        if y < len(grid[0]) - 1 and grid[x][y + 1] == k - 1:
            path.append((x, y))
            k -= 1
            y += 1
            continue
        grid[x][y] = " "
        x, y = path[-1]
        path.pop()
    path.append((x, y))
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    x, y = coord
    if (
        (x == 0 and y == 0)
        or (x == 0 and y == len(grid[0]) - 1)
        or (x == len(grid) - 1 and y == 0)
        or (x == len(grid) - 1 and y == len(grid[0]) - 1)
    ):
        return True
    if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
        if (
            (x == 0 and grid[x][y - 1] == "■" and grid[x][y - 1] and grid[x + 1][y] == "■")
            or (x == len(grid) - 1 and grid[x][y - 1] == "■"
                 and grid[x][y - 1] and grid[x - 1][y] == "■")
            or (y == 0 and grid[x - 1][y] == "■" and grid[x + 1][y] and grid[x][y + 1] == "■")
            or (y == len(grid[0]) - 1 and grid[x - 1][y] == "■" 
                and grid[x + 1][y] and grid[x][y - 1] == "■")
        ):
            return True
    if (x == 0 or x == len(grid) - 1) or (y == 0 or y == len(grid[0]) - 1):
        if (
            (x == 0 and grid[x][y - 1] == "■" and grid[x][y - 1] and grid[x + 1][y] == " ")
            or (x == len(grid) - 1 and grid[x][y - 1] == "■" and grid[x][y - 1] and grid[x - 1][y] == " ")
            or (y == 0 and grid[x - 1][y] == "■" and grid[x + 1][y] and grid[x][y + 1] == " ")
            or (y == len(grid[0]) - 1 and grid[x - 1][y] == "■" and grid[x + 1][y] and grid[x][y - 1] == " ")
        ):
            return False
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
        return (grid, None)
    if len(exits) == 2:
        if encircled_exit(grid, exits[0]) or encircled_exit(grid, exits[1]):
            return (grid, None)
        else:
            grid
            for i, row in enumerate(grid):
                for j, val in enumerate(row):
                    if val == " ":
                        grid[i][j] = 0
            grid[exits[0][0]][exits[0][1]] = 1
            grid[exits[1][0]][exits[1][1]] = 0
            k = 1
            while grid[exits[1][0]][exits[1][1]] == 0:
                grid = make_step(grid, k)
                k += 1
            for i, row in enumerate(grid):
                for j, val in enumerate(row):
                    if val == 0:
                        grid[i][j] = " "
            k = int(grid[exits[1][0]][exits[1][1]])
            path = shortest_path(grid, exits[1])
            return (grid, path)
    return (grid, path)


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
                elif grid[i][j] != "■":
                    grid[i][j] = " "
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    MAZE, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
