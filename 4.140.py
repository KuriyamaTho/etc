k = int(input("Введите k (1 <= k <= 222): "))
if k <= 9:
    digit = k
elif k <= 189:
    m = k - 9
    number = 10 + (m - 1) // 2
    if m % 2 == 1:
        digit = number // 10
    else:
        digit = number % 10
else:
    m = k - 189
    number = 100 + (m - 1) // 3
    p = (m - 1) % 3
    if p == 0:
        digit = number // 100
    elif p == 1:
        digit = number // 10 % 10
    else:
        digit = number % 10
print("k-я цифра:", digit)
