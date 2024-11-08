from typing import List, Optional
from copy import deepcopy


def validate_matrix(matrix):
    assert isinstance(matrix, list), "Входная матрица должна быть списком"
    assert len(matrix) > 0, "Входная матрица не должна быть пустой"
    assert all(isinstance(row, list) for row in matrix), "Каждая строка в матрице должна быть списком"
    assert all(len(row) == len(matrix[0]) for row in matrix), "Все строки в матрице должны быть одинаковой длины"


def scalar_multiplication(
    matrix: List[List[float]], scalar: float, copy: bool = True
) -> Optional[
    List[List[float]]
]:  # Необходимость создания копии матрицы перед совершением операций над ней определяет значение параметра copy
    validate_matrix(matrix)
    if copy:
        return [[element * scalar for element in row] for row in matrix]
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] *= scalar
        return matrix


def matrix_addition(
    matrix1: List[List[float]], matrix2: List[List[float]]
) -> List[List[float]]:  # Матрицы должны иметь одинаковые размеры, не забудьте проверить это
    validate_matrix(matrix1)
    validate_matrix(matrix2)
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны быть одинакового размера")
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] += matrix1[i][j] + matrix2[i][j]
    return result


def matrix_transposition(matrix: List[List[float]]) -> List[List[float]]:
    validate_matrix(matrix)
    transposed = [[matrix[j][i] for j in range(3)] for i in range(3)]
    return transposed


def matrix_multiplication(
    matrix1: List[List[float]], matrix2: List[List[float]]
) -> List[
    List[float]
]:  # Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице, не забудьте проверить это
    validate_matrix(matrix1)
    validate_matrix(matrix2)
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Количество столбцов первой матрицы должно быть равно количеству столбцов второй матрицы.")
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


print("Умножение на скаляр:")
result = scalar_multiplication(matrix1, 2, copy=True)
for row in result:
    print(row)

print("Сложение матриц:")
result = matrix_addition(matrix1, matrix2)
for row in result:
    print(row)

print("Произведение матриц:")
result = matrix_multiplication(matrix1, matrix2)
for row in result:
    print(row)

print("Транспонирование матрицы:")
result = matrix_transposition(matrix1)
for row in result:
    print(row)
