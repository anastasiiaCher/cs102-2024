from cmath import sqrt
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
    c = 0
    two_dim = [ values[c:c+n] for c in range( 0, len(values), n ) ]

   
    return two_dim


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    
    d = pos[0]
   
    element = grid[d]
    return element


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    e = pos[1]
    n = len(grid)
    grid_B = []
    k = 0
    for k in range (0,n):
        grid_T = [ grid[i][k] for i in range (0,n)]
        grid_B.append(grid_T)
    element = grid_B [e] 
    return element


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
    grid_A = []
    grid_B = []
    grid_C = []
    n = len(grid)
    n_2 =  int(len(grid)**0.5)
    i = 0
    
  
    for d in range (i, i+n_2):
        t = i
        if i>= (n*n_2):
            break
        for a in range (0, n,n_2):
            for c in range(t, t+n_2) :
                grid_A = grid[c][a:a+n_2] 
                grid_B += grid_A  
        i+=n_2

    grid_C = [grid_B[b : b+int(len((grid_B))**0.5)] for b in range (0, len(grid_B), int(len((grid_B))**0.5)) ]  
    i = pos[0]
    j = pos[1]
    n2 = len(grid_C)
    n2_2 = n2**0.5

    t = i*j
    t_2 = int(t**0.5)

    element = grid_C[t_2]


    # for t in range(0,n2,n2_2) and c in range(0,n_2):
    #     if i in range(t, t+n_2):
    #         i_2 = c
    #         break
    #     else:
    #         continue

    # for t in range(0,n2,n2_2) and c in range(0,n_2):
    #     if j in range(t, t+n_2):
    #         j_2 = c
    #         break
    #     else:
    #         continue    

    return element





def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
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
    pass


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    pass


# def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
#     """Генерация судоку заполненного на N элементов
#     >>> grid = generate_sudoku(40)
#     >>> sum(1 for row in grid for e in row if e == '.')
#     41
#     >>> solution = solve(grid)
#     >>> check_solution(solution)
#     True
#     >>> grid = generate_sudoku(1000)
#     >>> sum(1 for row in grid for e in row if e == '.')
#     0
#     >>> solution = solve(grid)
#     >>> check_solution(solution)
#     True
#     >>> grid = generate_sudoku(0)
#     >>> sum(1 for row in grid for e in row if e == '.')
#     81
#     >>> solution = solve(grid)
#     >>> check_solution(solution)
#     True
#     """
#     pass


# if __name__ == "__main__":
#     for fname in ["homework02/puzzle1.txt", "homework02/puzzle2.txt", "homework02/puzzle3.txt"]:
#         grid = read_sudoku(fname)
#         display(grid)
#         solution = solve(grid)
#         if not solution:
#             print(f"Puzzle {fname} can't be solved")
#         else:
#             display(solution)