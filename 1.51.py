x1 = float(input("Введите x1 (точка A): "))
y1 = float(input("Введите y1 (точка A): "))
x2 = float(input("Введите x2 (точка B): "))
y2 = float(input("Введите y2 (точка B): "))
x3 = float(input("Введите x3 (точка C): "))
y3 = float(input("Введите y3 (точка C): "))
x4 = float(input("Введите x4 (точка D): "))
y4 = float(input("Введите y4 (точка D): "))

s1 = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2  # треугольник ABC
s2 = abs((x3 - x1) * (y4 - y1) - (x4 - x1) * (y3 - y1)) / 2  # треугольник ACD
s = s1 + s2
print("Площадь четырехугольника =", s)
