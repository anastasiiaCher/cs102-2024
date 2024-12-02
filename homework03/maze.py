from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    """
    Create grid of ■
    """
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param coord:
    :return:
    """
    directions = ["up", "right"]
    x, y, rows, cols = coord[0], coord[1], len(grid) - 1, len(grid[0]) - 1

    direction = choice(directions)
    if (direction == "up") and (0 <= x - 2 < rows and 0 <= y < cols):
        grid[x - 1][y] = " "
    else:
        direction = "right"
    if (direction == "right") and (0 <= x < rows and 0 <= y + 2 < cols):
        grid[x][y + 1] = " "
    elif 0 <= x - 2 < rows and 0 <= y < cols:
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
    while empty_cells:
        x, y = empty_cells.pop(0)
        remove_wall(grid, (x, y))

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
    return [(x, y) for x, row in enumerate(grid) for y, elem in enumerate(row) if elem == "X"]


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param k:
    :return:
    """
    all_coords = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if row[y] == k:
                all_coords.append((x, y))

    k += 1
    for i in all_coords:
        cur_coord = i
        coords = [(x, y) for x, row in enumerate(grid) for y, _ in enumerate(row)]
        possible_pos = [
            (cur_coord[0] - 1, cur_coord[1]),
            (cur_coord[0] + 1, cur_coord[1]),
            (cur_coord[0], cur_coord[1] - 1),
            (cur_coord[0], cur_coord[1] + 1),
        ]
        for x, y in possible_pos:
            if (x, y) in coords and grid[x][y] == 0:
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
    cur_coord, k, path_len = exit_coord, grid[exit_coord[0]][exit_coord[1]], grid[exit_coord[0]][exit_coord[1]]
    coords = [(x, y) for x, row in enumerate(grid) for y, _ in enumerate(row)]
    path = [cur_coord]

    while grid[cur_coord[0]][cur_coord[1]] != 1:
        possible_pos = [
            (cur_coord[0] - 1, cur_coord[1]),
            (cur_coord[0] + 1, cur_coord[1]),
            (cur_coord[0], cur_coord[1] - 1),
            (cur_coord[0], cur_coord[1] + 1),
        ]
        for x, y in possible_pos:
            if (x, y) in coords and grid[x][y] == int(k) - 1:
                path.append((x, y))
                cur_coord = (x, y)
                k = int(k) - 1
                break

    if len(path) != path_len:
        grid[cur_coord[0]][cur_coord[1]] = " "
        shortest_path(grid, exit_coord)

    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """
    :param grid:
    :param coord:
    :return:
    """
    coord_x_max, coord_y_max = len(grid) - 1, len(grid[0]) - 1
    angles = [(0, 0), (0, coord_y_max), (coord_x_max, 0), (coord_x_max, coord_y_max)]

    if coord in angles:
        if grid[abs(coord[0] - 1)][coord[1]] == "■" and grid[coord[0]][abs(coord[1] - 1)] == "■":
            return True
    if coord[0] in [0, coord_x_max]:
        if (
            grid[coord[0]][coord[1] - 1] == "■"
            and grid[coord[0]][coord[1] + 1] == "■"
            and grid[abs(coord[0] - 1)][coord[1]] == "■"
        ):
            return True
    if coord[1] in [0, coord_y_max]:
        if (
            grid[coord[0] - 1][coord[1]] == "■"
            and grid[coord[0] + 1][coord[1]] == "■"
            and grid[coord[0]][abs(coord[1] - 1)] == "■"
        ):
            return True
    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """
    :param grid:
    :return:
    """
    if len(get_exits(grid)) == 1:
        return grid, get_exits(grid)[0]

    exits = get_exits(grid)
    entrance, exit_ = exits[0], exits[1]
    if encircled_exit(grid, entrance) or encircled_exit(grid, exit_):
        return grid, None

    k = 0
    grid[entrance[0]][entrance[1]] = 1
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == " " or grid[x][y] == "X":
                grid[x][y] = 0

    while grid[exit_[0]][exit_[1]] == 0:
        k += 1
        make_step(grid, k)
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
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if isinstance(grid[i][j], int):
                    grid[i][j] = " "
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
