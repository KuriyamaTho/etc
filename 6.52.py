n = int(input("Введите натуральное число: "))
d = 2
while d * d <= n and n % d != 0:
    d = d + 1
if n > 1 and d * d > n:
    print("Да, число простое")
else:
    print("Нет, число не является простым")
