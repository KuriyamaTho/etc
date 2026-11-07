import math

r = float(input("Введите радиус круга: "))
a = float(input("Введите сторону квадрата: "))
s1 = math.pi * r ** 2
s2 = a ** 2
if s1 > s2:
    print("Площадь больше у круга")
elif s1 < s2:
    print("Площадь больше у квадрата")
else:
    print("Площади равны")
