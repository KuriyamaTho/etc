def is_power_of_five(n):
    if n < 1:
        return False
    while n % 5 == 0:
        n = n // 5
    return n == 1


n = int(input("Введите натуральное число n: "))
k = 0
for i in range(1, n + 1):
    a = int(input(f"Введите a{i}: "))
    if is_power_of_five(a):
        k = k + 1
print("Количество степеней пятерки:", k)
