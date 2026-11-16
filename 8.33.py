for n in range(50, 71):
    s = 0
    for d in range(1, n):
        if n % d == 0:
            s = s + d
    print(n, ":", s)
