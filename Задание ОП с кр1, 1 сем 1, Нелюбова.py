def a(A, B):
    if A < B:
        for num in range(A, B + 1):
            print(num)
    else:
        for num in range(A, B - 1, -1):
            print(num)

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
a(A, B)
