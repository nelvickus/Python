def swap_first_last_column(matrix):
    n = len(matrix)
    
    for i in range(n):
        matrix[i][0], matrix[i][n - 1] = matrix[i][n - 1], matrix[i][0]

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    n = int(input("Введите количество строк и столбцов (N): "))
    
    matrix = []
    print("Введите элементы матрицы построчно(через пробел:")
    for i in range(n):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)

    print("Исходная матрица:")
    print_matrix(matrix)

    swapped_matrix = swap_first_last_column(matrix)

    print("Матрица после перестановки первого и последнего столбцов:")
    print_matrix(swapped_matrix)
