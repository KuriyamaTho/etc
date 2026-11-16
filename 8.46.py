n = int(input("Введите количество чисел n: "))
g = int(input("Введите число 1: "))
for i in range(2, n + 1):
    x = int(input(f"Введите число {i}: "))
    a = g
    b = x
    while b != 0:
        r = a % b
        a = b
        b = r
    g = a
print("НОД =", g)
