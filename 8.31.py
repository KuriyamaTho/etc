for n in range(100, 1000):
    prime = True
    for d in range(2, n):
        if d * d > n:
            break
        if n % d == 0:
            prime = False
            break
    if prime:
        print(n)
