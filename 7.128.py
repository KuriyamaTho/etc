n = int(input("Введите натуральное число: "))
s = 0
for i in range(1, n):
    if n % i == 0:
        s = s + i
if s == n:
    print("Да, число совершенное")
else:
    print("Нет, число не является совершенным")
