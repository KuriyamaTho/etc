k = int(input("Введите k (1 <= k <= 252): "))
if k <= 100:
    number = 50 + (k - 1) // 2
    if k % 2 == 1:
        digit = number // 10
    else:
        digit = number % 10
else:
    m = k - 100
    number = 100 + (m - 1) // 3
    p = (m - 1) % 3
    if p == 0:
        digit = number // 100
    elif p == 1:
        digit = number // 10 % 10
    else:
        digit = number % 10
print("k-я цифра:", digit)
