"Программа для судоку"

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
    "создаем субоку по файлу"
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
    mass = []
    for i in range(0, len(values), n):
        mass.append(values[i : i + n])
    return mass


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    copy = [row[:] for row in grid]
    return copy[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    copy = [row[:] for row in grid]
    mass = []
    for i in copy:
        mass.append(i[pos[1]])
    return mass


def full_line(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    "восстанавливаем строку"
    line = grid[pos[0]]
    mass = []
    if pos[1] % 3 == 0:
        mass.extend(line[pos[1] : pos[1] + 3])
    if pos[1] % 3 == 1:
        mass.extend(line[pos[1] - 1 : pos[1] + 2])
    if pos[1] % 3 == 2:
        mass.extend(line[pos[1] - 2 : pos[1] + 1])
    return mass


def get_block(copy: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    grid = [row[:] for row in copy]
    mass = []
    if pos[0] % 3 == 0:
        mass.extend(
            [full_line(grid, pos), full_line(grid, (pos[0] + 1, pos[1])), full_line(grid, (pos[0] + 2, pos[1]))]
        )
    elif pos[0] % 3 == 1:
        mass.extend(
            [full_line(grid, (pos[0] - 1, pos[1])), full_line(grid, pos), full_line(grid, (pos[0] + 1, pos[1]))]
        )
    elif pos[0] % 3 == 2:
        mass.extend(
            [full_line(grid, (pos[0] - 2, pos[1])), full_line(grid, (pos[0] - 1, pos[1])), full_line(grid, pos)]
        )
    line = []
    for i in mass:
        for j in i:
            line.append(j)
    return line


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i, row in enumerate(grid):
        if "." in row:
            return (i, row.index("."))
    return None


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
    perfect = "123456789"
    myset = set()
    for num in perfect:
        if (not num in get_col(grid, pos)) and (not num in get_row(grid, pos)) and (not num in get_block(grid, pos)):
            myset.add(num)
    return myset


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
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], 
    ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
     ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
     ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
      ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    empty = find_empty_positions(grid)
    if empty:
        values = find_possible_values(grid, empty)
        for value in values:
            grid[empty[0]][empty[1]] = value
            if solve(grid):
                return grid
            else:
                grid[empty[0]][empty[1]] = "."
    else:
        return grid
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""
    if find_empty_positions(solution):
        return False
    else:
        for i in range(9):
            for j in range(9):
                if (
                    len(get_col(solution, (i, j))) != len(set(get_col(solution, (i, j))))
                    or len(get_row(solution, (i, j))) != len(set(get_row(solution, (i, j))))
                    or len(get_block(solution, (i, j))) != len(set(get_block(solution, (i, j))))
                ):
                    return False
    return True


def full_sudoku() -> tp.List[tp.List[str]]:
    grid = [["." for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            pos = (i, j)
            for el in find_possible_values(grid, pos):
                grid[pos[0]][pos[1]] = el
                if not solve(grid):
                    grid[pos[0]][pos[1]] = "."
                else:
                    return grid
    if check_solution(grid):
        return grid
    return []


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
    grid = full_sudoku()
    count = 81 - N
    while count > 0:
        pos = (random.randint(0, 8), random.randint(0, 8))
        if grid[pos[0]][pos[1]] != ".":
            grid[pos[0]][pos[1]] = "."
            count -= 1
    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
