n = float(input("Введите число n: "))
x = float(input("Введите a1: "))
i = 1
prev = x
while x < n:
    prev = x
    i = i + 1
    x = float(input(f"Введите a{i}: "))
if x - n < n - prev:
    print("Ближайший к n элемент: a" + str(i), "=", x)
else:
    print("Ближайший к n элемент: a" + str(i - 1), "=", prev)
