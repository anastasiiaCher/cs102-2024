from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """
    Apparently that does not work:

    if coord[0] - 1 == 0 and coord[1] == len(grid[0]) - 2:
        return grid
    if coord[0] - 1 == 0:
        direction = (0, 1)
    elif coord[1] == len(grid[0]) - 2:
        direction = (-1, 0)
    else:
        direction = choice([(0, 1), (-1, 0)])
    grid[coord[0] + direction[0]][coord[1] + direction[1]] = ' '
    return grid

    IDK why
    The labyrinth is just fine but the tests fail
    """
    grid = deepcopy(grid)
    cols = len(grid[0])
    x, y = coord

    right = randint(0, 1)
    up = int(not right)
    can_go_up = int(x - 1 != 0)
    can_go_right = int(y + 2 != cols)

    match (up, right, can_go_up, can_go_right):
        case (1, 0, 1, _):
            grid[x - 1][y] = " "
        case (1, 0, 0, 1):
            grid[x][y + 1] = " "
        case (0, 1, _, 1):
            grid[x][y + 1] = " "
        case (0, 1, 1, 0):
            grid[x - 1][y] = " "
    return grid


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
    """
    Делает пустое поле, выкалывает в нем клетки
    Ходит змейкой по всем клетками и наугад сносит верхнюю или правую стену
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))
    """
    for y in range(1, rows, 2):
        for x in range(1, cols, 2):
            grid = remove_wall(grid, (y, x))
    """
    for cell in empty_cells:
        grid = remove_wall(grid, cell)

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
    return [(x, y.index("X")) for x, y in enumerate(grid) if "X" in y]


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """
    >>> grid = [["■", "■", "■"], ["■", 0, "■"], ["■", 1, "■"]]
    >>> make_step(grid, 1)
    [['■', '■', '■'], ['■', 2, '■'], ['■', 1, '■']]
    >>> grid = [[0, 0, 0], [0, 1, 0], [0, 1, 0]]
    >>> make_step(grid, 1)
    [[0, 2, 0], [2, 1, 2], [2, 1, 2]]
    """
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            step = (y, x)
            if grid[step[0]][step[1]] == k:
                for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if step[0] + direction[0] not in (-1, len(grid)) and step[1] + direction[1] not in (
                        -1,
                        len(grid[0]),
                    ):
                        if grid[step[0] + direction[0]][step[1] + direction[1]] == 0:
                            grid[step[0] + direction[0]][step[1] + direction[1]] = k + 1
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """
    k = int(grid[exit_coord[0]][exit_coord[1]])
    if grid[exit_coord[0]][exit_coord[1]] == 1:
        return exit_coord
    for directions in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if not (exit_coord[0] + directions[0] in {-1, len(grid)}
        or exit_coord[1] + directions[1] in {-1, len(grid[0])}):
            if grid[exit_coord[0] + directions[0]][exit_coord[1] + directions[1]] == k - 1:
                next_step_coord = (exit_coord[0] + directions[0], exit_coord[1] + directions[1])
                break

    next_step = shortest_path(grid, next_step_coord)
    mypy_step = list(next_step)[0]
    if type(mypy_step) == int:
        return [exit_coord, mypy_step]
    return [exit_coord, *mypy_step]
    """
    if grid[exit_coord[0]][exit_coord[1]] == 1:
        return exit_coord
    k = int(grid[exit_coord[0]][exit_coord[1]])
    path = [exit_coord]
    while k > 1:
        for directions in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if not (
                exit_coord[0] + directions[0] in {-1, len(grid)} or exit_coord[1] + directions[1] in {-1, len(grid[0])}
            ):
                if grid[exit_coord[0] + directions[0]][exit_coord[1] + directions[1]] == k - 1:
                    exit_coord = exit_coord[0] + directions[0], exit_coord[1] + directions[1]
                    path.append(exit_coord)
                    k -= 1
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """
    Если нахожу смежную с выходом свободную клетку - возвращаю False
    Иначе - True
    >>> grid = [["■", "■"], ["■", "X"], ["■", "■"]]
    >>> encircled_exit(grid, (1, 1))
    True
    >>> grid = [["■", "■", "■"], ["■", "X", "■"]]
    >>> encircled_exit(grid, (1, 1))
    True
    >>> grid = [["■", "■", "■"], ["■", " ", "■"], ["■", "X", "■"]]
    >>> encircled_exit(grid, (2, 1))
    False
    """
    wall_counter = 0
    void_counter = 0
    for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if not (coord[0] + direction[0] in {-1, len(grid)} or coord[1] + direction[1] in {-1, len(grid[0])}):
            if grid[coord[0] + direction[0]][coord[1] + direction[1]] == "■":
                wall_counter += 1
        else:
            void_counter += 1
    return (void_counter == 1 and wall_counter == 3) or (void_counter == 2 and wall_counter == 2)


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """
    >>> grid = [["■", "X", "■"], ["■", " ", "■"], ["■", "X", "■"]]
    >>> solve_maze(grid)
    ([['■', 1, '■'], ['■', 2, '■'], ['■', 3, '■']], [(2, 1), (1, 1), (0, 1)])
    """
    grid = deepcopy(grid)
    exits = get_exits(grid)

    # Проверка совпадения выходов
    if len(exits) == 1:
        return grid, exits[0]

    # Проверка тупиковости выходов
    for door in exits:
        if encircled_exit(grid, door):
            return grid, None

    # Заполнение поля нулями, замена входа единицей
    grid = [["■" if y == "■" else 0 for y in x] for x in grid]
    grid[exits[0][0]][exits[0][1]] = 1

    # Алгоритм Дейкстры
    k = 0
    while grid[exits[1][0]][exits[1][1]] == 0:
        k += 1
        grid = make_step(grid, k)
    return grid, shortest_path(grid, exits[1])


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
