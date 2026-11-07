# а)
k = int(input("а) Введите номер члена последовательности k: "))
p1 = 1
p2 = 2
q1 = 1
q2 = 1
for i in range(k - 1):
    p3 = p1 + p2
    p1 = p2
    p2 = p3
    q3 = q1 + q2
    q1 = q2
    q2 = q3
print("а) k-й член:", f"{p1}/{q1}", "=", p1 / q1)

# б)
n = int(input("б) Введите n: "))
p1 = 1
p2 = 2
q1 = 1
q2 = 1
for i in range(n):
    print(f"{p1}/{q1}", "=", p1 / q1)
    p3 = p1 + p2
    p1 = p2
    p2 = p3
    q3 = q1 + q2
    q1 = q2
    q2 = q3

# в)
a = float(input("в) Введите число A: "))
p1 = 1
p2 = 2
q1 = 1
q2 = 1
s = 0
for i in range(n):
    s = s + p1 / q1
    p3 = p1 + p2
    p1 = p2
    p2 = p3
    q3 = q1 + q2
    q1 = q2
    q2 = q3
if s > a:
    print("в) Да, сумма первых n членов больше A:", s)
else:
    print("в) Нет, сумма первых n членов не больше A:", s)
