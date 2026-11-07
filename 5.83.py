a = float(input("Введите вещественное число a: "))
n = int(input("Введите натуральное число n: "))
p = 1
for i in range(n):
    p = p * a
print(f"a^{n} =", p)
