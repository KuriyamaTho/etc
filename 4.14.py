import math

a = float(input("Введите a (a не равно 0): "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = b ** 2 - 4 * a * c
if d >= 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
else:
    print("Вещественных корней нет")
