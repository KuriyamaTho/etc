# а)
k = int(input("а) Введите номер члена последовательности k: "))
x = 0
y = 1
for i in range(k):
    z = x + y
    x = y
    y = z
print("а) k-й член последовательности:", x)

# б)
n = int(input("б) Введите n (n >= 3): "))
x = 1
y = 1
print(x)
print(y)
for i in range(3, n + 1):
    z = x + y
    x = y
    y = z
    print(z)

# в)
x = 1
y = 1
s = 2
for i in range(3, n + 1):
    z = x + y
    x = y
    y = z
    s = s + z
if s % 2 == 0:
    print("в) Да, сумма первых n членов - четное число:", s)
else:
    print("в) Нет, сумма первых n членов - нечетное число:", s)
