s = 0
for day in range(1, 32):
    x = float(input(f"Январь, осадки за день {day}: "))
    s = s + x
print("Среднедневное количество осадков за январь =", s / 31)

s = 0
for day in range(1, 32):
    x = float(input(f"Март, осадки за день {day}: "))
    s = s + x
print("Среднедневное количество осадков за март =", s / 31)
