import math

n = int(input("Введите натуральное число: "))
prime = n > 1
for d in range(2, math.isqrt(n) + 1):
    if n % d == 0:
        prime = False
if prime:
    print("Да, число простое")
else:
    print("Нет, число не является простым")
