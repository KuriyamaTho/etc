# а)
p = 1
for i in range(8, 16):
    p = p * i
print("а)", p)

# б)
a = int(input("б) Введите a (1 <= a <= 20): "))
p = 1
for i in range(a, 21):
    p = p * i
print("б)", p)

# в)
b = int(input("в) Введите b (1 <= b <= 20): "))
p = 1
for i in range(1, b + 1):
    p = p * i
print("в)", p)

# г)
a = int(input("г) Введите a: "))
b = int(input("г) Введите b (b >= a): "))
p = 1
for i in range(a, b + 1):
    p = p * i
print("г)", p)
