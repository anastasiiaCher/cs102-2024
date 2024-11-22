"""Solving and generating sudoku"""

import pathlib
import random
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку"""
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print("".join(grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)))
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    gr = [values[i : i + n] for i in range(0, len(values), n)]
    return gr


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    gr = [grid[i][pos[1]] for i in range(len(grid))]
    return gr


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    arr = [
        grid[i][j]
        for i in range((pos[0] // 3) * 3, (pos[0] // 3) * 3 + 3)
        for j in range((pos[1] // 3) * 3, (pos[1] // 3) * 3 + 3)
    ]
    return arr


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    pos = None
    flag = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if grid[i][j] == ".":
                pos = (i, j)
                flag = -1
                break
        if flag == -1:
            break
    return pos


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    used = [0] * 10
    arr1 = get_col(grid, pos)
    for i, row in enumerate(arr1):
        for val in enumerate(row):
            if val[1] != ".":
                used[ord(val[1]) - ord("0")] = 1
    arr2 = get_row(grid, pos)
    for val in enumerate(arr2):
        if val[1] != ".":
            used[ord(val[1]) - ord("0")] = 1
    arr3 = get_block(grid, pos)
    for i, row in enumerate(arr3):
        for val in enumerate(row):
            if val[1] != ".":
                used[ord(val[1]) - ord("0")] = 1
    values = set()
    for i in range(1, len(used)):
        if used[i] == 0:
            values.add(chr(i + 48))
    return values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решение пазла, заданного в grid"""
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    if find_empty_positions(grid) is None:
        return grid
    pos = find_empty_positions(grid)
    if pos is not None:
        values = find_possible_values(grid, pos)
        for i in values:
            if pos is not None:
                grid[pos[0]][pos[1]] = i
                solve(grid)
            if find_empty_positions(grid) is None:
                return grid
            else:
                if pos is not None:
                    grid[pos[0]][pos[1]] = "."
    return grid


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False
    >>> grid = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["4", "5", "6", "7", "8", "9", "1", "2", "3"], ["7", "8", "9", "1", "2", "3", "4", "5", "6"], ["2", "3", "4", "5", "6", "7", "8", "9", "1"], ["5", "6", "7", "8", "9", "1", "2", "3", "4"], ["8", "9", "1", "2", "3", "4", "5", "6", "7"], ["3", "4", "5", "6", "7", "8", "9", "1", "2"], ["6", "7", "8", "9", "1", "2", "3", "4", "5"], ["9", "1", "2", "3", "4", "5", "6", "7", "8"]]
    >>> check_solution(grid)
    True
    >>> grid = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["4", "5", "5", "7", "8", "9", "1", "2", "3"], ["7", "8", "9", "1", "2", "3", "4", "5", "6"], ["2", "3", "4", "5", "6", "7", "8", "9", "1"], ["5", "6", "7", "8", "9", "1", "2", "3", "4"], ["8", "9", "1", "2", "3", "4", "5", "6", "7"], ["3", "4", "5", "6", "7", "8", "9", "1", "2"], ["6", "7", "8", "9", "1", "2", "3", "4", "5"], ["9", "1", "2", "3", "4", "5", "6", "7", "8"]]
    >>> check_solution(grid)
    False
    """
    flag = True
    for i in range(0, 9):
        arr = get_row(solution, (i, 0))
        used = [0] * 10
        for j, val in enumerate(arr):
            used[ord(val) - ord("0")] += 1
            if used[ord(val) - ord("0")] > 1:
                flag = False
                break
    for i in range(0, 9):
        arr = get_col(solution, (i, 0))
        used = [0] * 10
        for j, row in enumerate(arr):
            for z, val in enumerate(row):
                used[ord(arr[j]) - ord("0")] += 1
                if used[ord(arr[j][z]) - ord("0")] > 1:
                    flag = False
                    break
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            arr = get_block(solution, (i, j))
            used = [0] * 10
            for z, val in enumerate(arr):
                used[ord(val) - ord("0")] += 1
                if used[ord(val) - ord("0")] > 1:
                    flag = False
                    break
    return flag


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    sudoku = [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ["4", "5", "6", "7", "8", "9", "1", "2", "3"],
        ["7", "8", "9", "1", "2", "3", "4", "5", "6"],
        ["2", "3", "4", "5", "6", "7", "8", "9", "1"],
        ["5", "6", "7", "8", "9", "1", "2", "3", "4"],
        ["8", "9", "1", "2", "3", "4", "5", "6", "7"],
        ["3", "4", "5", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "8", "9", "1", "2", "3", "4", "5"],
        ["9", "1", "2", "3", "4", "5", "6", "7", "8"],
    ]
    n = random.randint(0, 1000)
    for i in range(n):
        a1 = random.randint(0, 2)
        a2 = random.randint(0, 2)
        sudoku[a1], sudoku[a2] = sudoku[a2], sudoku[a1]
        a1 = random.randint(3, 5)
        a2 = random.randint(3, 5)
        sudoku[a1], sudoku[a2] = sudoku[a2], sudoku[a1]
        a1 = random.randint(6, 8)
        a2 = random.randint(6, 8)
        sudoku[a1], sudoku[a2] = sudoku[a2], sudoku[a1]
        sudoku = [[sudoku[j][i] for j in range(len(sudoku[i]))] for i in range(len(sudoku))]
    still = 81
    while still > N:
        pos1 = random.randint(0, 8)
        pos2 = random.randint(0, 8)
        if sudoku[pos1][pos2] != ".":
            sudoku[pos1][pos2] = "."
            still -= 1
    return sudoku


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
