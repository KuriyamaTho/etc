import math


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))
e = float(input("Введите e: "))
f = float(input("Введите f: "))
g = float(input("Введите g: "))
print("Площадь пятиугольника:", triangle_area(a, b, g) + triangle_area(g, c, f) + triangle_area(f, d, e))
