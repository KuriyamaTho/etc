n = int(input("Введите натуральное число n: "))
neg = 0
pos = 0
for i in range(1, n + 1):
    a = float(input(f"Введите a{i}: "))
    if a < 0:
        neg = neg + 1
    if a > 0:
        pos = pos + 1
print("Количество отрицательных чисел:", neg)
print("Количество положительных чисел:", pos)
