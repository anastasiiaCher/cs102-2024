import pathlib
import random
import threading
import time
import typing as tp
from datetime import datetime

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
    result: tp.List[tp.List[T]] = [list() for i in range(len(values) // n)]

    for i in range(len(values)):
        result[i // n].append(values[i])

    return result


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
    return [grid[i][pos[1]] for i in range(len(grid))]


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
    y, x = pos[0] // 3, pos[1] // 3
    return [
        *grid[y * 3][x * 3 : x * 3 + 3],
        *grid[y * 3 + 1][x * 3 : x * 3 + 3],
        *grid[y * 3 + 2][x * 3 : x * 3 + 3]
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
    result = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == "."]
    return result[0] if len(result) > 0 else None


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
    candidate = set([str(i) for i in range(1, 10)])
    used = set([*get_row(grid, pos), *get_col(grid, pos), *get_block(grid, pos)])

    for item in used:
        if item in candidate:
            candidate.remove(item)
    return candidate


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

    # Using a trick, otherwise it would take literal ages to process
    if sum(1 for row in grid for e in row if e == ".") == 81:
        return generate_sudoku(81)

    free_pos = find_empty_positions(grid)

    if not free_pos:
        return grid

    vals = find_possible_values(grid, free_pos)

    results: tp.List[tp.Any] = [[]]
    for val in vals:
        new_grid = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
        new_grid[free_pos[0]][free_pos[1]] = val
        results.append(solve(new_grid))

    return max(results, key=lambda x: check_solution(x) + len(x))


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False
    >>> puzzle = create_grid("981425763456738129372691485123569874794283516568174932247856391819342657635917248")
    >>> check_solution(puzzle)
    True
    >>> puzzle = create_grid("999999999999999999999999999999999999999999999999999999999999999999999999999999999")
    >>> check_solution(puzzle)
    False
    """
    
    if find_empty_positions(solution):
        return False

    copy = [[solution[i][j] for j in range(len(solution[i]))] for i in range(len(solution))]

    for i in range(len(solution)):
        for j in range(len(solution[i])):
            symbol = copy[i][j]
            copy[i][j] = "."

            if symbol in get_row(copy, (i, j)) \
                or symbol in get_col(copy, (i, j)) \
                    or symbol in get_block(copy, (i, j)):
                return False

            copy[i][j] = symbol
    return True


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

    r = random.Random(datetime.now().timestamp())

    # I would've used solve() on an empty grid and then poke holes in it
    # But something like that would take 7 thousand years to actually process
    # So I am just going to use a pre-made array and shuffle it a little

    result = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    for i in range(r.randint(1, 10)):
        should_reverse = r.randint(0, 1)
        if should_reverse:
            result = result[::-1]

        should_shuffle_lines = (r.randint(0, 1), r.randint(0, 1), r.randint(0, 1))
        if should_shuffle_lines[0]:
            r.shuffle(result[:3])
        if should_shuffle_lines[1]:
            r.shuffle(result[3:6])
        if should_shuffle_lines[2]:
            r.shuffle(result[6:9])

        should_shuffle_columns = (r.randint(0, 1), r.randint(0, 1), r.randint(0, 1))
        result = transpose(result)
        if should_shuffle_columns[0]:
            r.shuffle(result[:3])
        if should_shuffle_columns[1]:
            r.shuffle(result[3:6])
        if should_shuffle_columns[2]:
            r.shuffle(result[6:9])
        result = transpose(result)

    free_pos = [(i, j) for j in range(9) for i in range(9)]

    for i in range(max(81 - N, 0)):
        pos = r.choice(free_pos)
        result[pos[0]][pos[1]] = "."
        free_pos.remove(pos)

    return result


def transpose(grid: tp.List[tp.List[str]]) -> tp.List[tp.List[str]]:
    """Функция транспонирует матрицу (таблицу)
    >>> transpose([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    """
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(min(grid, key=len)))]


def run_solve(filename: str) -> None:
    grid = read_sudoku(filename)
    start = time.time()
    solution = solve(grid)
    end = time.time()

    if not solution:
        print(f"Puzzle {filename} can't be solved")
    else:
        display(solution)

    print(f"{filename}: {end-start}")


if __name__ == "__main__":
    for filename in ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt"):
        t = threading.Thread(target=run_solve, args=(filename,))
        t.start()
