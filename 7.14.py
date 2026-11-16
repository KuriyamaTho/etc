s = 0
for i in range(1, 9):
    a = float(input(f"Введите a{i}: "))
    if a > 10.75:
        s = s + a
print("Сумма чисел, больших 10,75:", s)
