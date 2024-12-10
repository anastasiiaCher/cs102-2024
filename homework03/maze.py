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

    position1, position2, row, col = coord[0], coord[1], len(
        grid) - 1, len(grid[0]) - 1
    paths = ["go_up", "go_right"]
    path = choice(paths)
    if path == "go_up" and (0 <= position1 - 2 < row) and (0 <= position2 - 2 < col):
        grid[position1 - 1][position2] = " "
    else:
        path = "go_right"
        if path == "go_right" and (0 <= position1 < row and 0 <= position2 + 2 < col):
            grid[position1][position2 + 1] = " "
        elif 0 <= position1 - 2 < row and 0 <= position2 < col:
            grid[position1 - 1][position2] = " "
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
    for position1, row in enumerate(grid):
        for position2, _ in enumerate(row):
            if position1 % 2 == 1 and position2 % 2 == 1:
                grid[position1][position2] = " "
                empty_cells.append((position1, position2))
    while empty_cells:
        position1, position2 = empty_cells.pop(0)
        grid = remove_wall(grid, (position1, position2))

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows -
                                                1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0,
                                                  rows - 1) else choice((0, cols - 1))
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
    exits = [(i, j) for i, row in enumerate(grid)
             for j, cell in enumerate(row) if cell == "X"]
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    rows, cols = len(grid), len(grid[0])
    while grid[rows - 1][cols - 1] == 0:
        k += 1
        found = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == k:
                    found = True
                    current_x, current_y = i, j
                    break
            if found:
                break

        if found:
            for x in range(max(0, current_x - 1), min(rows, current_x + 2)):
                for y in range(max(0, current_y - 1), min(cols, current_y + 2)):
                    if grid[x][y] == 0:
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
    k = 0
    exit_x, exit_y = exit_coord
    while grid[exit_x][exit_y] == 0:
        k += 1
        grid = make_step(grid, k)
    path = [exit_coord]
    k = int(grid[exit_x][exit_y])
    exit1, exit2 = exit_coord
    while grid[exit1][exit2] != 1 and k > 1:
        if grid[exit1 + 1][exit2] == k - 1 and exit1 + 1 < len(grid):
            path.append((exit1 + 1, exit2))
            exit1 = exit1 + 1
        elif grid[exit1 - 1][exit2] == k - 1 and exit1 - 1 >= 0:
            path.append((exit1 - 1, exit2))
            exit1 = exit1 - 1
        elif grid[exit1][exit2 - 1] == k - 1 and exit2 - 1 >= 0:
            path.append((exit1, exit2 - 1))
            exit2 = exit2 - 1
        elif grid[exit1][exit2 + 1] == k - 1 and exit2 + 1 < len(grid):
            path.append((exit1, exit2 + 1))
            exit2 = exit2 + 1
        k = k - 1
    if len(path) != grid[exit_coord[0]][exit_coord[1]]:
        grid[path[-1][0]][path[-1][1]] = " "
        path.pop(-1)
        exit1, exit2 = path[-1]
        shortest_path(grid, (exit1, exit2))
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    # проверка на тупик
    position1, position2 = coord
    row, col = len(grid), len(grid[0])

    if (position1 in (0, row - 1) and position2 in (0, col - 1)) or (position1 - 1 == 0 and position2 + 1 == col - 1):
        return True

    if position1 == 0 and position2 in range(0, col) and grid[position1 + 1][position2] == "■":
        return True
    if position2 == 0 and position1 in range(0, row) and grid[position1][position2 + 1] == "■":
        return True
    if position1 == row - 1 and position2 in range(0, col) and grid[position1 - 1][position2] == "■":
        return True
    if position2 == col - 1 and position1 in range(0, row) and grid[position1][position2 - 1] == "■":
        return True
    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """

    exit = get_exits(grid)
    if len(exit) > 1:
        if encircled_exit(grid, exit[0]) or encircled_exit(grid, exit[1]):
            return grid, None
        new_grid = deepcopy(grid)
        new_x, new_y = exit[0]
        grid[new_x][new_y] = 1
        for new_x, row in enumerate(grid):
            for new_y, _ in enumerate(row):
                if grid[new_x][new_y] == " " or grid[new_x][new_y] == "X":
                    grid[new_x][new_y] = 0
        path = shortest_path(grid, exit[1])
        return new_grid, path
    path = exit
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
    NEW_GRID, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(NEW_GRID, PATH)
    print(pd.DataFrame(MAZE))
