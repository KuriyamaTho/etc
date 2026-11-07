x = 2
s = 1
for k in range(1, 11):
    s = s + (-1) ** k * (k + 1) / (k + 2) * x ** k
print("Сумма =", s)
