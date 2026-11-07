import math

e = float(input("Введите e: "))
f = float(input("Введите f: "))
g = float(input("Введите g: "))
h = float(input("Введите h: "))
a = (e + f / 2) / 3
b = abs(h ** 2 - g)
c = math.sqrt((g - h) ** 2 - 3 * math.sin(e))
print("a =", a)
print("b =", b)
print("c =", c)
