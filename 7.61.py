n = int(input("Введите количество участников: "))
t = float(input("Введите результат участника 1: "))
best = t
pos = 1
for i in range(2, n + 1):
    t = float(input(f"Введите результат участника {i}: "))
    if t < best:
        best = t
        pos = i
print("Лучший результат показал лыжник, стартовавший по счету:", pos)
