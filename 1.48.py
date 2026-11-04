import math

a = float(input("Введите большее основание: "))
b = float(input("Введите меньшее основание: "))
h = float(input("Введите высоту: "))
c = math.sqrt(h ** 2 + ((a - b) / 2) ** 2)  # боковая сторона
p = a + b + 2 * c
print("Периметр трапеции =", p)
