n = int(input("Введите натуральное число n: "))
a = 1
for k in range(1, n + 1):
    a = k * a + 1 / k
    print(f"a{k} =", a)
