def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("Введите числитель a: "))
b = int(input("Введите знаменатель b: "))
d = gcd(a, b)
print("Сокращенная дробь:", f"{a // d}/{b // d}")
