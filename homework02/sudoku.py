import pathlib
import random
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open(encoding="utf-8") as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    """Создать сетку Судоку из строки"""
    digits = [c for c in puzzle if c in "123456789."]
    return group(digits, 9)


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку"""
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print("".join(grid[row][col].center(width) + ("|" if col in {2, 5} else "") for col in range(9)))
        if row in {2, 5}:
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """Сгруппировать значения values в список из списков по n элементов"""
    return [values[i * n : (i + 1) * n] for i in range(len(values) // n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения строки для указанной позиции"""
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения столбца для указанной позиции"""
    return [row[pos[1]] for row in grid]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения блока, в который входит указанная позиция"""
    start_row, start_col = pos[0] // 3 * 3, pos[1] // 3 * 3
    return [grid[row][col] for row in range(start_row, start_row + 3) for col in range(start_col, start_col + 3)]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Находит первую свободную позицию в сетке"""
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == ".":
                return i, j
    return None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Возвращает множество возможных значений для указанной позиции"""
    all_values = set("123456789")
    used_values = set(get_row(grid, pos)) | set(get_col(grid, pos)) | set(get_block(grid, pos))
    return all_values - used_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решает Судоку"""
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
    """Проверяет корректность решения"""
    standard = set("123456789")
    for i in range(9):
        if set(get_row(solution, (i, 0))) != standard or set(get_col(solution, (0, i))) != standard:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if set(get_block(solution, (i, j))) != standard:
                return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерирует Судоку с N заполненными клетками"""
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
        if solution:
            display(solution)
        else:
            print(f"Puzzle {fname} can't be solved")
