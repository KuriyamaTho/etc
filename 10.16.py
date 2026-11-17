def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True


for p in range(2, 199):
    if is_prime(p) and is_prime(p + 2):
        print(p, p + 2)
