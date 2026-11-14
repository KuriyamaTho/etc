n = float(input("Введите число n: "))
x = float(input("Введите a1: "))
i = 1
s = 0
prev = x
prev_i = 1
while x < n:
    s = s + x
    prev = x
    prev_i = i
    i = i + 1
    x = float(input(f"Введите a{i}: "))
print("а) Сумма чисел, меньших n:", s)
print("б) Элементы, между которыми находится n:")
print("   a" + str(prev_i), "=", prev)
print("   a" + str(i), "=", x)
