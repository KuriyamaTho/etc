# а)
s = 0
for i in range(1, 1001):
    s = s + i
print("а)", s / 1000)

# б)
b = int(input("б) Введите b (b >= 100): "))
s = 0
for i in range(100, b + 1):
    s = s + i
print("б)", s / (b - 100 + 1))

# в)
a = int(input("в) Введите a (a <= 200): "))
s = 0
for i in range(a, 201):
    s = s + i
print("в)", s / (200 - a + 1))

# г)
a = int(input("г) Введите a: "))
b = int(input("г) Введите b (b >= a): "))
s = 0
for i in range(a, b + 1):
    s = s + i
print("г)", s / (b - a + 1))
