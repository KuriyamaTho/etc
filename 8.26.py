n = int(input("Введите n: "))
for i in range(1, n + 1):
    print(i, end="")
    for d in range(1, i + 1):
        if i % d == 0:
            print("+", end="")
    print()
