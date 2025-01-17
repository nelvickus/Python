N = int(input("Введите количество элементов в массиве: "))

array = []
for i in range(N):
    element = int(input(f"Введите элемент {i + 1}: "))
    array.append(element)


min_value = array[0]
min_index = 0

for i in range(1, N):
    if array[i] < min_value:
        min_value = array[i]
        min_index = i


print(f"Индекс минимального элемента: {min_index}")
