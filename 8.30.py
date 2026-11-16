a = int(input("Введите a: "))
b = int(input("Введите b: "))
best = 0
max_number = 0
min_number = 0
for n in range(a, b + 1):
    k = 0
    for d in range(1, n + 1):
        if n % d == 0:
            k = k + 1
    if k > best:
        best = k
        max_number = n
        min_number = n
    elif k == best:
        max_number = n
print("Максимальное количество делителей:", best)
print("а) Максимальное из чисел с таким количеством делителей:", max_number)
print("б) Минимальное из чисел с таким количеством делителей:", min_number)
