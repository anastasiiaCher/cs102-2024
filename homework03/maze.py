from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd  # type: ignore


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """
    x, y, col, row = coord[0], coord[1], len(grid) - 1, len(grid[0]) - 1
    paths = ["go_up", "go_right"]
    path = choice(paths)
    if (path == "go_up") and ((0 <= x - 2 < col) and (0 <= y < row)):
        grid[x - 1][y] = " "
    else:
        path = "go_right"
    if (path == "go_right") and ((0 <= x < col) and (0 <= y + 2 < row)):
        grid[x][y + 1] = " "
    elif (path == "go_right") and ((0 <= x - 2 < col) and (0 <= y < row)):
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
    for pos1, row in enumerate(grid):
        for pos2, _ in enumerate(row):
            if pos1 % 2 == 1 and pos2 % 2 == 1:
                grid[pos1][pos2] = " "
                empty_cells.append((pos1, pos2))

    while empty_cells:
        x, y = empty_cells.pop(0)
        grid = remove_wall(grid, (x, y))

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

    paths = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == k:
                for go_x, go_y in paths:
                    new_x, new_y = x + go_x, y + go_y
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = k + 1

    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    k = 0
    x_out, y_out = exit_coord

    while grid[x_out][y_out] == 0:
        k += 1
        grid = make_step(grid, k)

    path = [exit_coord]
    k = int(grid[x_out][y_out])
    x, y = exit_coord

    while grid[x][y] != 1 and k > 0:
        if (x + 1 < len(grid)) and (grid[x + 1][y] == k - 1):
            x += 1
        elif (x - 1 >= 0) and (grid[x - 1][y] == k - 1):
            x -= 1
        elif (y + 1 < len(grid[0])) and (grid[x][y + 1] == k - 1):
            y += 1
        elif (y - 1 >= 0) and (grid[x][y - 1] == k - 1):
            y -= 1
        else:
            break

        path.append((x, y))
        k -= 1

    if len(path) != grid[exit_coord[0]][exit_coord[1]]:
        grid[path[-1][0]][path[-1][1]] = " "
        path.pop()

        if path:
            x, y = path[-1]
            shortest_path(grid, (x, y))

    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    rows = len(grid)
    cols = len(grid[0])
    x, y = coord

    if (
        (x == 0 and y == 0)
        or (x == 0 and y == cols - 1)
        or (x == rows - 1 and y == 0)
        or (x == rows - 1 and y == cols - 1)
    ):
        return True
    if x == 0:
        if grid[x + 1][y] == "■":
            return True
    if x == rows - 1:
        if grid[x - 1][y] == "■":
            return True
    if y == 0:
        if grid[x][y + 1] == "■":
            return True
    if y == cols - 1:
        if grid[x][y - 1] == "■":
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

    if len(exits) > 1:
        if encircled_exit(grid, exits[0]) or encircled_exit(grid, exits[1]):
            return grid, None

        new_grid = deepcopy(grid)
        x_in, y_in = exits[0]
        grid[x_in][y_in] = 1

        for x in range(len(new_grid)):
            for y in range(len(new_grid[x])):
                if grid[x][y] == " " or grid[x][y] == "X":
                    grid[x][y] = 0

        path = shortest_path(grid, exits[1])
        return new_grid, path
    path = exits
    return grid, path


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path is not None:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    NEW_GRID, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(NEW_GRID, PATH)
    print(pd.DataFrame(MAZE))
