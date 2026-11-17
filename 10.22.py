def max2(x, y):
    if x > y:
        return x
    return y


a1 = float(input("Введите число 1: "))
a2 = float(input("Введите число 2: "))
a3 = float(input("Введите число 3: "))
a4 = float(input("Введите число 4: "))
a5 = float(input("Введите число 5: "))
a6 = float(input("Введите число 6: "))
m = max2(max2(max2(a1, a2), max2(a3, a4)), max2(a5, a6))
print("Максимальное число:", m)
