n = int(input("Введите количество предметов: "))
s = 0
for i in range(1, n + 1):
    m = float(input(f"Введите массу предмета {i}: "))
    s = s + m
print("Общая масса груза =", s)
