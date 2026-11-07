import math

a = float(input("Введите большее основание: "))
b = float(input("Введите меньшее основание: "))
alpha = float(input("Введите угол при большем основании (в градусах): "))
h = (a - b) / 2 * math.tan(math.radians(alpha))  # высота трапеции
s = (a + b) / 2 * h
print("Площадь трапеции =", s)
