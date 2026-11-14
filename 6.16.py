n = float(input("Введите число n: "))
s = 1
k = 1
while s <= n:
    k = k + 1
    s = s + 1 / k
print("Первое число, большее n:", s)
