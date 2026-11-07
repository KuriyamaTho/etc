import math

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))

ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
bc = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
ca = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
p = ab + bc + ca
s = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
print("Периметр =", p)
print("Площадь =", s)
