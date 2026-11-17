def min2(x, y):
    if x < y:
        return x
    return y


a = float(input("Введите a: "))
b = float(input("Введите b: "))

# 1)
if a < 3 * b:
    m1 = a
else:
    m1 = 3 * b
if 2 * a - b < 2 * b:
    m2 = 2 * a - b
else:
    m2 = 2 * b
print("1) z =", m1 * m2)

# 2)
print("2) z =", min2(a, 3 * b) * min2(2 * a - b, 2 * b))
