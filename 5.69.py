n = int(input("Введите n (n >= 4): "))
v1 = 0
v2 = 0
v3 = 1.5
for i in range(4, n + 1):
    v = (i - 1) / (i ** 2 + 1) * v3 - v2 + v1
    v1 = v2
    v2 = v3
    v3 = v
print("v_n =", v3)
