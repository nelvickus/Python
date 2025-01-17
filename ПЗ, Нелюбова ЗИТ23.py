def read_matrix(file):
    matrix = []
    for line in file:
        line = line.strip()
        if line:  # Если строка не пустая
            row = list(map(int, line.split()))
            matrix.append(row)
        else:  # Пустая строка, конец матрицы
            break
    return matrix

def write_matrix(file, matrix):
    for row in matrix:
        file.write(' '.join(map(str, row)) + '\n')
    file.write('\n')  

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def main():
    input_file_name = "НелюбоваВА_группаЗИТ23_vvod.txt"
    
    with open(input_file_name, 'r') as file:
        matrix1 = read_matrix(file)
        matrix2 = read_matrix(file)

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Размеры матриц не совпадают!")
        return


    result_matrix = add_matrices(matrix1, matrix2)


    with open(input_file_name, 'w') as file:
        file.write("Первая матрица:\n")
        write_matrix(file, matrix1)
        
        file.write("Вторая матрица:\n")
        write_matrix(file, matrix2)
        
        file.write("Результат (Сумма матриц):\n")
        write_matrix(file, result_matrix)

if __name__ == "__main__":
    main()
