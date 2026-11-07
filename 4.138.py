n = int(input("Введите n (1 <= n <= 32): "))
if n == 1:
    digit = 0
elif n <= 10:
    digit = n - 1
else:
    m = n - 10
    number = 10 + (m - 1) // 2
    if m % 2 == 1:
        digit = number // 10
    else:
        digit = number % 10
print("Цифра с номером n:", digit)
