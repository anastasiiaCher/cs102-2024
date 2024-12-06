from copy import deepcopy
from random import choice, randint
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
    x, y = coord
    max_row, max_col = len(grid) - 1, len(grid[0]) - 1

    if choice([True, False]):
        if 0 <= x - 2 <= max_row and 0 <= y <= max_col:
            grid[x - 1][y] = " "
        elif 0 <= x <= max_row and 0 <= y + 2 <= max_col:
            grid[x][y + 1] = " "
    else:
        if 0 <= x <= max_row and 0 <= y + 2 <= max_col:
            grid[x][y + 1] = " "
        elif 0 <= x - 2 <= max_row and 0 <= y <= max_col:
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

    while empty_cells:
        x, y = empty_cells.pop(0)
        remove_wall(grid, (x, y))
    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

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
        for y, cell in enumerate(row):
            if cell == "X":  # Если клетка - это вход/выход
                exits.append((x, y))
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    positions = [(row, col) for row, cells in enumerate(grid) for col, value in enumerate(cells) if value == k]

    for row, col in positions:
        neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]

        for n_row, n_col in neighbors:
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and grid[n_row][n_col] == 0:
                grid[n_row][n_col] = k + 1

    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    current_pos = exit_coord
    path_length = grid[exit_coord[0]][exit_coord[1]]

    if not isinstance(path_length, int):
        raise ValueError

    k = path_length
    path = [current_pos]

    while grid[current_pos[0]][current_pos[1]] != 1:
        neighbors = [
            (current_pos[0] - 1, current_pos[1]),
            (current_pos[0] + 1, current_pos[1]),
            (current_pos[0], current_pos[1] - 1),
            (current_pos[0], current_pos[1] + 1),
        ]

        found_next = False
        for n_row, n_col in neighbors:
            if (
                0 <= n_row < len(grid)
                and 0 <= n_col < len(grid[0])
                and isinstance(grid[n_row][n_col], int)
                and grid[n_row][n_col] == k - 1
            ):
                path.append((n_row, n_col))
                current_pos = (n_row, n_col)
                k -= 1
                found_next = True
                break

        if not found_next:
            return None

    if len(path) != path_length:
        return None

    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    row, col = coord
    max_row, max_col = len(grid) - 1, len(grid[0]) - 1
    corners = [(0, 0), (0, max_col), (max_row, 0), (max_row, max_col)]

    if coord in corners:
        return True

    if row in [0, max_row]:
        if grid[row][col - 1] == "■" and grid[row][col + 1] == "■" and grid[abs(row - 1)][col] == "■":
            return True

    if col in [0, max_col]:
        if grid[row - 1][col] == "■" and grid[row + 1][col] == "■" and grid[row][abs(col - 1)] == "■":
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
        return grid, exits[0]

    entrance, exit_ = exits[0], exits[1]

    if encircled_exit(grid, entrance) or encircled_exit(grid, exit_):
        return grid, None

    grid[entrance[0]][entrance[1]] = 1
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell in {" ", "X"}:
                grid[row_idx][col_idx] = 0

    steps = 0
    while grid[exit_[0]][exit_[1]] == 0:
        steps += 1
        make_step(grid, steps)

    path = shortest_path(grid, exit_)

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
