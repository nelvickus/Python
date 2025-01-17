def split_array(arr):
    A_array = []  # положительныe 
    B_array = []  # неположительныe

    for number in arr:
        if number > 0:
            A_array.append(number)  
        else:
            B_array.append(number)  

    return A_array, B_array


N = int(input("Введите количество элементов в массиве: "))
array = []

for i in range(N):
    element = int(input(f"Введите элемент {i + 1}: "))
    array.append(element)


A, B = split_array(array # разделение массива

print("Положительные элементы:", A)
print("Неположительные элементы:", B)
