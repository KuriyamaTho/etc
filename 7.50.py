n = int(input("Введите натуральное число n: "))
pos = 0
for i in range(1, n + 1):
    b = int(input(f"Введите b{i}: "))
    if b > 100:
        pos = i
print("Номер последнего числа, большего 100:", pos)
