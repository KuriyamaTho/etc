import math


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


ab = float(input("Введите длину AB: "))
ac = float(input("Введите длину AC: "))
dc = float(input("Введите длину DC: "))
bc = hypotenuse(ab, ac)
bd = hypotenuse(bc, dc)
print("Периметр фигуры ABCD:", ab + bd + dc + ac)
