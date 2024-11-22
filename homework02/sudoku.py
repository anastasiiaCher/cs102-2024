import pathlib
import random
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
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
    matrix = [values[i:i + n] for i in range(0, len(values), n)]
    return matrix
    pass


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
    pass


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    return [row[pos[1]] for row in grid]
    pass


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
    start_row, start_col = pos[0] - pos[0] % 3, pos[1] - pos[1] % 3
    block_values = [grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]
    return block_values
    pass


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return i, j
    return None
    pass
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
    all_values = set(map(str, range(1, 10)))
    row_values = set(grid[row])
    col_values = set(grid[i][col] for i in range(len(grid)))
    block_size = 3
    block_row, block_col = row // block_size, col // block_size
    start_row, start_col = block_row * block_size, block_col * block_size
    block_values = set(
        grid[i][j] for i in range(start_row, start_row + block_size) for j in range(start_col, start_col + block_size))
    return all_values - row_values - col_values - block_values
    pass


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
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
    empty_pos = find_empty_positions(grid)
    if not empty_pos:
        return grid
    row, col = empty_pos
    possible_values = find_possible_values(grid, (row, col))
    for i in possible_values:
        grid[row][col] = i
        if solve(grid):
            return grid
        grid[row][col] = '.'
    return None
    pass


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False

    >>> valid_solution = [
    ...     ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ...     ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ...     ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ...     ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ...     ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ...     ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ...     ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ...     ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ...     ['3', '4', '5', '2', '8', '6', '1', '7', '9'],
    ... ]
    >>> check_solution(valid_solution)
    True

    >>> invalid_solution = [
    ...     ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ...     ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ...     ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ...     ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ...     ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ...     ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ...     ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ...     ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ...     ['3', '4', '5', '2', '8', '6', '1', '9', '7'],
    ... ]
    >>> check_solution(invalid_solution)
    False
    """
    rows = [all(len(set(row)) == 9 for row in solution)]
    cols = [all(len(set(col)) == 9 for col in zip(*solution))]
    return rows and cols


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация пазла Sudoku"""
    """ 
        Создать готовую судоку
        Убрать случайные элементы из судоки
        вернуть судоку """
    empty_value = "."
    generated_grid = [[empty_value] * 9 for _ in range(9)]
    solve(generated_grid)
    removable = random.sample([(i, j) for i in range(9) for j in range(9)], k=N)
    for rem in removable:
        generated_grid[rem[0]][rem[1]] = empty_value
    return generated_grid