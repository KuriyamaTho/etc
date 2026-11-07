n = int(input("Введите натуральное число n: "))
s = 0
for i in range(1, n + 1):
    s = s + 1 / i
print("Сумма =", s)
