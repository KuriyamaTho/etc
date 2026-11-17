def max2(x, y):
    if x > y:
        return x
    return y


a = float(input("Введите a: "))
b = float(input("Введите b: "))

# 1)
if a > 2 * b:
    m1 = a
else:
    m1 = 2 * b
if 2 * a - b > b:
    m2 = 2 * a - b
else:
    m2 = b
print("1) z =", m1 * m2)

# 2)
print("2) z =", max2(a, 2 * b) * max2(2 * a - b, b))
