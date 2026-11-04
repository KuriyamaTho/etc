import math

r1 = float(input("Введите внешний радиус: "))
r2 = float(input("Введите внутренний радиус: "))
s = math.pi * (r1 ** 2 - r2 ** 2)
print("Площадь кольца =", s)
