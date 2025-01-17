def is_magic_square(matrix):
    n = len(matrix)
    
   
    magic_sum = sum(matrix[0]) # сумма первой строки
    
   
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    
  
    for col in range(n):  #  сумма столбцов
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False

    
    if sum(matrix[i][i] for i in range(n)) != magic_sum:#  сумма главной диагонали
        return False


    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:    # сумма побочной диагонали
        return False

    return True


if __name__ == "__main__":
    
    n = int(input("Введите порядок матрицы (n): "))
    
    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)

    if is_magic_square(matrix):
        print("Матрица является магическим квадратом.")
    else:
        print("Матрица не является магическим квадратом.")
