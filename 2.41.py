import math

y = float(input("Введите y в радианах (0 < y <= 2*pi): "))
angle = 12 * y % (2 * math.pi)
print("Угол для минутной стрелки:", angle)
print("Число полных часов:", int(round(y * 6 / math.pi, 9)))
print("Число полных минут:", int(round(y * 360 / math.pi, 9)))
