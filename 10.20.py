def digit_sum3(x):
    return x // 100 + x // 10 % 10 + x % 10


for n in range(100000, 1000000):
    if digit_sum3(n // 1000) == digit_sum3(n % 1000):
        print(n)
