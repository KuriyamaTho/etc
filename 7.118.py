k = int(input("Введите натуральное число k: "))
pos = 0
for i in range(1, k + 1):
    a = int(input(f"Введите a{i}: "))
    if a < 0:
        pos = i
if pos > 0:
    print("Номер последнего отрицательного числа:", pos)
else:
    print("Отрицательных чисел среди заданных нет")
