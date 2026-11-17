def sign(a):
    if a < 0:
        return -1
    if a == 0:
        return 0
    return 1


x = float(input("Введите x: "))
y = float(input("Введите y: "))

# 1)
if x < 0:
    s1 = -1
elif x == 0:
    s1 = 0
else:
    s1 = 1
if y < 0:
    s2 = -1
elif y == 0:
    s2 = 0
else:
    s2 = 1
print("1) z =", s1 + s2)

# 2)
print("2) z =", sign(x) + sign(y))
