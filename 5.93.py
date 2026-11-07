import math

n = int(input("Введите натуральное число n: "))

# а)
sin_sum = 0
total = 0
for k in range(1, n + 1):
    sin_sum = sin_sum + math.sin(k)
    total = total + 1 / sin_sum
print("а)", total)

# б)
s = 0
for i in range(n):
    s = math.sqrt(2 + s)
print("б)", s)

# в)
cos_sum = 0
sin_sum = 0
total = 0
for k in range(1, n + 1):
    cos_sum = cos_sum + math.cos(k)
    sin_sum = sin_sum + math.sin(k)
    total = total + cos_sum / sin_sum
print("в)", total)

# г)
s = 0
for k in range(n, 0, -1):
    s = math.sqrt(3 * k + s)
print("г)", s)
