n = int(input("Введите n (100 <= n <= 999): "))
b = n % 10
r = n // 10
x = r // 10 * 100 + b * 10 + r % 10
print("x =", x)
