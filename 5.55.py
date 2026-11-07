n = int(input("Введите количество предметов в наборе: "))
s = 0
for i in range(1, n + 1):
    m = float(input(f"Введите массу предмета {i}: "))
    s = s + m
print("Средняя масса =", s / n)
