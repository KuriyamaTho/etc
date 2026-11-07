import math

e = float(input("Введите e: "))
f = float(input("Введите f: "))
g = float(input("Введите g: "))
h = float(input("Введите h: "))
a = math.sqrt(abs(e - 3 / f) ** 3 + g)
b = math.sin(e) + math.cos(h) ** 2
c = 33 * g / (e * f - 3)
print("a =", a)
print("b =", b)
print("c =", c)
