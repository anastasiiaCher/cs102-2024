import pathlib
import random
import time
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    """Создать Судоку"""
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
    res: tp.List[tp.List[T]] = [[] for _ in range(n)]
    for idx, val in enumerate(values):
        res[idx // n].append(val)
    return res


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
    return [row[pos[1]] for row in grid]


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
    return [
        grid[i][j]
        for i in range(pos[0] // 3 * 3, pos[0] // 3 * 3 + 3)
        for j in range(pos[1] // 3 * 3, pos[1] // 3 * 3 + 3)
    ]


def find_empty_positions(
    grid: tp.List[tp.List[str]],
) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    empty_positions = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "."]
    return empty_positions[0] if empty_positions else None


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
    return set(str(i) for i in range(1, 10)) - (
        set(get_row(grid, pos)) | set(get_col(grid, pos)) | set(get_block(grid, pos))
    )


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
    if empty_pos:
        possible_values = find_possible_values(grid, empty_pos)
        if possible_values:
            for i in possible_values:
                grid[empty_pos[0]][empty_pos[1]] = i
                res = solve(grid)
                if res:
                    return res
            grid[empty_pos[0]][empty_pos[1]] = "."
        else:
            return None
    else:
        return grid
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""
    rset = set(str(i) for i in range(1, 10))
    rows = [set(i) == rset for i in solution]
    columns = [set(get_col(solution, (0, i))) == rset for i in range(9)]
    blocks = [set(get_block(solution, (i * 3, j * 3))) == rset for i in range(3) for j in range(3)]
    return all(rows + columns + blocks)


def transpose(grid: tp.List[tp.List[str]]) -> tp.List[tp.List[str]]:
    """Транспонирует матрицу"""
    grid_t: tp.List[tp.List[str]] = []
    for i in range(len(grid[0])):
        grid_t.append([])
        for j in range(len(grid)):
            grid_t[i].append(grid[j][i])
    return grid_t


def swap_rows(grid: tp.List[tp.List[str]]) -> tp.List[tp.List[str]]:
    """Меняет местами две строки в пределах одного района"""
    area_start = random.randint(0, 2)
    row1 = random.randint(0, 2)
    row2 = random.randint(0, 2)
    while row2 == row1:
        row2 = random.randint(0, 2)

    area = grid[area_start * 3 : area_start * 3 + 3]
    area[row1], area[row2] = area[row2], area[row1]
    grid[area_start * 3 : area_start * 3 + 3] = area
    return grid


def swap_cols(grid: tp.List[tp.List[str]]) -> tp.List[tp.List[str]]:
    """Меняет местами два столбца в пределах одного района"""
    area_start = random.randint(0, 2)
    col1 = random.randint(0, 2)
    col2 = random.randint(0, 2)
    while col2 == col1:
        col2 = random.randint(0, 2)

    grid = transpose(grid)
    area = grid[area_start * 3 : area_start * 3 + 3]
    area[col1], area[col2] = area[col2], area[col1]
    grid[area_start * 3 : area_start * 3 + 3] = area
    return transpose(grid)


def swap_rows_area(grid: tp.List[tp.List[str]]) -> tp.List[tp.List[str]]:
    """Меняет местами два района по горизонтали"""
    n_area1 = random.randint(0, 2)
    n_area2 = random.randint(0, 2)
    while n_area2 == n_area1:
        n_area2 = random.randint(0, 2)

    area1 = grid[n_area1 * 3 : n_area1 * 3 + 3]
    area2 = grid[n_area2 * 3 : n_area2 * 3 + 3]

    grid[n_area1 * 3 : n_area1 * 3 + 3], grid[n_area2 * 3 : n_area2 * 3 + 3] = (
        area2,
        area1,
    )
    return grid


def swap_cols_area(grid: tp.List[tp.List[str]]) -> tp.List[tp.List[str]]:
    """Меняет местами два района по вертикали"""
    n_area1 = random.randint(0, 2)
    n_area2 = random.randint(0, 2)
    while n_area2 == n_area1:
        n_area2 = random.randint(0, 2)

    grid = transpose(grid)
    area1 = grid[n_area1 * 3 : n_area1 * 3 + 3]
    area2 = grid[n_area2 * 3 : n_area2 * 3 + 3]

    grid[n_area1 * 3 : n_area1 * 3 + 3], grid[n_area2 * 3 : n_area2 * 3 + 3] = (
        area2,
        area1,
    )
    return transpose(grid)


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
    grid = [
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

    moves = ["transpose", "swap_rows", "swap_cols", "swap_rows_area", "swap_cols_area"]

    for _ in range(random.randint(0, 10)):
        move = moves[random.randint(0, 4)]
        if move == "transpose":
            grid = transpose(grid)
        elif move == "swap_rows":
            grid = swap_rows(grid)
        elif move == "swap_cols":
            grid = swap_cols(grid)
        elif move == "swap_rows_area":
            grid = swap_rows_area(grid)
        elif move == "swap_cols_area":
            grid = swap_cols_area(grid)

    N = 81 - min(81, N)
    pos_list = [(i, j) for i in range(9) for j in range(9)]

    for _ in range(N):
        pos = pos_list[random.randint(0, len(pos_list) - 1)]
        while grid[pos[0]][pos[1]] == ".":
            pos = pos_list[random.randint(0, len(pos_list) - 1)]
        grid[pos[0]][pos[1]] = "."
    return grid


if __name__ == "__main__":
    for filename in ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt"):
        grid = read_sudoku(filename)
        start = time.time()
        solve(grid)
        end = time.time()
        print(f"{filename}: {end-start}")
