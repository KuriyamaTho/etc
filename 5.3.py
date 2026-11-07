# а)
for i in range(20, 36):
    print(i)

# б)
b = int(input("б) Введите b (b >= 10): "))
for i in range(10, b + 1):
    print(i ** 2)

# в)
a = int(input("в) Введите a (a <= 50): "))
for i in range(a, 51):
    print(i ** 3)

# г)
a = int(input("г) Введите a: "))
b = int(input("г) Введите b (b >= a): "))
for i in range(a, b + 1):
    print(i)
