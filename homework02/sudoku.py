"sudoky"
import pathlib
import random
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать из указанного файла"""
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
    return [values[i : i + n] for i in range(0, len(values), n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row_index = pos[0]
    return grid[row_index]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    col_index = pos[1]
    return [grid[row][col_index] for row in range(len(grid))]


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
    row_start = (pos[0] // 3) * 3
    col_start = (pos[1] // 3) * 3
    return [grid[row][col] for row in range(row_start, row_start + 3) for col in range(col_start, col_start + 3)]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                return (row, col)
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
    row, col = pos
    possible_values = set("123456789")

    # Убираем числа, которые уже есть в строке
    possible_values -= set(grid[row])

    # Убираем числа, которые уже есть в столбце
    for r in range(len(grid)):
        possible_values.discard(grid[r][col])

    # Убираем числа, которые уже есть в блоке 3x3
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            possible_values.discard(grid[r][c])

    return possible_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решение пазла, заданного в grid"""
    """ 
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'], 
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
    ['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
    ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    empty_pos = find_empty_positions(grid)
    if not empty_pos:
        return grid

    row, col = empty_pos

    for value in find_possible_values(grid, (row, col)):
        grid[row][col] = value
        if solve(grid):
            return grid
        grid[row][col] = "."

    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False
    >>> check_solution([
    ...     ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ...     ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ...     ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ...     ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ...     ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ...     ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ...     ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ...     ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ...     ['3', '4', '5', '2', '8', '6', '1', '7', '7']
    ... ])
    False
    """

    def is_valid_group(group: tp.List[str]) -> bool:
        return sorted(group) == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Проверка строк
    for row in solution:
        if not is_valid_group(row):
            return False

    # Проверка столбцов
    for col in range(9):
        col_values = [solution[row][col] for row in range(9)]
        if not is_valid_group(col_values):
            return False

    # Проверка блоков 3x3
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            block = [
                solution[row][col] for row in range(block_row, block_row + 3) for col in range(block_col, block_col + 3)
            ]
            if not is_valid_group(block):
                return False

    return True


def generate_sudoku(n: int) -> tp.List[tp.List[str]]:
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

    def create_full_grid() -> tp.List[tp.List[str]]:
        """
        Создаёт полностью заполненный судоку.
        """
        grid = [["." for _ in range(9)] for _ in range(9)]
        solve(grid)
        return grid

    def remove_elements(grid: tp.List[tp.List[str]], count: int) -> None:
        """
        Убирает заданное количество элементов из судоку, заменяя их на точки.
        """
        positions = [(row, col) for row in range(9) for col in range(9)]
        random.shuffle(positions)
        for i in range(count):
            row, col = positions[i]
            grid[row][col] = "."

    full_grid = create_full_grid()

    n = min(n, 81)
    remove_elements(full_grid, 81 - n)

    return full_grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
