def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f


x = (2 * factorial(5) + 3 * factorial(8)) / (factorial(6) + factorial(4))
print("x =", x)
