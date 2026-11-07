n = int(input("Введите натуральное число n: "))
s = 0
for i in range(1, n + 1):
    a = float(input(f"Введите a{i}: "))
    s = s + a ** 2
print("Сумма квадратов =", s)
