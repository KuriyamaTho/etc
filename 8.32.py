count = 0
n = 2
while count < 100:
    prime = True
    d = 2
    while d * d <= n and prime:
        if n % d == 0:
            prime = False
        d = d + 1
    if prime:
        print(n)
        count = count + 1
    n = n + 1
