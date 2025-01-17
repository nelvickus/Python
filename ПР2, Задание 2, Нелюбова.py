def calculate_area(length, width):
    """Вычисляет площадь прямоугольника."""
    return length * width


areas = []# Список для хранения 


for i in range(1, 4):
    print(f"Введите размеры {i}-го прямоугольника:")
    length = float(input("Длина: "))
    width = float(input("Ширина: "))
    

    area = calculate_area(length, width)
    areas.append(area)

for i, area in enumerate(areas, start=1):
    print(f"Площадь {i}-го прямоугольника: {area:.2f}")
