import math

def area_of_triangle(a):
    """Вычисляет площадь равностороннего треугольника со стороной a."""
    return (math.sqrt(3) / 4) * (a ** 2)

def area_of_hexagon(a):
    """Вычисляет площадь правильного шестиугольника со стороной a."""
    triangle_area = area_of_triangle(a)
    return 6 * triangle_area

side_length = float(input("Введите длину стороны правильного шестиугольника: "))# Ввод стороны шестиугольника

hexagon_area = area_of_hexagon(side_length)# Вычисление площади шестиугольника

print(f"Площадь правильного шестиугольника со стороной {side_length} равна: {hexagon_area:.2f}")
