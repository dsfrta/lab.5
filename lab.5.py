def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
from random import *

def create_matrix(rows, cols):
    matrix = [[randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
    return matrix

def print_matrix(matrix, title="матрица"):

    print(f"\n{title}:")
    for row in matrix:
        for elem in row:
            print(f"{elem:6.2f}", end=" ")
        print()

def to_triangular(matrix):
    n = len(matrix)
    m = len(matrix[0])
    tri_matrix = [row[:] for row in matrix]

    for i in range(min(n, m)):
        if tri_matrix[i][i] == 0:
            for k in range(i + 1, n):
                if tri_matrix[k][i] != 0:
                    tri_matrix[i], tri_matrix[k] = tri_matrix[k], tri_matrix[i]
                    break

        if tri_matrix[i][i] != 0:
            for j in range(i + 1, n):
                factor = tri_matrix[j][i] / tri_matrix[i][i]
                for k in range(i, m):
                    tri_matrix[j][k] -= factor * tri_matrix[i][k]

    for i in range(n):
        for j in range(m):
            tri_matrix[i][j] = round(tri_matrix[i][j], 2)

    return tri_matrix

def count_rows_less_than(matrix, value):
    count = 0
    for row in matrix:
        avg = sum(row) / len(row)
        if avg < value:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input("введите количество строк: "))
    m = int(input("введите количество столбов: "))

    mat = create_matrix(n, m)
    print_matrix(mat, "исходная матрица")

    tri_mat = to_triangular(mat)
    print_matrix(tri_mat, "треугольная матрица")

    val = float(input("\nвведите значение для сравнения величину: "))
    result = count_rows_less_than(tri_mat, val)
    print(f"количество строк где среднее меньше {val}: {result}")