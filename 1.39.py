import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = (x + (2 + y) / x ** 2) / (y + 1 / math.sqrt(x ** 2 + 10))
q = 2.8 * math.sin(x) + abs(y)
print("z =", z)
print("q =", q)
