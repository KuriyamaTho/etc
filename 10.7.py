import math


def trapezoid_perimeter(a, b, h):
    return a + b + 2 * math.sqrt(h ** 2 + ((a - b) / 2) ** 2)


a1 = float(input("Первая трапеция, основание a: "))
b1 = float(input("Первая трапеция, основание b: "))
h1 = float(input("Первая трапеция, высота h: "))
a2 = float(input("Вторая трапеция, основание a: "))
b2 = float(input("Вторая трапеция, основание b: "))
h2 = float(input("Вторая трапеция, высота h: "))
print("Сумма периметров:", trapezoid_perimeter(a1, b1, h1) + trapezoid_perimeter(a2, b2, h2))
