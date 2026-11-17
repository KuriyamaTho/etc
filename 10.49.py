def index_of_maximum(a, n):
    if n == 1:
        return 1
    k = index_of_maximum(a, n - 1)
    if a[n - 1] > a[k - 1]:
        return n
    return k


n = int(input("Введите количество элементов массива n: "))
a = []
for i in range(1, n + 1):
    a.append(float(input(f"Введите a{i}: ")))
print("Индекс (номер) максимального элемента:", index_of_maximum(a, n))
