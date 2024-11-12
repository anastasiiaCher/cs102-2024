import pathlib
import random
import typing as tp

T = tp.TypeVar("T")


def matrix_transposition(matrix: list[list[str]]) -> list[list[str]]:
    return [[matrix[row_n][column_n] for row_n in range(len(matrix))] for column_n in range(len(matrix[0]))]


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
    line_len = len(values) // n
    return [values[i : i + line_len] for i in range(0, len(values), line_len)]


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
    return matrix_transposition(grid)[pos[1]]


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
    start_row = pos[0] // 3 * 3
    start_column = pos[1] // 3 * 3
    return [grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_column, start_column + 3)]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
    """
    for row in range(len(grid)):
        column = "".join(grid[row]).find(".")
        if column != -1:
            return (row, column)
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
    return set("123456789") - set(get_block(grid, pos)).union(get_row(grid, pos), get_col(grid, pos))


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решение пазла, заданного в grid
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    next_space = find_empty_positions(grid)
    if not next_space:
        return grid
    local_grid = [i.copy() for i in grid]
    possibilities = find_possible_values(grid, next_space)
    for turn in possibilities:
        local_grid[next_space[0]][next_space[1]] = turn
        next_level = solve(local_grid)
        if next_level:
            return next_level
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False
    >>> solution = [['1', '1', '3', '4', '5', '6', '7', '8', '9'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['9', '1', '2', '3', '4', '5', '6', '7', '8']]
    >>> check_solution(solution)
    False
    >>> solution = [['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['1', '5', '6', '7', '8', '9', '1', '2', '3'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['9', '1', '2', '3', '4', '5', '6', '7', '8']]
    >>> check_solution(solution)
    False
    >>> solution = [['9', '1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7']]
    >>> check_solution(solution)
    False
    >>> solution = [['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['9', '1', '2', '3', '4', '5', '6', '7', '8']]
    >>> check_solution(solution)
    True
    """
    correct = set("123456789")
    for row in solution:
        if set(row) != correct:
            return False
    for column in matrix_transposition(solution):
        if set(column) != correct:
            return False
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            if set(get_block(solution, (x, y))) != correct:
                return False
    return True


def shuffle_grid(grid):
    """Перемешивает столбцы и строки пазла, сохраняя их внутри одного блока строк и столбцов"""
    for _ in range(2):
        for block_row in range(0, 9, 3):
            if random.randint(0, 1):
                grid[block_row], grid[block_row + 1] = grid[block_row + 1], grid[block_row]
            if random.randint(0, 1):
                grid[block_row + 1], grid[block_row + 2] = grid[block_row + 2], grid[block_row + 1]
            if random.randint(0, 1):
                grid[block_row + 2], grid[block_row] = grid[block_row + 2], grid[block_row]
        grid = matrix_transposition(grid)
    return grid


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
    trivial_solution = [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ["4", "5", "6", "7", "8", "9", "1", "2", "3"],
        ["7", "8", "9", "1", "2", "3", "4", "5", "6"],
        ["2", "3", "4", "5", "6", "7", "8", "9", "1"],
        ["5", "6", "7", "8", "9", "1", "2", "3", "4"],
        ["8", "9", "1", "2", "3", "4", "5", "6", "7"],
        ["3", "4", "5", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "8", "9", "1", "2", "3", "4", "5"],
        ["9", "1", "2", "3", "4", "5", "6", "7", "8"]
    ]
    null_grid = [["." for _ in range(9)] for _ in range(9)]
    point_list = [(i, j) for i in range(9) for j in range(9)]
    trivial_solution = shuffle_grid(trivial_solution)
    if N > 81:
        N = 81
    for _ in range(N):
        replace_pos = random.randint(0, len(point_list) - 1)
        point = point_list[replace_pos]
        null_grid[point[0]][point[1]] = trivial_solution[point[0]][point[1]]
        point_list.pop(replace_pos)
    return null_grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
