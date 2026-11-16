for n in range(2, 100000):
    s = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            s = s + d
            if d * d != n:
                s = s + n // d
        d = d + 1
    if s == n:
        print(n)
