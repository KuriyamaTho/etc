for n in range(1, 301):
    k = 0
    for d in range(1, n + 1):
        if n % d == 0:
            k = k + 1
    if k == 5:
        print(n)
