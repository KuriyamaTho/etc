def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True


for n in range(100, 1000):
    if is_prime(n):
        print(n)
