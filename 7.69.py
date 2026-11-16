mx = 0
for i in range(1, 31):
    m = float(input(f"Введите массу тела {i}, кг: "))
    v = float(input(f"Введите объем тела {i}, см3: "))
    if m / v > mx:
        mx = m / v
print("Максимальная плотность материала, кг/см3:", mx)
