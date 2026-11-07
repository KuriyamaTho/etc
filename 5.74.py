import math

r = 50
v = 0
for i in range(12):
    outer = r + 5
    v = v + 4 / 3 * math.pi * (outer ** 3 - r ** 3)
    r = outer
print("Суммарный объем шаров, л:", v / 1000000)
