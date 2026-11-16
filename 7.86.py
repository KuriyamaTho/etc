s = 0
for i in range(1, 11):
    a = float(input(f"Введите a{i}: "))
    s = s + a
if s > 100.78:
    print("Да, сумма превышает 100,78")
else:
    print("Нет, сумма не превышает 100,78")
