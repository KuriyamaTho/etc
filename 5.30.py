# а)
s = 0
for i in range(20, 41):
    s = s + i ** 3
print("а)", s)

# б)
a = int(input("б) Введите a (0 <= a <= 50): "))
s = 0
for i in range(a, 51):
    s = s + i ** 2
print("б)", s)

# в)
n = int(input("в) Введите n (1 <= n <= 100): "))
s = 0
for i in range(1, n + 1):
    s = s + i ** 2
print("в)", s)

# г)
a = int(input("г) Введите a: "))
b = int(input("г) Введите b (b >= a): "))
s = 0
for i in range(a, b + 1):
    s = s + i ** 2
print("г)", s)
