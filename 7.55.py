n = int(input("Введите количество спортсменов: "))
for i in range(1, n + 1):
    t = float(input(f"Введите результат спортсмена {i}: "))
    if i == 1 or t < best:
        best = t
    print("Лучший результат:", best)
