a = float(input("Введите число a (1 < a <= 1,5): "))
n = 2
while 1 + 1 / n >= a:
    n = n + 1
print("Наименьшее n:", n)
