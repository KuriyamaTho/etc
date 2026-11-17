def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


a = float(input("Введите вещественное число a: "))
n = int(input("Введите натуральное число n: "))
print(f"a^{n} =", power(a, n))
