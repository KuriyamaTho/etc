a = float(input("Введите вещественное число a: "))
n = int(input("Введите натуральное число n: "))
p = 1
for i in range(1, n + 1):
    p = p * a
    print(f"a^{i} =", p)
