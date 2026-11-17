def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
print("НОД =", gcd(gcd(a, b), c))
