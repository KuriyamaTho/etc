k = int(input("Введите натуральное число k: "))
pos = 0
for i in range(1, k + 1):
    a = int(input(f"Введите a{i}: "))
    if a < 0:
        pos = i
print("Номер последнего отрицательного числа:", pos)
