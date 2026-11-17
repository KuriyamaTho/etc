def is_prime(n, d=2):
    if n < 2:
        return False
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return is_prime(n, d + 1)


n = int(input("Введите натуральное число: "))
if is_prime(n):
    print("Да, число простое")
else:
    print("Нет, число не является простым")
