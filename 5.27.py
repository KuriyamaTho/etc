# а)
s = 0
for i in range(100, 501):
    s = s + i
print("а)", s)

# б)
a = int(input("б) Введите a (a <= 500): "))
s = 0
for i in range(a, 501):
    s = s + i
print("б)", s)

# в)
b = int(input("в) Введите b (b >= -10): "))
s = 0
for i in range(-10, b + 1):
    s = s + i
print("в)", s)

# г)
a = int(input("г) Введите a: "))
b = int(input("г) Введите b (b >= a): "))
s = 0
for i in range(a, b + 1):
    s = s + i
print("г)", s)
