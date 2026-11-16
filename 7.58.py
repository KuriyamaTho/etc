import math

n = int(input("Введите количество кругов: "))
s = float(input("Введите площадь круга 1: "))
mn = s
for i in range(2, n + 1):
    s = float(input(f"Введите площадь круга {i}: "))
    if s < mn:
        mn = s
print("Радиус самого маленького круга:", math.sqrt(mn / math.pi))
