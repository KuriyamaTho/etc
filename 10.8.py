def has_real_roots(a, b, c):
    return b ** 2 - 4 * a * c >= 0


a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
k = 0
if has_real_roots(a, b, c):
    k = k + 1
if has_real_roots(b, a, c):
    k = k + 1
if has_real_roots(c, a, b):
    k = k + 1
print("Количество уравнений с вещественными корнями:", k)
