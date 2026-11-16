m = int(input("Введите количество чисел m: "))
best = 0
cur = 0
for i in range(1, m + 1):
    a = int(input(f"Введите число {i} (0 или 1): "))
    if a == 0:
        cur = cur + 1
    else:
        if cur > 0 and (best == 0 or cur < best):
            best = cur
        cur = 0
if cur > 0 and (best == 0 or cur < best):
    best = cur
if best > 0:
    print("Наименьшая длина отрезка из одних нулей:", best)
else:
    print("В последовательности нет нулей")
