n = int(input("Введите натуральное число n: "))
p = float(input("Введите p: "))
s = 0
for i in range(1, n + 1):
    b = int(input(f"Введите b{i}: "))
    s = s + b
if s < p:
    print("Да, сумма меньше p")
else:
    print("Нет, сумма не меньше p")
