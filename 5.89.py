n = int(input("Введите n (1 < n <= 10): "))
f = 1
s = 0
for k in range(1, n + 1):
    f = f * k
    s = s + f
print("Сумма =", s)
