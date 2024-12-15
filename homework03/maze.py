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

    moves = ["up", "right"]
    a, b, rowa, columna = coord[0], coord[1], len(grid) - 1, len(grid[0]) - 1

    move = choice(moves)
    if (move == "up") and (0 <= a - 2 < rowa and 0 <= b < columna):
        grid[a - 1][b] = " "
    else:
        move = "right"
    if (move == "right") and (0 <= a < rowa and 0 <= b + 2 < columna):
        grid[a][b + 1] = " "
    elif 0 <= a - 2 < rowa and 0 <= b < columna:
        grid[a - 1][b] = " "
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
        a, b = empty_cells.pop(0)
        remove_wall(grid, (a, b))

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

    for a, rowa in enumerate(grid):
        for b, _ in enumerate(rowa):
            if grid[a][b] == k:
                if a + 1 < len(grid) and grid[a + 1][b] == 0:
                    grid[a + 1][b] = k + 1
                if a - 1 >= 0 and grid[a - 1][b] == 0:
                    grid[a - 1][b] = k + 1
                if b + 1 < len(grid[0]) and grid[a][b + 1] == 0:
                    grid[a][b + 1] = k + 1
                if b - 1 >= 0 and grid[a][b - 1] == 0:
                    grid[a][b - 1] = k + 1
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
    avih, bvih = exit_coord
    while grid[avih][bvih] == 0:
        k += 1
        grid = make_step(grid, k)

    path = [exit_coord]
    k = int(grid[avih][bvih])
    a, b = exit_coord
    while grid[a][b] != 1 and k > 0:
        if a + 1 < len(grid) and grid[a + 1][b] == k - 1:
            path.append((a + 1, b))
            a = a + 1
        elif a - 1 >= 0 and grid[a - 1][b] == k - 1:
            path.append((a - 1, b))
            a = a - 1
        elif b + 1 < len(grid[0]) and grid[a][b + 1] == k - 1:
            path.append((a, b + 1))
            b = b + 1
        elif b - 1 >= 0 and grid[a][b - 1] == k - 1:
            path.append((a, b - 1))
            b = b - 1
        k -= 1

    if len(path) != grid[exit_coord[0]][exit_coord[1]]:
        grid[path[-1][0]][path[-1][1]] = " "
        path.pop(-1)
        a, b = path[-1]
        shortest_path(grid, (a, b))

    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    a, b = coord
    rowi, columni = len(grid), len(grid[0])
    if (a in (0, rowi - 1) and b in (0, columni - 1)) or (a - 1 == 0 and a + 1 == columni - 1):
        return True
    if a == 0 and b in range(0, columni) and grid[a + 1][b] == "■":
        return True
    if a == rowi - 1 and b in range(0, columni) and grid[a - 1][b] == "■":
        return True
    if b == 0 and a in range(0, rowi) and grid[a][b + 1] == "■":
        return True
    if b == columni - 1 and a in range(0, rowi) and grid[a][b - 1] == "■":
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
    escapades = get_exits(grid)
    gracias, campagnes = escapades[0], escapades[1]
    if encircled_exit(grid, gracias) or encircled_exit(grid, campagnes):
        return grid, None
    grid[gracias[0]][gracias[1]] = 1
    k = 0
    for a, rowa in enumerate(grid):
        for b, _ in enumerate(rowa):
            if grid[a][b] == " " or grid[a][b] == "X":
                grid[a][b] = 0
    while grid[campagnes[0]][campagnes[1]] == 0:
        k += 1
        make_step(grid, k)
    path = shortest_path(grid, campagnes)
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
