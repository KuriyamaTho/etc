import math

s = 0
for k in range(50, 0, -1):
    s = math.sqrt(k + s)
print("Сумма =", s)
