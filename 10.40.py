import math


def trapezoid(a, b, h):
    side = math.sqrt(h ** 2 + ((a - b) / 2) ** 2)
    return a + b + 2 * side, (a + b) / 2 * h


a1 = float(input("Первая трапеция, основание a: "))
b1 = float(input("Первая трапеция, основание b: "))
h1 = float(input("Первая трапеция, высота h: "))
a2 = float(input("Вторая трапеция, основание a: "))
b2 = float(input("Вторая трапеция, основание b: "))
h2 = float(input("Вторая трапеция, высота h: "))
p1, s1 = trapezoid(a1, b1, h1)
p2, s2 = trapezoid(a2, b2, h2)
print("Сумма периметров:", p1 + p2)
print("Сумма площадей:", s1 + s2)
