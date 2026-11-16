for a in range(2, 50000):
    s = 1
    d = 2
    while d * d <= a:
        if a % d == 0:
            s = s + d
            if d * d != a:
                s = s + a // d
        d = d + 1
    b = s
    if a < b < 50000:
        t = 1
        d = 2
        while d * d <= b:
            if b % d == 0:
                t = t + d
                if d * d != b:
                    t = t + b // d
            d = d + 1
        if t == a:
            print(a, b)
