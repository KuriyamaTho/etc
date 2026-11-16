for n in range(300, 601):
    s = 0
    for d in range(1, n):
        if n % d == 0:
            s = s + d
    if s % 10 == 0:
        print(n)
