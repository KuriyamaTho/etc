def maximum(a, n):
    if n == 1:
        return a[0]
    m = maximum(a, n - 1)
    if a[n - 1] > m:
        return a[n - 1]
    return m


n = int(input("Введите количество элементов массива n: "))
a = []
for i in range(1, n + 1):
    a.append(float(input(f"Введите a{i}: ")))
print("Максимальный элемент:", maximum(a, n))
