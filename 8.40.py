v = int(input("Введите натуральное число v: "))

# а)
print("а) Перестановки ребер считаются разными:")
for a in range(1, v + 1):
    if v % a == 0:
        for b in range(1, v // a + 1):
            if (v // a) % b == 0:
                print(a, "x", b, "x", v // a // b)

# б)
print("б) Перестановки ребер считаются совпадающими:")
for a in range(1, v + 1):
    if v % a == 0:
        for b in range(a, v // a + 1):
            if (v // a) % b == 0 and b <= v // a // b:
                print(a, "x", b, "x", v // a // b)
