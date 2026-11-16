import math

n = int(input("Введите количество квадратов: "))
s = float(input("Введите площадь квадрата 1: "))
mx = s
for i in range(2, n + 1):
    s = float(input(f"Введите площадь квадрата {i}: "))
    if s > mx:
        mx = s
print("Длина диагонали самого большого квадрата:", math.sqrt(2 * mx))
