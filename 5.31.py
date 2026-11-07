n = int(input("Введите натуральное число n: "))
s = 0
for i in range(n, 2 * n + 1):
    s = s + i ** 2
print("Сумма =", s)
