import pathlib
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
    array = [values[i*n: i*n + n] for i in range(len(values) // n)]
    return array

def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row_values = grid[pos[0]]
    return row_values


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    col_values = [grid[i][pos[-1]] for i in range(len(grid))]
    return col_values
    


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
    
    row = pos[0]
    col = pos[-1]
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    block = [grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]
    return block



def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    pos = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                pos.append(i)
                pos.append(j)
                return tuple(pos)
    else:
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
    val = '123456789'

    square = get_block(grid, pos)
    square = ''.join(square)
    square_set = set(square.replace('.', ''))

    row = ''.join(get_row(grid, pos))
    row_set = set(row.replace('.', ''))

    col = ''.join(get_col(grid, pos))
    col_set = set(col.replace('.', ''))

    existing_values = square_set.union(row_set, col_set)

    potential_values = set()
    for num in val:
        if num not in existing_values:
            potential_values.add(num)
    if potential_values == set():
        return None
    return potential_values
    

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


    pos = find_empty_positions(grid)
    if pos == None:
        return grid
    else:
        potential_values = find_possible_values(grid, pos)
        if potential_values == None:
            return None
        
        for num in potential_values:
            grid[pos[0]][pos[-1]] = num
            res = solve(grid)
            if res == None:
                grid[pos[0]][pos[-1]] = '.'
            else:
                return res


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False

    >>> check_solution([
    ... ["5", "5", "4", "6", "7", "8", "9", "1", "2"],
    ... ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ... ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ... ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ... ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ... ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ... ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ... ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ... ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ... ])
    False
    >>> check_solution([
    ... ["5", "3", "4", "1", "7", "8", "9", "1", "2"],
    ... ["6", "7", "2", "1", "9", "5", "6", "4", "8"],
    ... ["1", "9", "8", "3", "4", "5", "6", "7", "9"],
    ... ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ... ["4", "9", "9", "9", "9", "7", "9", "9", "1"],
    ... ["7", "1", "3", "9", "2", "2", "8", "5", "6"],
    ... ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ... ["2", "8", "7", "4", "1", "9", "9", "3", "5"],
    ... ["7", "4", "5", "2", "8", "6", "1", "7", "4"],
    ... ])
    False

    """
    val_0 = tuple('123456789')
    for i in range(9):
        pos = (i, i)
        row = get_row(solution, pos)
        col = get_col(solution, pos)
        block = get_block(solution, pos)

        val = list(val_0)
        for element in row:
            try:
                val.pop(val.index(element))
            except ValueError:
                return False

        val = list(val_0)
        for element_col in col:
            try:
                val.pop(val.index(element_col))
            except ValueError:
                return False

        val = list(val_0)
        for element in block:
            try:
                val.pop(val.index(element))
            except ValueError:
                return False
    else:
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
    import random

    correct_grid = tuple([
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ])
    
    returned_grid = list(correct_grid)

    while 81 - N > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if returned_grid[row][col] != '.':
            returned_grid[row][col] = '.'
            N += 1
    return returned_grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)