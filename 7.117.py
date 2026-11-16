n = int(input("Введите натуральное число n: "))
pos = 0
for i in range(1, n + 1):
    b = int(input(f"Введите b{i}: "))
    if b == 100:
        pos = i
if pos > 0:
    print("Номер последнего числа, равного 100:", pos)
else:
    print("Чисел, равных 100, среди заданных нет")
