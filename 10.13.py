def is_square(n):
    if n < 0:
        return False
    r = 0
    while r * r < n:
        r = r + 1
    return r * r == n


n = int(input("Введите натуральное число n: "))
k = 0
for i in range(1, n + 1):
    a = int(input(f"Введите a{i}: "))
    if is_square(a):
        k = k + 1
print("Количество полных квадратов:", k)
