def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))
print("НОК =", a * b // gcd(a, b))
