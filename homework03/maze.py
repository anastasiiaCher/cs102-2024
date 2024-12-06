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
    row, col = coord[0], coord[1]
    directions = ["go up", "go right"]

    decision = choice(directions)
    if decision == "go up" and (0 <= row - 2 < len(grid) - 1 and 0 <= col < len(grid[0]) - 1):
        grid[row - 1][col] = " "
    else:
        decision = "go right"
    if decision == "go right" and (0 <= row < len(grid) - 1 and 0 <= col + 2 < len(grid[0]) - 1):
        grid[row][col + 1] = " "
    elif 0 <= row - 2 < len(grid) - 1 and 0 <= col < len(grid[0]) - 1:
        grid[row - 1][col] = " "

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
        empty_cell_row, empty_cell_col = empty_cells.pop(0)
        grid = remove_wall(grid, (empty_cell_row, empty_cell_col))

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

    exits = [(i, j) for i, row in enumerate(grid) for j, element in enumerate(row) if element == "X"]
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if grid[i][j] == k:
                
                if i + 1 < len(grid) and grid[i + 1][j] == 0:
                    grid[i + 1][j] = k + 1
                if 0 <= i - 1 and grid[i - 1][j] == 0:
                    grid[i - 1][j] = k + 1
                if j + 1 < len(row) and grid[i][j + 1] == 0:
                    grid[i][j + 1] = k + 1
                if 0 <= i - 1 and grid[i][j - 1] == 0:
                    grid[i][j - 1] = k + 1

    return grid

        
def find_closest_coordinates(grid: List[List[Union[str, int]]], current_position: Tuple[int, int]
) -> List[Tuple[int, int]]:
    """
    Эта функция вычисляет ближайшие к текущей позиции доступные непустые координаты
    >>> find_closest_coordinates(
    ...     [["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
    ...     ["■", 0, 0, 0, 0, 0, 0, 0, 0, 0, "■"],
    ...     ["■", "■", "■", "■", "■", 0, "■", 0, "■", 0, "■"],
    ...     ["■", 0, 0, 0, 0, 0, "■", 0, "■", 3, "■"],
    ...     ["■", "■", "■", "■", "■", "■", "■", "■", "■", 2, 1],
    ...     [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, "■"],
    ...     ["■", "■", "■", "■", "■", "■", "■", 0, "■", 0, "■"],
    ...     ["■", 0, 0, 0, 0, 0, 0, 0, "■", 0, "■"],
    ...     ["■", "■", "■", 0, "■", "■", "■", 0, "■", 0, "■"],
    ...     ["■", 0, 0, 0, "■", 0, 0, 0, "■", 0, "■"],
    ...     ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]], (3, 9))
    [(4, 9), (2, 9)]
    """
        
    i = current_position[0]
    j = current_position[1]

    closest_coordinates = list()
    if i + 1 < len(grid) and grid[i + 1][j] != "■":
        closest_coordinates.append((i + 1, j))
    if j + 1 < len(grid[0]) and grid[i][j + 1] != "■":
        closest_coordinates.append((i, j + 1))
    if i - 1 >= 0 and grid[i - 1][j] != "■":
        closest_coordinates.append((i - 1, j))
    if j - 1 >= 0 and grid[i][j - 1] != "■" :
        closest_coordinates.append((i, j - 1))

    return closest_coordinates

def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    i = exit_coord[0]
    j = exit_coord[1]
    current_value = grid[i][j]

    if current_value == 1:
        return [(i, j)]
    
    close_coordinates = find_closest_coordinates(grid, exit_coord)

    for step in close_coordinates:
        next_value = grid[step[0]][step[1]]
        if type(current_value) == int and type(next_value) == int and next_value == current_value - 1:
            result = shortest_path(grid, step)
            if result:
                return [(i, j)] + result
    grid[step[0]][step[1]] = " "

def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    i = coord[0]
    j = coord[1]
    if find_closest_coordinates(grid, coord) or (i != 0 and j != 0 and i != len(grid) - 1 and j != len(grid[0]) - 1):
        return False
    return True


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
    start, finish = exits[0], exits[1]
    if encircled_exit(grid, start) or encircled_exit(grid, finish):
        return grid, None
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if grid[i][j] != "■":
                grid[i][j] = 0
    grid[start[0]][start[1]] = 1   #в клетку входа ставим 1            
    k = 0
    while grid[finish[0]][finish[1]] == 0:
        k += 1
        make_step(grid, k)
    path = shortest_path(grid, finish)
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
