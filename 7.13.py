n = int(input("Введите натуральное число: "))

# а)
print("а) Делители числа:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# б)
s = 0
for i in range(1, n + 1):
    if n % i == 0:
        s = s + i
print("б) Сумма делителей:", s)

# в)
s = 0
for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 0:
        s = s + i
print("в) Сумма четных делителей:", s)

# г)
k = 0
for i in range(1, n + 1):
    if n % i == 0:
        k = k + 1
print("г) Количество делителей:", k)

# д)
k = 0
for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 1:
        k = k + 1
print("д) Количество нечетных делителей:", k)

# е)
k = 0
even = 0
for i in range(1, n + 1):
    if n % i == 0:
        k = k + 1
        if i % 2 == 0:
            even = even + 1
print("е) Количество делителей:", k, ", из них четных:", even)

# ж)
d = int(input("ж) Введите d: "))
k = 0
for i in range(1, n + 1):
    if n % i == 0 and i > d:
        k = k + 1
print("ж) Количество делителей, больших d:", k)
