import math

g = 9.8
n = int(input("Введите количество выстрелов n: "))
r = float(input("Введите расстояние до цели R, м: "))
h = float(input("Введите высоту нижней точки цели H, м: "))
p = float(input("Введите высоту цели P, м: "))
hits = 0
for i in range(1, n + 1):
    alpha = float(input(f"Выстрел {i}, угол alpha, градусов: "))
    v0 = float(input(f"Выстрел {i}, начальная скорость v0, м/с: "))
    a = math.radians(alpha)
    t = r / (v0 * math.cos(a))
    y = v0 * t * math.sin(a) - g * t ** 2 / 2
    if h <= y <= h + p:
        hits = hits + 1
print("Процент попадания:", hits / n * 100)
