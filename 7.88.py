s = 0
for i in range(1, 10):
    a = int(input(f"Введите a{i}: "))
    s = s + a
if s % 2 == 0:
    print("Да, сумма - четное число")
else:
    print("Нет, сумма - нечетное число")
