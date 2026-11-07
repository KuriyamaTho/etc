import math

a = float(input("Введите a (a не равно 0): "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Два различных корня:")
    print("x1 =", x1)
    print("x2 =", x2)
elif d == 0:
    x = -b / (2 * a)
    print("Корни равны:")
    print("x1 = x2 =", x)
else:
    print("Вещественных корней нет")
