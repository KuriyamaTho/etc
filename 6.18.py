a = float(input("Введите вещественное число a: "))
s = 1
n = 1
while s <= a:
    n = n + 1
    s = s + 1 / n
print("Наименьшее n:", n)
