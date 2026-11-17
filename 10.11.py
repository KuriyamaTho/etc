def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2


x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))
x4 = float(input("Введите x4: "))
y4 = float(input("Введите y4: "))
x5 = float(input("Введите x5: "))
y5 = float(input("Введите y5: "))
s = triangle_area(x1, y1, x2, y2, x3, y3) + triangle_area(x1, y1, x3, y3, x4, y4) + triangle_area(x1, y1, x4, y4, x5, y5)
print("Площадь пятиугольника:", s)
