n = int(input("Введите натуральное число n: "))
s = 0
sign = 1
for k in range(1, n + 1):
    s = s + sign / k
    sign = -sign
print("Сумма =", s)
