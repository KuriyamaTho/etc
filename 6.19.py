p1 = 1
p2 = 2
q1 = 1
q2 = 1
k = 2
while abs(p2 / q2 - p1 / q1) > 0.001:
    p3 = p1 + p2
    p1 = p2
    p2 = p3
    q3 = q1 + q2
    q1 = q2
    q2 = q3
    k = k + 1
print("Номер члена:", k)
print("Первый такой член:", f"{p2}/{q2}", "=", p2 / q2)
