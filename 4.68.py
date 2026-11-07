import math

g = 9.8
alpha = float(input("Введите угол alpha, градусов: "))
v0 = float(input("Введите начальную скорость v0, м/с: "))
r = float(input("Введите расстояние до цели R, м: "))
h = float(input("Введите высоту нижней точки цели H, м: "))
p = float(input("Введите высоту цели P, м: "))
a = math.radians(alpha)
t = r / (v0 * math.cos(a))
y = v0 * t * math.sin(a) - g * t ** 2 / 2
if h <= y <= h + p:
    print("Снаряд поразит цель")
else:
    print("Снаряд не поразит цель")
