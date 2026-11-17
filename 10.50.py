def ackermann(n, m):
    if n == 0:
        return m + 1
    if m == 0:
        return ackermann(n - 1, 1)
    return ackermann(n - 1, ackermann(n, m - 1))


print("A(1, 3) =", ackermann(1, 3))
