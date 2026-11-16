m = int(input("Введите натуральное число m: "))
n = int(input("Введите натуральное число n: "))
s = 0
for i in range(1, m + 1):
    s = s + i ** n
print("Сумма =", s)
