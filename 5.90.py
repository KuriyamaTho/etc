n = int(input("Введите n (1 < n <= 10): "))
f = 1
s = 1
for k in range(1, n + 1):
    f = f * k
    s = s + 1 / f
print("Сумма =", s)
