import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
if a < b + c and b < a + c and c < a + b:
    s = sorted([a, b, c])
    if math.isclose(s[0] ** 2 + s[1] ** 2, s[2] ** 2):
        print("Да, треугольник прямоугольный")
    else:
        print("Нет, треугольник не прямоугольный")
else:
    print("Треугольника с такими сторонами не существует")
