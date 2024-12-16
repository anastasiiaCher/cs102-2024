import copy
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
    new_list = list(zip(*(iter(values),) * n))
    return [list(group) for group in new_list]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos"""
    row, _ = pos
    return grid[row]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos"""
    _, col = pos
    return [grid[row][col] for row in range(len(grid))]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos"""
    block_size = 3  # Размер блока 3x3
    start_row = (pos[0] // block_size) * block_size
    start_col = (pos[1] // block_size) * block_size
    block_numbers = []

    for i in range(start_row, start_row + block_size):
        for j in range(start_col, start_col + block_size):
            block_numbers.append(grid[i][j])

    return block_numbers


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле"""

    for row, row_values in enumerate(grid):
        for col, value in enumerate(row_values):
            if value == ".":
                return row, col
    return None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество всех возможных значения для указанной позиции"""
    row_values = get_row(grid, pos)
    column_values = get_col(grid, pos)
    block_values = get_block(grid, pos)

    digits = {str(num) for num in range(1, 10)}
    used_values = set(row_values).union(column_values).union(block_values)
    remaining_values = digits - used_values

    return remaining_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Поиск решения для указанного пазла."""
    pos = find_empty_positions(grid)
    if not pos:
        return grid

    for value in find_possible_values(grid, pos):
        grid[pos[0]][pos[1]] = value
        if solve(grid):
            return grid
        grid[pos[0]][pos[1]] = "."
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""
    for index in range(9):
        current_col = get_col(solution, (0, index))
        current_row = get_row(solution, (index, 0))

        block_start_row = (index // 3) * 3
        block_start_col = (index % 3) * 3
        current_block = get_block(solution, (block_start_row, block_start_col))

        for number in range(1, 10):
            str_number = str(number)
            if str_number not in current_col:
                return False
            if str_number not in current_row:
                return False
            if str_number not in current_block:
                return False

    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов"""
    sudoku = [["."] * 9 for _ in range(9)]
    numbers = list("123456789")
    random.shuffle(numbers)

    for i in range(9):
        sudoku[i // 3 * 3 + i % 3][i] = numbers[i]

    if not solve(sudoku):
        return generate_sudoku(N)

    for _ in range(81 - N):
        i, j = random.randint(0, 8), random.randint(0, 8)
        while sudoku[i][j] == ".":
            i, j = random.randint(0, 8), random.randint(0, 8)
        sudoku[i][j] = "."

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
