n = int(input("Введите натуральное число n: "))
f = 1
for i in range(2, n + 1):
    f = f * i
print(f"{n}! =", f)
