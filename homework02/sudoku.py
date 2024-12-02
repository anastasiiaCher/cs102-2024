import pathlib
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
    size = int(len(digits) ** 0.5)
    return group(digits, size)


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку"""
    size = len(grid)
    subgrid_size = int(size**0.5)
    width = 2
    line = "+".join(["-" * (width * subgrid_size)] * subgrid_size)
    for row in range(size):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if (col + 1) % subgrid_size == 0 and col + 1 < size else "")
                for col in range(size)
            )
        )
        if (row + 1) % subgrid_size == 0 and row + 1 < size:
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
    return [grid[row][pos[1]] for row in range(len(grid))]


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
    block_size = int(len(grid) ** 0.5)
    block_row, block_col = pos[0] // block_size * block_size, pos[1] // block_size * block_size
    return [
        grid[row][col]
        for row in range(block_row, block_row + block_size)
        for col in range(block_col, block_col + block_size)
    ]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == ".":
                return r, c
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
    used_values = set(get_row(grid, pos) + get_col(grid, pos) + get_block(grid, pos))
    return set("123456789") - used_values


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
    """Если решение solution верно, то вернуть True, в противном случае False"""
    # TODO: Add doctests with bad puzzles
    size = len(solution)
    valid_set = set(str(i) for i in range(1, size + 1))

    for i in range(size):
        if set(solution[i]) != valid_set:
            return False
        if set(row[i] for row in solution) != valid_set:
            return False

    block_size = int(size**0.5)
    for block_row in range(0, size, block_size):
        for block_col in range(0, size, block_size):
            block = []
            for r in range(block_row, block_row + block_size):
                for c in range(block_col, block_col + block_size):
                    block.append(solution[r][c])
            if set(block) != valid_set:
                return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку, заполненного на N элементов."""

    import random

    n = 9
    grid = [["." for _ in range(n)] for _ in range(n)]

    def fill_grid(grid):
        """Рекурсивно заполняет пустую сетку для решения"""
        pos = find_empty_positions(grid)
        if not pos:
            return True
        row, col = pos
        numbers = list(map(str, range(1, n + 1)))
        random.shuffle(numbers)
        for num in numbers:
            if num in find_possible_values(grid, pos):
                grid[row][col] = num
                if fill_grid(grid):
                    return True
                grid[row][col] = "."
        return False

    fill_grid(grid)

    cells = [(r, c) for r in range(n) for c in range(n)]
    random.shuffle(cells)
    for i in range(len(cells) - N):
        row, col = cells[i]
        grid[row][col] = "."
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
