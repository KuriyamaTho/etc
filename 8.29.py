a = int(input("Введите a: "))
b = int(input("Введите b: "))
k0 = int(input("Введите k: "))
for n in range(a, b + 1):
    k = 0
    for d in range(1, n + 1):
        if n % d == 0:
            k = k + 1
    if k == k0:
        print(n)
