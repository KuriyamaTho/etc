s = 0
sign = -1
for k in range(1, 11):
    s = s + sign * k * k
    sign = -sign
print("Сумма =", s)
