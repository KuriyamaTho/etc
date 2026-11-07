x = float(input("Введите x: "))
n = int(input("Введите n (1 < n <= 10): "))
f = 1
p = 1
s = 1
for k in range(1, n + 1):
    f = f * k
    p = p * x
    s = s + p / f
print("Сумма =", s)
