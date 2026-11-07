import math

n = 100000
h = math.pi / n
s = 0
for i in range(n):
    s = s + math.sin((i + 0.5) * h) * h
print("Площадь одной арки синусоиды (приближенно):", s)
