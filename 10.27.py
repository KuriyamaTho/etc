def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


n = int(input("Введите количество чисел n: "))
d = int(input("Введите число 1: "))
for i in range(2, n + 1):
    x = int(input(f"Введите число {i}: "))
    d = gcd(d, x)
print("НОД =", d)
